# NetBox Python

Python API client library for [NetBox](https://github.com/netbox-community/netbox).

> **Note:** This is a preliminary release and still under development.

[![Release](https://img.shields.io/github/v/release/netbox-community/netbox-python)](https://img.shields.io/github/v/release/netbox-community/netbox-python)
[![Build status](https://img.shields.io/github/actions/workflow/status/netbox-community/netbox-python/main.yml?branch=main)](https://github.com/netbox-community/netbox-python/actions/workflows/main.yml?query=branch%3Amain)
[![Commit activity](https://img.shields.io/github/commit-activity/m/netbox-community/netbox-python)](https://img.shields.io/github/commit-activity/m/netbox-community/netbox-python)
[![License](https://img.shields.io/github/license/netbox-community/netbox-python)](https://img.shields.io/github/license/netbox-community/netbox-python)

- **Github repository**: <https://github.com/netbox-community/netbox-python/>
- **Documentation** <https://netbox-community.github.io/netbox-python/>

- [Report a Bug](https://github.com/netbox-community/netbox-python/issues/new?assignees=&labels=bug&template=01_BUG_REPORT.md&title=bug%3A+)
- [Request a Feature](https://github.com/netbox-community/netbox-python/issues/new?assignees=&labels=enhancement&template=02_FEATURE_REQUEST.md&title=feat%3A+)
- [Ask a Question](https://github.com/netbox-community/netbox-python/discussions)

[![Project license](https://img.shields.io/github/license/netbox-community/netbox-python.svg?style=flat-square)](LICENSE)

[![Pull Requests welcome](https://img.shields.io/badge/PRs-welcome-ff69b4.svg?style=flat-square)](https://github.com/netbox-community/netbox-python/issues?q=is%3Aissue+is%3Aopen+label%3A%22help+wanted%22)
[![code with love by netbox-community](https://img.shields.io/badge/%3C%2F%3E%20with%20%E2%99%A5%20by-netbox-community-ff1414.svg?style=flat-square)](https://github.com/netbox-community)

<details open="open">
<summary>Table of Contents</summary>

- [About](#about)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [Roadmap](#roadmap)
- [Support](#support)
- [Contributing](#contributing)
- [Authors & contributors](#authors--contributors)
- [License](#license)

</details>

---

## About

This is a thin python wrapper over the NetBox API.

## Getting Started

To install run `pip install netbox-python`.

Alternatively, you can clone the repo and run `python setup.py install`.

## Usage

The full documentation is at https://netbox-community.github.io/netbox-python/, but the following should be enough to get started using it.

To begin, import the NetBox client and instantiate it:

```
from netbox_python import NetBoxClient, Result
nb = NetBoxClient(
    base_url="http://127.0.0.1:8000/", token="1dc6fa5bfcef8390dd83a261c36ed8f1551b2d6b"
)
```
The first argument NetBoxClient takes is the NetBox URL. The 'token' argument is from NetBox.

Now using the client you can make calls to the api, for example:

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

# 6. Bulk Create
data = [
    {"name": "foo4", "slug": "foo4"},
    {"name": "foo5", "slug": "foo5"},
    {"name": "foo6", "slug": "foo6"},
]
ret = nb.dcim.sites.create(data)

# 7. Update
ret = nb.dcim.sites.update(26, name="foo2-new", slug="foo2-new-slug")

# 8. Bulk Update
data = [
    {"id": 28, "name": "foo4-new", "slug": "foo4-new"},
    {"id": 29, "name": "foo5-new", "slug": "foo5-new"},
]
ret = nb.dcim.sites.update(data)

# 9. Delete
ret = nb.dcim.sites.delete(37)

# 10. Bulk Delete
data = [{"id": 25}, {"id": 27}]
ret = nb.dcim.sites.delete(data)
```
The methods on the api's correspond to the NetBox REST API, so ('circuits', 'core', 'dcim', 'extras', 'ipam', 'plugins', 'tenancy', 'users', 'virtualization', 'wireless')

circuits would have 'circuit_terminations', 'circuit_types', etc... off of it.  Each of the endpoints has 'list', 'get', 'create', 'update' and 'delete' functions.

## Roadmap

See the [open issues](https://github.com/netbox-community/netbox-python/issues) for a list of proposed features (and known issues).

- [Top Feature Requests](https://github.com/netbox-community/netbox-python/issues?q=label%3Aenhancement+is%3Aopen+sort%3Areactions-%2B1-desc) (Add your votes using the 👍 reaction)
- [Top Bugs](https://github.com/netbox-community/netbox-python/issues?q=is%3Aissue+is%3Aopen+label%3Abug+sort%3Areactions-%2B1-desc) (Add your votes using the 👍 reaction)
- [Newest Bugs](https://github.com/netbox-community/netbox-python/issues?q=is%3Aopen+is%3Aissue+label%3Abug)

## Support

Reach out to the maintainer at one of the following places:

- [GitHub Discussions](https://github.com/netbox-community/netbox-python/discussions)


## Contributing

First off, thanks for taking the time to contribute! Contributions are what make the open-source community such an amazing place to learn, inspire, and create. Any contributions you make will benefit everybody else and are **greatly appreciated**.


Please read [our contribution guidelines](docs/CONTRIBUTING.md), and thank you for being involved!

## Authors & contributors

The original setup of this repository is by [Arthur Hanson](https://github.com/netbox-community).

For a full list of all authors and contributors, see [the contributors page](https://github.com/netbox-community/netbox-python/contributors).


## License

This project is licensed under the **Apache Software License 2.0**.

See [LICENSE](LICENSE) for more information.
