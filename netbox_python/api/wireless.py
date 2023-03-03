from netbox_python.baseapi import APIResource


class wireless:
    def __init__(self, client):
        self.wireless_lan_groups = self._wireless_lan_groups(client)
        self.wireless_lans = self._wireless_lans(client)
        self.wireless_links = self._wireless_links(client)
        super().__init__()

    class _wireless_lan_groups(APIResource):
        path = "wireless/wireless-lan-groups/"

    class _wireless_lans(APIResource):
        path = "wireless/wireless-lans/"

    class _wireless_links(APIResource):
        path = "wireless/wireless-links/"
