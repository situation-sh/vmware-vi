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
from vmware_vi.models.virtual_machine_target_info import VirtualMachineTargetInfo
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class VirtualMachineVgpuProfileInfo(VirtualMachineTargetInfo):
    """
    Description of PCI vGPU profile and its attributes.  ***Since:*** vSphere API 7.0.3.0 
    """ # noqa: E501
    profile_name: StrictStr = Field(description="The vGPU profile name.  ***Since:*** vSphere API 7.0.3.0 ", alias="profileName")
    device_vendor_id: StrictInt = Field(description="A well-known unique identifier for the device that supports this profile.  It concatenates the 16-bit PCI vendor id in lower bits followed by 16-bit PCI device id.  ***Since:*** vSphere API 7.0.3.0 ", alias="deviceVendorId")
    fb_size_in_gib: StrictInt = Field(description="The profile framebuffer size in gibibytes.  ***Since:*** vSphere API 7.0.3.0 ", alias="fbSizeInGib")
    profile_sharing: StrictStr = Field(description="Indicate how this profile is shared within device.  ***Since:*** vSphere API 7.0.3.0 ", alias="profileSharing")
    profile_class: StrictStr = Field(description="Indicate class for this profile.  ***Since:*** vSphere API 7.0.3.0 ", alias="profileClass")
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
        """Create an instance of VirtualMachineVgpuProfileInfo from a JSON string"""
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
        """Create an instance of VirtualMachineVgpuProfileInfo from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "_typeName": obj.get("_typeName")
        })
        return _obj


