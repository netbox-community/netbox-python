from netbox_python.baseapi import AvailableAPIResource


class ip_range:
    def __init__(self, client):
        self.available_ips = self._available_ips(client)
        super().__init__()

    class _available_ips(AvailableAPIResource):
        path = "ipam/ip-ranges/{id}/available-ips"
