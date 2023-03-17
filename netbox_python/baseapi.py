from typing import Any, Callable, Dict, List

from .rest import Result


class baseapi:
    def __init__(self, client):
        self.client = client
        super().__init__()


class CreateableAPIResource:
    def create(self, *args, **kwargs) -> Result:
        return self.client.post(self.path, json=args[0] if args else kwargs)


class DeletableAPIResource:
    def delete(self, obj: List[Any] | str | int) -> Result:
        if isinstance(obj, list):
            return self.client.delete(self.path, json=obj)

        return self.client.delete(f"{self.path}{obj}/")


class ListableAPIResource:
    def paginate(self, result: Result) -> Result:
        next_token = result.pagination["next"]
        yield result
        while next_token:
            result = self.client.get(
                self.path, url_override=next_token, params=result.params
            )
            yield result
            next_token = result.pagination["next"]

    def list(self, **kwargs) -> Result:
        return self.client.get(self.path, params=kwargs)

    def all(self, **kwargs):
        result = None
        for page in self.paginate(self.client.get(self.path, params=kwargs)):
            if not result:
                result = page
            else:
                result.data.append(page.data)

        result.pagination["next"] = None
        result.pagination["previous"] = None
        return result


class RetrievableAPIResource:
    def get(self, id: str | int) -> Result:
        return self.client.get(f"{self.path}{id}/")


class RetrievableRootAPIResource:
    def get(self, **kwargs) -> Result:
        return self.client.get(self.path, params=kwargs)


class UpdateableAPIResource:
    def update(self, obj: List[Any] | str | int, **kwargs) -> Result:
        if isinstance(obj, list):
            return self.client.patch(self.path, json=obj)

        return self.client.patch(f"{self.path}{obj}/", json=kwargs)


class APIResource(
    baseapi,
    CreateableAPIResource,
    DeletableAPIResource,
    ListableAPIResource,
    RetrievableAPIResource,
    UpdateableAPIResource,
):
    pass


class ROAPIResource(
    baseapi,
    DeletableAPIResource,
    ListableAPIResource,
    RetrievableAPIResource,
    UpdateableAPIResource,
):
    pass
