from typing import Any, Callable, Dict, List

from .rest import Result


class baseapi:
    def __init__(self, client):
        self.client = client
        super().__init__()


class CreateableAPIResource:
    def _create(self, path, *args, **kwargs) -> Result:
        return self.client.post(path, json=args[0] if args else kwargs)

    def create(self, *args, **kwargs) -> Result:
        return self._create(self.path, *args, **kwargs)


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
            result = self.client.get(self.path, url_override=next_token, params=result.params)
            yield result
            next_token = result.pagination["next"]

    def _list(self, path, **kwargs) -> Result:
        return self.client.get(path, params=kwargs)

    def list(self, **kwargs) -> Result:
        return self._list(self.path, **kwargs)

    def _all(self, path, **kwargs):
        result = None
        for page in self.paginate(self._list(path, **kwargs)):
            if not result:
                result = page
            else:
                result.data.extend(page.data)

        result.pagination["next"] = None
        result.pagination["previous"] = None
        return result

    def all(self, **kwargs):
        return self._all(self.path, **kwargs)


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


class CreateablePathAPIResource:
    def create(self, *args, **kwargs) -> Result:
        path = self.path.format(id=id)
        return self._create(path, *args, **kwargs)


class ListablePathAPIResource:
    def list(self, **kwargs) -> Result:
        path = self.path.format(id=id)
        return self._list(path, **kwargs)

    def all(self, **kwargs):
        path = self.path.format(id=id)
        return self._all(path, **kwargs)


class AvailableAPIResource(
    baseapi,
    CreateablePathAPIResource,
    ListablePathAPIResource,
):
    pass


class ElevationAPIResource(baseapi, ListablePathAPIResource):
    pass
