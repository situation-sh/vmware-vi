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
from pydantic import StrictInt, StrictStr
from pydantic import Field
from vmware_vi.models.data_object import DataObject
from vmware_vi.models.host_virtual_switch_spec import HostVirtualSwitchSpec
from vmware_vi.models.physical_nic import PhysicalNic
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class HostVirtualSwitch(DataObject):
    """
    The virtual switch is a software entity to which multiple virtual network adapters can connect to create a virtual network.  It can also be bridged to a physical network. 
    """ # noqa: E501
    name: StrictStr = Field(description="The name of the virtual switch.  Maximum length is 32 characters. ")
    key: StrictStr = Field(description="The virtual switch key. ")
    num_ports: StrictInt = Field(description="The number of ports that this virtual switch currently has. ", alias="numPorts")
    num_ports_available: StrictInt = Field(description="The number of ports that are available on this virtual switch.  There are a number of networking services that utilize a port on the virtual switch and are not accounted for in the Port array of a PortGroup. For example, each physical NIC attached to a virtual switch consumes one port. This property should be used when attempting to implement admission control for new services attaching to virtual switches. ", alias="numPortsAvailable")
    mtu: Optional[StrictInt] = Field(default=None, description="The maximum transmission unit (MTU) associated with this virtual switch in bytes.  ***Since:*** VI API 2.5 ")
    portgroup: Optional[List[HostPortGroup]] = Field(default=None, description="The list of port groups configured for this virtual switch. ")
    pnic: Optional[List[PhysicalNic]] = Field(default=None, description="The set of physical network adapters associated with this bridge. ")
    spec: HostVirtualSwitchSpec
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
        """Create an instance of HostVirtualSwitch from a JSON string"""
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
        """Create an instance of HostVirtualSwitch from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "_typeName": obj.get("_typeName")
        })
        return _obj

from vmware_vi.models.host_port_group import HostPortGroup
# TODO: Rewrite to not use raise_errors
HostVirtualSwitch.model_rebuild(raise_errors=False)
