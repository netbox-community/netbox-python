from netbox_python.baseapi import APIResource


class tenancy:
    def __init__(self, client):
        self.contact_assignments = self._contact_assignments(client)
        self.contact_groups = self._contact_groups(client)
        self.contact_roles = self._contact_roles(client)
        self.contacts = self._contacts(client)
        self.tenant_groups = self._tenant_groups(client)
        self.tenants = self._tenants(client)
        super().__init__()

    class _contact_assignments(APIResource):
        path = "tenancy/contact-assignments/"

    class _contact_groups(APIResource):
        path = "tenancy/contact-groups/"

    class _contact_roles(APIResource):
        path = "tenancy/contact-roles/"

    class _contacts(APIResource):
        path = "tenancy/contacts/"

    class _tenant_groups(APIResource):
        path = "tenancy/tenant-groups/"

    class _tenants(APIResource):
        path = "tenancy/tenants/"
