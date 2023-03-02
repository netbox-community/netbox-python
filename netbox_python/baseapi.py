import json


class baseapi:
    def __init__(self, client):
        self.client = client
        super().__init__()


class CreateableAPIResource:
    def create(self, *args, **kwargs):
        return self.client.post(self.path, json=args[0] if args else kwargs)


class DeletableAPIResource:
    def delete(self, obj):
        if obj and isinstance(obj, list):
            return self.client.delete(self.path, json=obj)
        return self.client.delete(f"{self.path}{obj}/")


class ListableAPIResource:
    def list(self, **kwargs):
        return self.client.get(self.path, params=kwargs)


class RetrievableAPIResource:
    def get(self, id):
        return self.client.get(f"{self.path}{id}/")


class UpdateableAPIResource:
    def update(self, obj, **kwargs):
        if obj and isinstance(obj, list):
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
