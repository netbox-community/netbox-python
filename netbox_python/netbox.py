from typing import Any, Dict, List, Union

from api.circuits import circuits
from api.core import core
from api.dcim import dcim
from api.extras import extras
from api.ipam import ipam
from api.plugins import plugins
from api.tenancy import tenancy
from api.users import users
from api.virtualization import virtualization
from api.wireless import wireless
from requests.auth import HTTPBasicAuth
from rest import RestClient
from baseapi import RetrievableRootAPIResource, baseapi

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
