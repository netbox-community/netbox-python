"""Top-level package for NetBox Python."""
from importlib.metadata import version

__author__ = """Arthur Hanson"""
__email__ = "ahanson@netboxlabs.com"
__version__ = version(__name__)

from netbox_python.exceptions import NetBoxException
from netbox_python.netbox import NetBoxClient
from netbox_python.rest import Result
