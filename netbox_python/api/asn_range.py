from netbox_python.baseapi import AvailableAPIResource


class asn_range:
    def __init__(self, client):
        self.available_asns = self._available_asns(client)
        super().__init__()

    class _available_asns(AvailableAPIResource):
        path = "ipam/asn-ranges/{id}/available-asns"
