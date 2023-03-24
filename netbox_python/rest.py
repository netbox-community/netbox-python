from functools import partialmethod
from json import JSONDecodeError
from typing import Any, Dict, List, Union

import requests
from requests.structures import CaseInsensitiveDict

from netbox_python.exceptions import NetBoxException

# JSONType = Union[None, bool, int, float, str, List[Any], Dict[str, Any]]


class Result:
    def __init__(
        self,
        pagination: dict = None,
        params: dict = None,
        response: requests.Response = None,
        data: List[Dict] = None,
    ):
        """
        Result returned from low-level RestAdapter
        :param pagination: {'count': int, 'next': str, 'previous': str} for paginating list returns
        :param params: dict of parmas sent in the query
        :param response: requests.response object (status, headers) from API call
        :param data: Python List of Dictionaries (or maybe just a single Dictionary on error)
        """
        self.pagination = pagination
        self.params = params
        self.response = response
        self.data = data if data else []


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

    def request(self, method: str, path: str, **kwargs) -> Result:
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
            raise NetBoxException("Request failed") from err

        if method != "DELETE":
            # Deserialize JSON output to Python object, or return failed Result on exception
            try:
                data_out = response.json()
            except (ValueError, TypeError, JSONDecodeError) as err:
                raise NetBoxException("Bad JSON in response") from err

        # If status_code in 200-299 range, return success Result with data, otherwise raise exception
        is_success = 299 >= response.status_code >= 200  # 200 to 299 is OK
        if is_success:
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
                pagination=pagination,
                params=kwargs.get("params", None),
                response=response,
                data=data_out,
            )
        raise NetBoxException(f"{response.status_code}: {response.reason}")

    get = partialmethod(request, "GET")
    post = partialmethod(request, "POST")
    put = partialmethod(request, "PUT")
    patch = partialmethod(request, "PATCH")
    delete = partialmethod(request, "DELETE")
    head = partialmethod(request, "HEAD")
    options = partialmethod(request, "OPTIONS")
