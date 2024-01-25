from netbox_python.api.asn_range import asn_range
from netbox_python.api.ip_range import ip_range
from netbox_python.api.prefix import prefix
from netbox_python.api.vlan_group import vlan_group
from netbox_python.baseapi import APIResource


class ipam:
    def __init__(self, client):
        self.aggregates = self._aggregates(client)
        self.asns = self._asns(client)
        self.asn_ranges = self._asn_ranges(client)
        self.asn_range = asn_range(client)
        self.fhrp_group_assignments = self._fhrp_group_assignments(client)
        self.fhrp_groups = self._fhrp_groups(client)
        self.ip_addresses = self._ip_addresses(client)
        self.ip_ranges = self._ip_ranges(client)
        self.ip_range = ip_range(client)
        self.prefixes = self._prefixes(client)
        self.rirs = self._rirs(client)
        self.roles = self._roles(client)
        self.route_targets = self._route_targets(client)
        self.service_templates = self._service_templates(client)
        self.services = self._services(client)
        self.vlan_groups = self._vlan_groups(client)
        self.vlan_group = vlan_group(client)
        self.vlans = self._vlans(client)
        self.vrfs = self._vrfs(client)
        super().__init__()

    class _aggregates(APIResource):
        path = "ipam/aggregates/"

    class _asns(APIResource):
        path = "ipam/asns/"

    class _asn_ranges(APIResource):
        path = "ipam/asn-ranges/"

    class _fhrp_group_assignments(APIResource):
        path = "ipam/fhrp-group-assignments/"

    class _fhrp_groups(APIResource):
        path = "ipam/fhrp-groups/"

    class _ip_addresses(APIResource):
        path = "ipam/ip-addresses/"

    class _ip_ranges(APIResource):
        path = "ipam/ip-ranges/"

    class _prefixes(APIResource):
        path = "ipam/prefixes/"

    class _rirs(APIResource):
        path = "ipam/rirs/"

    class _roles(APIResource):
        path = "ipam/roles/"

    class _route_targets(APIResource):
        path = "ipam/route-targets/"

    class _service_templates(APIResource):
        path = "ipam/service-templates/"

    class _services(APIResource):
        path = "ipam/services/"

    class _vlan_groups(APIResource):
        path = "ipam/vlan-groups/"

    class _vlans(APIResource):
        path = "ipam/vlans/"

    class _vrfs(APIResource):
        path = "ipam/vrfs/"
