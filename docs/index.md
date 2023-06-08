# netbox-python

[![Release](https://img.shields.io/github/v/release/netbox-community/netbox-python)](https://img.shields.io/github/v/release/netbox-community/netbox-python)
[![Build status](https://img.shields.io/github/actions/workflow/status/netbox-community/netbox-python/main.yml?branch=main)](https://github.com/netbox-community/netbox-python/actions/workflows/main.yml?query=branch%3Amain)
[![Commit activity](https://img.shields.io/github/commit-activity/m/netbox-community/netbox-python)](https://img.shields.io/github/commit-activity/m/netbox-community/netbox-python)
[![License](https://img.shields.io/github/license/netbox-community/netbox-python)](https://img.shields.io/github/license/netbox-community/netbox-python)

Python NetBox API Client

## Installation

To install run `pip install netbox-python`.

Alternatively, you can clone the repo and run `python setup.py install`.

## Usage

To begin, import the NetBox client and instantiate it:

```
from netbox_python import NetBoxClient, Result
nb = NetBoxClient(
    base_url="http://127.0.0.1:8000/", token="1dc6fa5bfcef8390dd83a261c36ed8f1551b2d6b"
)
```
The first argument NetBoxClient takes is the NetBox URL. The 'token' argument is from NetBox, see the [Authentication documentation](https://docs.netbox.dev/en/stable/integrations/rest-api/#authentication) in the NetBox docs for more about creating and using API Tokens.

Now using the client you can make calls to the api.

### Basic CRUD APIs

Each of these objects has the standard CRUD endpoints as follows:

```
# 1. List (paginated)
ret = nb.dcim.sites.list(limit=3)

# 2. Filtered List
ret = nb.dcim.sites.list(region_id="43")

# 3. All
ret = nb.dcim.sites.all()

# 4. Get
ret = nb.dcim.sites.get(24)

# 5. Create
ret = nb.dcim.sites.create(name="foo3", slug="foo3")

# 6. Update
ret = nb.dcim.sites.update(26, name="foo2-new", slug="foo2-new-slug")

# 7. Delete
ret = nb.dcim.sites.delete(37)
```

### Bulk APIs

In addition, bulk operations are available on the API's as well:
```
# 8. Bulk Create
data = [
    {"name": "foo4", "slug": "foo4"},
    {"name": "foo5", "slug": "foo5"},
    {"name": "foo6", "slug": "foo6"},
]
ret = nb.dcim.sites.create(data)

# 8. Bulk Update
data = [
    {"id": 28, "name": "foo4-new", "slug": "foo4-new"},
    {"id": 29, "name": "foo5-new", "slug": "foo5-new"},
]
ret = nb.dcim.sites.update(data)

# 10. Bulk Delete
data = [{"id": 25}, {"id": 27}]
ret = nb.dcim.sites.delete(data)
```
### Special APIs

In addition to the standard API calls above, devices also have a special API for rendering config context:
```
ret = nb.dcim.devices.render_config(107)
```

### Endpoints

The methods on the api's correspond to the NetBox REST API - the best reference to the objects that can be called is by using the [browsable API](https://demo.netbox.dev/api/) on the netbox instance.  The root objects that can be called are:

- circuits
- core
- dcim
- extras
- ipam
- plugins
- status
- tenancy
- users
- virtualization
- wireless

circuits would have 'circuit_terminations', 'circuit_types', etc... off of it.  Each of the endpoints has 'list', 'get', 'create', 'update' and 'delete' functions.


## Return Object

The return object from the API calls is a dictionary with two values (response and data).  **data** is the actual data returned from the call and response contains detailed information on the call, including the HTTP status code returned. Netbox-python is a wrapper around the python [requests](https://github.com/psf/requests) library. Detailed information on the response object can be found in python requests library [documentation](https://requests.readthedocs.io/en/latest/).  After making an API call you can check the status code and get the returned data as follows:

```
ret = nb.dcim.sites.all()
print(f"status code: {ret.response.status_code}")
print(ret.data)
```
