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
from pydantic import StrictBool, StrictInt, StrictStr
from pydantic import Field
from vmware_vi.models.data_object import DataObject
from vmware_vi.models.host_internet_scsi_hba_ipv6_properties import HostInternetScsiHbaIPv6Properties
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class HostInternetScsiHbaIPProperties(DataObject):
    """
    The IP properties for the host bus adapter 
    """ # noqa: E501
    mac: Optional[StrictStr] = Field(default=None, description="The MAC address. ")
    address: Optional[StrictStr] = Field(default=None, description="The current IPv4 address. ")
    dhcp_configuration_enabled: StrictBool = Field(description="True if the host bus adapter fetches its IP using DHCP. ", alias="dhcpConfigurationEnabled")
    subnet_mask: Optional[StrictStr] = Field(default=None, description="The current IPv4 subnet mask. ", alias="subnetMask")
    default_gateway: Optional[StrictStr] = Field(default=None, description="The current IPv4 gateway. ", alias="defaultGateway")
    primary_dns_server_address: Optional[StrictStr] = Field(default=None, description="The current primary DNS address. ", alias="primaryDnsServerAddress")
    alternate_dns_server_address: Optional[StrictStr] = Field(default=None, description="The current secondary DNS address. ", alias="alternateDnsServerAddress")
    ipv6_address: Optional[StrictStr] = Field(default=None, description="Deprecated since vSphere API 5.5 use { @link IPProperties#ipv6properties }.  The current IPv6 address.  ***Since:*** vSphere API 4.0 ", alias="ipv6Address")
    ipv6_subnet_mask: Optional[StrictStr] = Field(default=None, description="Deprecated since vSphere API 5.5 use { @link IPProperties#ipv6properties }.  The current IPv6 subnet mask.  ***Since:*** vSphere API 4.0 ", alias="ipv6SubnetMask")
    ipv6_default_gateway: Optional[StrictStr] = Field(default=None, description="Deprecated since vSphere API 5.5 use { @link IPProperties#ipv6properties }.  The current IPv6 default gateway.  ***Since:*** vSphere API 4.0 ", alias="ipv6DefaultGateway")
    arp_redirect_enabled: Optional[StrictBool] = Field(default=None, description="True if ARP Redirect is enabled  ***Since:*** vSphere API 4.0 ", alias="arpRedirectEnabled")
    mtu: Optional[StrictInt] = Field(default=None, description="True if the host bus adapter supports setting its MTU, (for Jumbo Frames, etc) Setting enableJumboFrames and not a numeric mtu value implies autoselection of appropriate MTU value for Jumbo Frames.  ***Since:*** vSphere API 4.0 ")
    jumbo_frames_enabled: Optional[StrictBool] = Field(default=None, alias="jumboFramesEnabled")
    ipv4_enabled: Optional[StrictBool] = Field(default=None, description="True if IPv4 is enabled.  Unset value will keep existing IPv4 enabled state as is.  ***Since:*** vSphere API 6.0 ", alias="ipv4Enabled")
    ipv6_enabled: Optional[StrictBool] = Field(default=None, description="True if IPv6 is enabled.  Unset value will keep existing IPv6 enabled state as is.  ***Since:*** vSphere API 6.0 ", alias="ipv6Enabled")
    ipv6properties: Optional[HostInternetScsiHbaIPv6Properties] = None
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
        """Create an instance of HostInternetScsiHbaIPProperties from a JSON string"""
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
        """Create an instance of HostInternetScsiHbaIPProperties from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "_typeName": obj.get("_typeName")
        })
        return _obj

