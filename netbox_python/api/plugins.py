from netbox_python.baseapi import APIResource


class plugins:
    def __init__(self, client):
        self.installed_plugins = self._installed_plugins(client)
        super().__init__()

    class _installed_plugins(APIResource):
        path = "plugins/installed-plugins/"
