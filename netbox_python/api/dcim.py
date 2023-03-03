from netbox_python.baseapi import APIResource


class dcim:
    def __init__(self, client):
        self.cable_terminations = self._cable_terminations(client)
        self.cables = self._cables(client)
        self.connected_devices = self._connected_devices(client)
        self.console_port_templates = self._console_port_templates(client)
        self.console_ports = self._console_ports(client)
        self.console_server_port_templates = self._console_server_port_templates(client)
        self.console_server_ports = self._console_server_ports(client)
        self.device_bay_templates = self._device_bay_templates(client)
        self.device_bays = self._device_bays(client)
        self.device_roles = self._device_roles(client)
        self.device_types = self._device_types(client)
        self.devices = self._devices(client)
        self.front_port_templates = self._front_port_templates(client)
        self.front_ports = self._front_ports(client)
        self.interface_templates = self._interface_templates(client)
        self.interfaces = self._interfaces(client)
        self.inventory_item_roles = self._inventory_item_roles(client)
        self.inventory_item_templates = self._inventory_item_templates(client)
        self.inventory_items = self._inventory_items(client)
        self.locations = self._locations(client)
        self.manufacturers = self._manufacturers(client)
        self.module_bay_templates = self._module_bay_templates(client)
        self.module_bays = self._module_bays(client)
        self.module_types = self._module_types(client)
        self.modules = self._modules(client)
        self.platforms = self._platforms(client)
        self.power_feeds = self._power_feeds(client)
        self.power_outlet_templates = self._power_outlet_templates(client)
        self.power_outlets = self._power_outlets(client)
        self.power_panels = self._power_panels(client)
        self.power_port_templates = self._power_port_templates(client)
        self.power_ports = self._power_ports(client)
        self.rack_reservations = self._rack_reservations(client)
        self.rack_roles = self._rack_roles(client)
        self.racks = self._racks(client)
        self.rear_port_templates = self._rear_port_templates(client)
        self.rear_ports = self._rear_ports(client)
        self.regions = self._regions(client)
        self.site_groups = self._site_groups(client)
        self.sites = self._sites(client)
        self.virtual_chassiss = self._virtual_chassiss(client)
        self.virtual_device_contexts = self._virtual_device_contexts(client)
        super().__init__()

    class _cable_terminations(APIResource):
        path = "dcim/cable-terminations/"

    class _cables(APIResource):
        path = "dcim/cables/"

    class _connected_devices(APIResource):
        path = "dcim/connected-device/"

    class _console_port_templates(APIResource):
        path = "dcim/console-port-templates/"

    class _console_ports(APIResource):
        path = "dcim/console-ports/"

    class _console_server_port_templates(APIResource):
        path = "dcim/console-server-port-templates/"

    class _console_server_ports(APIResource):
        path = "dcim/console-server-ports/"

    class _device_bay_templates(APIResource):
        path = "dcim/device-bay-templates/"

    class _device_bays(APIResource):
        path = "dcim/device-bays/"

    class _device_roles(APIResource):
        path = "dcim/device-roles/"

    class _device_types(APIResource):
        path = "dcim/device-types/"

    class _devices(APIResource):
        path = "dcim/devices/"

    class _front_port_templates(APIResource):
        path = "dcim/front-port-templates/"

    class _front_ports(APIResource):
        path = "dcim/front-ports/"

    class _interface_templates(APIResource):
        path = "dcim/interface-templates/"

    class _interfaces(APIResource):
        path = "dcim/interfaces/"

    class _inventory_item_roles(APIResource):
        path = "dcim/inventory-item-roles/"

    class _inventory_item_templates(APIResource):
        path = "dcim/inventory-item-templates/"

    class _inventory_items(APIResource):
        path = "dcim/inventory-items/"

    class _locations(APIResource):
        path = "dcim/locations/"

    class _manufacturers(APIResource):
        path = "dcim/manufacturers/"

    class _module_bay_templates(APIResource):
        path = "dcim/module-bay-templates/"

    class _module_bays(APIResource):
        path = "dcim/module-bays/"

    class _module_types(APIResource):
        path = "dcim/module-types/"

    class _modules(APIResource):
        path = "dcim/modules/"

    class _platforms(APIResource):
        path = "dcim/platforms/"

    class _power_feeds(APIResource):
        path = "dcim/power-feeds/"

    class _power_outlet_templates(APIResource):
        path = "dcim/power-outlet-templates/"

    class _power_outlets(APIResource):
        path = "dcim/power-outlets/"

    class _power_panels(APIResource):
        path = "dcim/power-panels/"

    class _power_port_templates(APIResource):
        path = "dcim/power-port-templates/"

    class _power_ports(APIResource):
        path = "dcim/power-ports/"

    class _rack_reservations(APIResource):
        path = "dcim/rack-reservations/"

    class _rack_roles(APIResource):
        path = "dcim/rack-roles/"

    class _racks(APIResource):
        path = "dcim/racks/"

    class _rear_port_templates(APIResource):
        path = "dcim/rear-port-templates/"

    class _rear_ports(APIResource):
        path = "dcim/rear-ports/"

    class _regions(APIResource):
        path = "dcim/regions/"

    class _site_groups(APIResource):
        path = "dcim/site-groups/"

    class _sites(APIResource):
        path = "dcim/sites/"

    class _virtual_chassiss(APIResource):
        path = "dcim/virtual-chassis/"

    class _virtual_device_contexts(APIResource):
        path = "dcim/virtual-device-contexts/"
