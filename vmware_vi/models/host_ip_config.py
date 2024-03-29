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
from vmware_vi.models.host_ip_config_ip_v6_address_configuration import HostIpConfigIpV6AddressConfiguration
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class HostIpConfig(DataObject):
    """
    The IP configuration. 
    """ # noqa: E501
    dhcp: StrictBool = Field(description="The flag to indicate whether or not DHCP (dynamic host control protocol) is enabled.  If this property is set to true, the ipAddress and the subnetMask strings cannot be set explicitly. ")
    ip_address: Optional[StrictStr] = Field(default=None, description="The IP address currently used by the network adapter.  All IP addresses are specified using IPv4 dot notation. For example, \"192.168.0.1\". Subnet addresses and netmasks are specified using the same notation.  **Note**: When DHCP is enabled, this property reflects the current IP configuration and cannot be set. When DHCP is not enabled, this property can be set explicitly. ", alias="ipAddress")
    subnet_mask: Optional[StrictStr] = Field(default=None, description="The subnet mask.  **Note**: When DHCP is not enabled, this property can be set explicitly. When DHCP is enabled, this property reflects the current IP configuration and cannot be set. ", alias="subnetMask")
    ip_v6_config: Optional[HostIpConfigIpV6AddressConfiguration] = Field(default=None, alias="ipV6Config")
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
        """Create an instance of HostIpConfig from a JSON string"""
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
        """Create an instance of HostIpConfig from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "_typeName": obj.get("_typeName")
        })
        return _obj


