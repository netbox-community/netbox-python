from netbox_python.baseapi import APIResource


class vpn:
    def __init__(self, client):
        self.ike_policies = self._ike_policies(client)
        self.ike_proposals = self._ike_proposals(client)
        self.ipsec_policies = self._ipsec_policies(client)
        self.ipsec_proposals = self._ipsec_proposals(client)
        self.ipsec_profiles = self._ipsec_profiles(client)
        self.tunnel_groups = self._tunnel_groups(client)
        self.tunnels = self._tunnels(client)
        self.tunnel_terminations = self._tunnel_terminations(client)
        self.l2vpns = self._l2vpns(client)
        self.l2vpn_terminations = self._l2vpn_terminations(client)

        super().__init__()

    class _ike_policies(APIResource):
        path = "vpn/ike-policies/"

    class _ike_proposals(APIResource):
        path = "vpn/ike-proposals/"

    class _ipsec_policies(APIResource):
        path = "vpn/ipsec-policies/"

    class _ipsec_proposals(APIResource):
        path = "vpn/ipsec-proposals/"

    class _ipsec_profiles(APIResource):
        path = "vpn/ipsec-profiles/"

    class _tunnel_groups(APIResource):
        path = "vpn/tunnel-groups/"

    class _tunnels(APIResource):
        path = "vpn/tunnels/"

    class _tunnel_terminations(APIResource):
        path = "vpn/tunnel-terminations/"

    class _l2vpns(APIResource):
        path = "vpn/l2vpns/"

    class _l2vpn_terminations(APIResource):
        path = "vpn/l2vpn-terminations/"
