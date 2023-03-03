from netbox_python.baseapi import APIResource


class circuits:
    def __init__(self, client):
        self.circuit_terminations = self._circuit_terminations(client)
        self.circuit_types = self._circuit_types(client)
        self.circuits = self._circuits(client)
        self.provider_networks = self._provider_networks(client)
        self.providers = self._providers(client)

        super().__init__()

    class _circuit_terminations(APIResource):
        path = "circuits/circuit-terminations/"

    class _circuit_types(APIResource):
        path = "circuits/circuit-types/"

    class _circuits(APIResource):
        path = "circuits/circuits/"

    class _provider_networks(APIResource):
        path = "circuits/provider_networks/"

    class _providers(APIResource):
        path = "circuits/providers/"
