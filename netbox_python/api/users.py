from netbox_python.baseapi import APIResource


class users:
    def __init__(self, client):
        self.configs = self._configs(client)
        self.groups = self._groups(client)
        self.permissions = self._permissions(client)
        self.tokens = self._tokens(client)
        self.users = self._users(client)
        super().__init__()

    class _configs(APIResource):
        path = "users/config/"

    class _groups(APIResource):
        path = "users/groups/"

    class _permissions(APIResource):
        path = "users/permissions/"

    class _tokens(APIResource):
        path = "users/tokens/"

    class _users(APIResource):
        path = "users/users/"
