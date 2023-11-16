# coding: utf-8

"""
    Virtual Infrastructure JSON API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 8.0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Any, ClassVar, Dict, List, Optional
from pydantic import StrictBool, StrictStr
from pydantic import Field
from vmware_vi.models.data_object import DataObject
from vmware_vi.models.host_dhcp_service import HostDhcpService
from vmware_vi.models.host_dns_config import HostDnsConfig
from vmware_vi.models.host_ip_route_config import HostIpRouteConfig
from vmware_vi.models.host_ip_route_table_info import HostIpRouteTableInfo
from vmware_vi.models.host_nat_service import HostNatService
from vmware_vi.models.host_net_stack_instance import HostNetStackInstance
from vmware_vi.models.host_opaque_network_info import HostOpaqueNetworkInfo
from vmware_vi.models.host_opaque_switch import HostOpaqueSwitch
from vmware_vi.models.host_port_group import HostPortGroup
from vmware_vi.models.host_proxy_switch import HostProxySwitch
from vmware_vi.models.host_rdma_device import HostRdmaDevice
from vmware_vi.models.host_virtual_nic import HostVirtualNic
from vmware_vi.models.host_virtual_switch import HostVirtualSwitch
from vmware_vi.models.physical_nic import PhysicalNic
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class HostNetworkInfo(DataObject):
    """
    This data object type describes networking host configuration data objects. 
    """ # noqa: E501
    vswitch: Optional[List[HostVirtualSwitch]] = Field(default=None, description="Virtual switches configured on the host. ")
    proxy_switch: Optional[List[HostProxySwitch]] = Field(default=None, description="Proxy switches configured on the host.  ***Since:*** vSphere API 4.0 ", alias="proxySwitch")
    portgroup: Optional[List[HostPortGroup]] = Field(default=None, description="Port groups configured on the host. ")
    pnic: Optional[List[PhysicalNic]] = Field(default=None, description="Physical network adapters as seen by the primary operating system. ")
    rdma_device: Optional[List[HostRdmaDevice]] = Field(default=None, description="Remote direct memory access devices, if any are present on the host.  ***Since:*** vSphere API 7.0 ", alias="rdmaDevice")
    vnic: Optional[List[HostVirtualNic]] = Field(default=None, description="Virtual network adapters configured on the host (hosted products) or the vmkernel.  In the hosted architecture, these network adapters are used by the host to communicate with the virtual machines running on that host. In the VMkernel architecture, these virtual network adapters provide the ESX Server with external network access through a virtual switch that is bridged to a physical network adapter. The VMkernel uses these network adapters for features such as VMotion, NAS, iSCSI, and remote MKS connections. ")
    console_vnic: Optional[List[HostVirtualNic]] = Field(default=None, description="Virtual network adapters configured for use by the service console.  The service console uses this network access for system management and bootstrapping services like network boot. The two sets of virtual network adapters are mutually exclusive. A virtual network adapter in this list cannot be used for things like VMotion. Likewise, a virtual network adapter in the other list cannot be used by the service console. ", alias="consoleVnic")
    dns_config: Optional[HostDnsConfig] = Field(default=None, alias="dnsConfig")
    ip_route_config: Optional[HostIpRouteConfig] = Field(default=None, alias="ipRouteConfig")
    console_ip_route_config: Optional[HostIpRouteConfig] = Field(default=None, alias="consoleIpRouteConfig")
    route_table_info: Optional[HostIpRouteTableInfo] = Field(default=None, alias="routeTableInfo")
    dhcp: Optional[List[HostDhcpService]] = Field(default=None, description="DHCP Service instances configured on the host.  ***Since:*** VI API 2.5 ")
    nat: Optional[List[HostNatService]] = Field(default=None, description="NAT service instances configured on the host.  ***Since:*** VI API 2.5 ")
    ip_v6_enabled: Optional[StrictBool] = Field(default=None, description="Enable or disable IPv6 protocol on this system.  ***Since:*** vSphere API 4.0 ", alias="ipV6Enabled")
    at_boot_ip_v6_enabled: Optional[StrictBool] = Field(default=None, description="If true then dual IPv4/IPv6 stack enabled else IPv4 only.  ***Since:*** vSphere API 4.1 ", alias="atBootIpV6Enabled")
    net_stack_instance: Optional[List[HostNetStackInstance]] = Field(default=None, description="List of NetStackInstances  ***Since:*** vSphere API 5.5 ", alias="netStackInstance")
    opaque_switch: Optional[List[HostOpaqueSwitch]] = Field(default=None, description="List of opaque switches configured on the host.  ***Since:*** vSphere API 5.5 ", alias="opaqueSwitch")
    opaque_network: Optional[List[HostOpaqueNetworkInfo]] = Field(default=None, description="List of opaque networks  ***Since:*** vSphere API 5.5 ", alias="opaqueNetwork")
    nsx_transport_node_id: Optional[StrictStr] = Field(default=None, description="The nsx transport node Id  ***Since:*** vSphere API 7.0 ", alias="nsxTransportNodeId")
    nvds_to_vds_migration_required: Optional[StrictBool] = Field(default=None, description="Whether NSX N-VDS to VDS migration is required  ***Since:*** vSphere API 7.0.2.0 ", alias="nvdsToVdsMigrationRequired")
    migration_status: Optional[StrictStr] = Field(default=None, description="Current status of NVDS to VDS migration.  See *HostNetworkConfig*.*HostNetworkConfigMigrationStatus_enum* for supported values.  ***Since:*** vSphere API 7.0.2.0 ", alias="migrationStatus")
    __properties: ClassVar[List[str]] = ["_typeName"]

    model_config = {
        "populate_by_name": True,
        "validate_assignment": True
    }


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of HostNetworkInfo from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        _dict = self.model_dump(
            by_alias=True,
            exclude={
            },
            exclude_none=True,
        )
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of HostNetworkInfo from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "_typeName": obj.get("_typeName")
        })
        return _obj

