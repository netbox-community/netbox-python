from netbox_python.baseapi import APIResource


class virtualization:
    def __init__(self, client):
        self.cluster_groups = self._cluster_groups(client)
        self.cluster_types = self._cluster_types(client)
        self.clusters = self._clusters(client)
        self.interfaces = self._interfaces(client)
        self.virtual_machines = self._virtual_machines(client)
        super().__init__()

    class _cluster_groups(APIResource):
        path = "virtualization/cluster-groups/"

    class _cluster_types(APIResource):
        path = "virtualization/cluster-types/"

    class _clusters(APIResource):
        path = "virtualization/clusters/"

    class _interfaces(APIResource):
        path = "virtualization/interfaces/"

    class _virtual_machines(APIResource):
        path = "virtualization/virtual-machines/"
