from functools import partialmethod
from json import JSONDecodeError
from typing import Any, Dict, List, Union

import requests
from requests.structures import CaseInsensitiveDict

from netbox_python.exceptions import NetBoxException

JSONType = Union[None, bool, int, float, str, List[Any], Dict[str, Any]]


class Result:
    def __init__(
        self,
        status_code: int,
        headers: CaseInsensitiveDict,
        message: str = "",
        pagination: dict = None,
        data: List[Dict] = None,
    ):
        """
        Result returned from low-level RestAdapter
        :param status_code: Standard HTTP Status code
        :param message: Human readable result
        :param data: Python List of Dictionaries (or maybe just a single Dictionary on error)
        """
        self.status_code = int(status_code)
        self.headers = headers
        self.message = str(message)
        self.data = data if data else []
        self.pagination = pagination


class RestClient:
    def __init__(self, base_url: str, **session_kwargs):
        self.base_url = base_url
        self._session = requests.Session()

        for key, value in session_kwargs.items():
            setattr(self._session, key, value)

    def __enter__(self):
        return self

    def __exit__(self, *_):
        self.close()

    def close(self):
        return self._session.close()

    def request(self, method: str, path: str, **kwargs) -> JSONType:
        url = kwargs.pop("url_override", None)
        if not url:
            url = f"{self.base_url}/{path}"

        data_out = None
        try:
            response = self._session.request(method=method, url=url, **kwargs)
            response.raise_for_status()
        except requests.HTTPError as http_error:
            raise NetBoxException(
                f"Invalid request from {self.base_url}: {http_error}"
            ) from http_error
        except requests.RequestException as err:
            # self._logger.error(msg=(str(err)))
            raise NetBoxException("Request failed") from err

        if method != "DELETE":
            # Deserialize JSON output to Python object, or return failed Result on exception
            try:
                data_out = response.json()
            except (ValueError, TypeError, JSONDecodeError) as err:
                # self._logger.error(msg=log_line_post.format(False, None, e))
                raise NetBoxException("Bad JSON in response") from err

        # If status_code in 200-299 range, return success Result with data, otherwise raise exception
        is_success = 299 >= response.status_code >= 200  # 200 to 299 is OK
        # log_line = log_line_post.format(is_success, response.status_code, response.reason)
        if is_success:
            # self._logger.debug(msg=log_line)
            # check if list - fixme: should have cleaner way to do this
            pagination = None
            if "count" in data_out and "results" in data_out:
                pagination = {
                    "count": data_out.get("count"),
                    "next": data_out.get("next"),
                    "previous": data_out.get("previous"),
                }
                data_out = data_out.get("results")

            return Result(
                response.status_code,
                headers=response.headers,
                message=response.reason,
                pagination=pagination,
                data=data_out,
            )
        # self._logger.error(msg=log_line)
        raise NetBoxException(f"{response.status_code}: {response.reason}")

    get = partialmethod(request, "GET")
    post = partialmethod(request, "POST")
    put = partialmethod(request, "PUT")
    patch = partialmethod(request, "PATCH")
    delete = partialmethod(request, "DELETE")
    head = partialmethod(request, "HEAD")
    options = partialmethod(request, "OPTIONS")
