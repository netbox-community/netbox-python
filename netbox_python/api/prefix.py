from netbox_python.baseapi import AvailableAPIResource


class prefix:
    def __init__(self, client):
        self.available_ips = self._available_ips(client)
        self.available_prefixes = self._available_prefixes(client)
        super().__init__()

    class _available_ips(AvailableAPIResource):
        path = "ipam/prefixes/{id}/available-ips"

    class _available_prefixes(AvailableAPIResource):
        path = "ipam/prefixes/{id}/available-prefixes"
