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
from vmware_vi.models.host_dhcp_service_config import HostDhcpServiceConfig
from vmware_vi.models.host_dns_config import HostDnsConfig
from vmware_vi.models.host_ip_route_config import HostIpRouteConfig
from vmware_vi.models.host_ip_route_table_config import HostIpRouteTableConfig
from vmware_vi.models.host_nat_service_config import HostNatServiceConfig
from vmware_vi.models.host_network_config_net_stack_spec import HostNetworkConfigNetStackSpec
from vmware_vi.models.host_port_group_config import HostPortGroupConfig
from vmware_vi.models.host_proxy_switch_config import HostProxySwitchConfig
from vmware_vi.models.host_virtual_nic_config import HostVirtualNicConfig
from vmware_vi.models.host_virtual_switch_config import HostVirtualSwitchConfig
from vmware_vi.models.physical_nic_config import PhysicalNicConfig
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class HostNetworkConfig(DataObject):
    """
    This data object type describes networking host configuration data objects.  These objects contain only the configuration information for networking. The runtime information is available from the *NetworkInfo* data object type.  See also *HostNetworkInfo*. 
    """ # noqa: E501
    vswitch: Optional[List[HostVirtualSwitchConfig]] = Field(default=None, description="Virtual switches configured on the host. ")
    proxy_switch: Optional[List[HostProxySwitchConfig]] = Field(default=None, description="Host proxy switches configured on the host.  ***Since:*** vSphere API 4.0 ", alias="proxySwitch")
    portgroup: Optional[List[HostPortGroupConfig]] = Field(default=None, description="Port groups configured on the host. ")
    pnic: Optional[List[PhysicalNicConfig]] = Field(default=None, description="Physical network adapters as seen by the primary operating system. ")
    vnic: Optional[List[HostVirtualNicConfig]] = Field(default=None, description="Virtual network adapters configured for use by the host operating system network adapter. ")
    console_vnic: Optional[List[HostVirtualNicConfig]] = Field(default=None, description="Virtual network adapters configured for use by the Service Console. ", alias="consoleVnic")
    dns_config: Optional[HostDnsConfig] = Field(default=None, alias="dnsConfig")
    ip_route_config: Optional[HostIpRouteConfig] = Field(default=None, alias="ipRouteConfig")
    console_ip_route_config: Optional[HostIpRouteConfig] = Field(default=None, alias="consoleIpRouteConfig")
    route_table_config: Optional[HostIpRouteTableConfig] = Field(default=None, alias="routeTableConfig")
    dhcp: Optional[List[HostDhcpServiceConfig]] = Field(default=None, description="Dynamic Host Control Protocol (DHCP) Service instances configured on the host.  ***Since:*** VI API 2.5 ")
    nat: Optional[List[HostNatServiceConfig]] = Field(default=None, description="Network address translation (NAT) Service instances configured on the host.  ***Since:*** VI API 2.5 ")
    ip_v6_enabled: Optional[StrictBool] = Field(default=None, description="Enable or disable IPv6 protocol on this system.  This property must be set by itself, no other property can accompany this change. Following the successful change, the system should be rebooted to have the change take effect.  ***Since:*** vSphere API 4.0 ", alias="ipV6Enabled")
    net_stack_spec: Optional[List[HostNetworkConfigNetStackSpec]] = Field(default=None, description="The list of network stack instance spec  ***Since:*** vSphere API 5.5 ", alias="netStackSpec")
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
        """Create an instance of HostNetworkConfig from a JSON string"""
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
        """Create an instance of HostNetworkConfig from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "_typeName": obj.get("_typeName")
        })
        return _obj


