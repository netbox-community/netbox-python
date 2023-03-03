from netbox_python.baseapi import APIResource


class core:
    def __init__(self, client):
        self.data_files = self._data_files(client)
        self.data_sourcess = self._data_sources(client)
        super().__init__()

    class _data_files(APIResource):
        path = "core/data-files/"

    class _data_sources(APIResource):
        path = "core/data-sources/"
