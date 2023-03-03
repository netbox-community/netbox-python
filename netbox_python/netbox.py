from typing import Any, Dict, List, Union

from netbox_python.api.circuits import circuits
from netbox_python.api.core import core
from netbox_python.api.dcim import dcim
from netbox_python.api.extras import extras
from netbox_python.api.ipam import ipam
from netbox_python.api.plugins import plugins
from netbox_python.api.tenancy import tenancy
from netbox_python.api.users import users
from netbox_python.api.virtualization import virtualization
from netbox_python.api.wireless import wireless
from netbox_python.baseapi import RetrievableRootAPIResource, baseapi
from netbox_python.rest import RestClient

NETBOX_DEFAULT_HEADERS = {
    "Accept": "application/json;",
    "User-Agent": "python-requests",
}

JSONType = Union[None, bool, int, float, str, List[Any], Dict[str, Any]]


class NetBoxClient(RestClient):
    def __init__(self, base_url: str, token: str, headers: Dict[str, str] = None):
        self.status = self._status(self)
        self.token = token

        headers = headers or NETBOX_DEFAULT_HEADERS
        if token:
            headers["authorization"] = f"Token {token}"

        url = base_url = "{}/api".format(
            base_url if base_url[-1] != "/" else base_url[:-1]
        )

        self.circuits = circuits(self)
        self.core = core(self)
        self.dcim = dcim(self)
        self.extras = extras(self)
        self.ipam = ipam(self)
        self.plugins = plugins(self)
        self.tenancy = tenancy(self)
        self.users = users(self)
        self.virtualization = virtualization(self)
        self.wireless = wireless(self)

        super().__init__(base_url=url, headers=headers)

    def __enter__(self):
        return self

    class _status(baseapi, RetrievableRootAPIResource):
        path = "status/"
