#!/usr/bin/env python

"""The setup script."""

from setuptools import find_packages, setup

with open("README.md") as readme_file:
    readme = readme_file.read()

requirements = [
    "requests>=2.20.0,<3.0",
]

test_requirements = [
    "pytest>=3",
]

setup(
    author="Arthur Hanson",
    author_email="ahanson@netboxlabs.com",
    python_requires=">=3.8",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    description="NetBox Python API Client",
    install_requires=requirements,
    license="Apache Software License 2.0",
    long_description=readme,
    long_description_content_type="text/markdown",
    include_package_data=True,
    keywords="netbox_python",
    name="netbox_python",
    packages=find_packages(include=["netbox_python", "netbox_python.*"]),
    test_suite="tests",
    tests_require=test_requirements,
    url="https://github.com/netbox-community/netbox_python",
    version="0.1.4",
    zip_safe=False,
)
