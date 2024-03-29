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

from pydantic import Field
from vmware_vi.models.data_object import DataObject
from vmware_vi.models.virtual_machine_virtual_device_groups_device_group import VirtualMachineVirtualDeviceGroupsDeviceGroup
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class VirtualMachineVirtualDeviceGroups(DataObject):
    """
    The VirtualDeviceGroups data object type contains information about the backing that maps the virtual device onto a physical device for a Vendor Device Group device.  Vendor Device Groups allow third-parties to define collections of devices that must be allocated to a virtual machine as a unit. Typically, this is because the set of devices are related in a some way, e.g. a physical link connects the devices. 
    """ # noqa: E501
    device_group: Optional[List[VirtualMachineVirtualDeviceGroupsDeviceGroup]] = Field(default=None, description="Information about device groups used by this VM.  When adding a group, all devices that form the group must be added in the same request. When removing group, also all devices participating in the group must be removed. Modifying existing device group membership is not allowed. ", alias="deviceGroup")
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
        """Create an instance of VirtualMachineVirtualDeviceGroups from a JSON string"""
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
        """Create an instance of VirtualMachineVirtualDeviceGroups from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "_typeName": obj.get("_typeName")
        })
        return _obj


