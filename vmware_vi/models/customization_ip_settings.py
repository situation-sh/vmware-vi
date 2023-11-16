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
from pydantic import StrictStr
from pydantic import Field
from vmware_vi.models.customization_ip_generator import CustomizationIpGenerator
from vmware_vi.models.customization_ip_settings_ip_v6_address_spec import CustomizationIPSettingsIpV6AddressSpec
from vmware_vi.models.customization_net_bios_mode_enum import CustomizationNetBIOSModeEnum
from vmware_vi.models.data_object import DataObject
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class CustomizationIPSettings(DataObject):
    """
    IP settings for a virtual network adapter. 
    """ # noqa: E501
    ip: CustomizationIpGenerator
    subnet_mask: Optional[StrictStr] = Field(default=None, description="Subnet mask for this virtual network adapter. ", alias="subnetMask")
    gateway: Optional[List[StrictStr]] = Field(default=None, description="For a virtual network adapter with a static IP address, this data object type contains a list of gateways, in order of preference. ")
    ip_v6_spec: Optional[CustomizationIPSettingsIpV6AddressSpec] = Field(default=None, alias="ipV6Spec")
    dns_server_list: Optional[List[StrictStr]] = Field(default=None, description="A list of server IP addresses to use for DNS lookup in a Windows guest operating system.  In Windows, these settings are adapter-specific, whereas in Linux, they are global. As a result, the Linux guest customization process ignores this setting and looks for its DNS servers in the globalIPSettings object.  Specify these servers in order of preference. If this list is not empty, and if a DHCP IpGenerator is used, then these settings override the DHCP settings. ", alias="dnsServerList")
    dns_domain: Optional[StrictStr] = Field(default=None, description="A DNS domain suffix such as vmware.com. ", alias="dnsDomain")
    primary_wins: Optional[StrictStr] = Field(default=None, description="The IP address of the primary WINS server.  This property is ignored for Linux guest operating systems. ", alias="primaryWINS")
    secondary_wins: Optional[StrictStr] = Field(default=None, description="The IP address of the secondary WINS server.  This property is ignored for Linux guest operating systems. ", alias="secondaryWINS")
    net_bios: Optional[CustomizationNetBIOSModeEnum] = Field(default=None, alias="netBIOS")
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
        """Create an instance of CustomizationIPSettings from a JSON string"""
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
        """Create an instance of CustomizationIPSettings from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "_typeName": obj.get("_typeName")
        })
        return _obj


