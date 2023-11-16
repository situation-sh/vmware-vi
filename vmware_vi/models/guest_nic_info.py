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
from vmware_vi.models.net_bios_config_info import NetBIOSConfigInfo
from vmware_vi.models.net_dns_config_info import NetDnsConfigInfo
from vmware_vi.models.net_ip_config_info import NetIpConfigInfo
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class GuestNicInfo(DataObject):
    """
    Information about each virtual network adapter configured in the guest operating system. 
    """ # noqa: E501
    network: Optional[StrictStr] = Field(default=None, description="Name of the virtual switch portgroup or dvPort connected to this adapter. ")
    ip_address: Optional[List[StrictStr]] = Field(default=None, description="Deprecated as of vSphere API 5.0, use ipConfig property.  IP addresses of the adapter. ", alias="ipAddress")
    mac_address: Optional[StrictStr] = Field(default=None, description="MAC address of the adapter. ", alias="macAddress")
    connected: StrictBool = Field(description="Flag indicating whether or not the virtual device is connected. ")
    device_config_id: StrictInt = Field(description="Link to the corresponding virtual device. ", alias="deviceConfigId")
    dns_config: Optional[NetDnsConfigInfo] = Field(default=None, alias="dnsConfig")
    ip_config: Optional[NetIpConfigInfo] = Field(default=None, alias="ipConfig")
    net_bios_config: Optional[NetBIOSConfigInfo] = Field(default=None, alias="netBIOSConfig")
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
        """Create an instance of GuestNicInfo from a JSON string"""
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
        """Create an instance of GuestNicInfo from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "_typeName": obj.get("_typeName")
        })
        return _obj

