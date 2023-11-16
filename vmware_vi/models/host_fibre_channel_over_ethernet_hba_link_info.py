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


from typing import Any, ClassVar, Dict, List
from pydantic import StrictInt, StrictStr
from pydantic import Field
from vmware_vi.models.data_object import DataObject
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class HostFibreChannelOverEthernetHbaLinkInfo(DataObject):
    """
    Represents FCoE link information.  The link information represents a VNPort to VFPort Virtual Link, as described in the FC-BB-5 standard, with the addition of the VLAN ID over which a link exists.  ***Since:*** vSphere API 5.0 
    """ # noqa: E501
    vnport_mac: StrictStr = Field(description="VNPort MAC address, as defined by the FC-BB-5 standard.  This MAC address should be of the form \"xx:xx:xx:xx:xx:xx\", where 'x' is a hexadecimal digit. Valid MAC addresses are unicast addresses.  ***Since:*** vSphere API 5.0 ", alias="vnportMac")
    fcf_mac: StrictStr = Field(description="FCF MAC address, also known as the VFPort MAC address in the FC-BB-5 standard.  This MAC address should be of the form \"xx:xx:xx:xx:xx:xx\", where 'x' is a hexadecimal digit. Valid MAC addresses are unicast addresses.  ***Since:*** vSphere API 5.0 ", alias="fcfMac")
    vlan_id: StrictInt = Field(description="VLAN ID.  This field represents the VLAN on which an FCoE HBA was discovered. Valid numbers fall into the range \\[0,4094\\].  ***Since:*** vSphere API 5.0 ", alias="vlanId")
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
        """Create an instance of HostFibreChannelOverEthernetHbaLinkInfo from a JSON string"""
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
        """Create an instance of HostFibreChannelOverEthernetHbaLinkInfo from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "_typeName": obj.get("_typeName")
        })
        return _obj

