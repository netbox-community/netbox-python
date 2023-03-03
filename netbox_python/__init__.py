"""Top-level package for NetBox Python."""

__author__ = """Arthur Hanson"""
__email__ = "ahanson@netboxlabs.com"
__version__ = "0.1.0"

from netbox_python.exceptions import NetBoxException
from netbox_python.netbox import NetBoxClient
from netbox_python.rest import Result
