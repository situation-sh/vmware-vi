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
from vmware_vi.models.virtual_machine_pci_passthrough_info import VirtualMachinePciPassthroughInfo
from vmware_vi.models.virtual_machine_sriov_device_pool_info import VirtualMachineSriovDevicePoolInfo
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class VirtualMachineSriovInfo(VirtualMachinePciPassthroughInfo):
    """
    Description of a SRIOV device that can be attached to a virtual machine.  ***Since:*** vSphere API 5.5 
    """ # noqa: E501
    virtual_function: StrictBool = Field(description="Indicates whether corresponding PCI device is a virtual function instantiated by a SR-IOV capable device.  ***Since:*** vSphere API 5.5 ", alias="virtualFunction")
    pnic: Optional[StrictStr] = Field(default=None, description="The name of the physical nic that is represented by a SR-IOV capable physical function.  ***Since:*** vSphere API 5.5 ")
    device_pool: Optional[VirtualMachineSriovDevicePoolInfo] = Field(default=None, alias="devicePool")
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
        """Create an instance of VirtualMachineSriovInfo from a JSON string"""
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
        """Create an instance of VirtualMachineSriovInfo from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "_typeName": obj.get("_typeName")
        })
        return _obj


