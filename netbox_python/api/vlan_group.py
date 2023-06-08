from netbox_python.baseapi import AvailableAPIResource


class vlan_group:
    def __init__(self, client):
        self.available_vlans = self._available_vlans(client)
        super().__init__()

    class _available_vlans(AvailableAPIResource):
        path = "ipam/vlan-groups/{id}/available-vlans"
