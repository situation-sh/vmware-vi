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
from pydantic import BaseModel
from pydantic import Field
from vmware_vi.models.managed_object_reference import ManagedObjectReference
from vmware_vi.models.option_value import OptionValue
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class PowerOnMultiVMRequestType(BaseModel):
    """
    The parameters of *Datacenter.PowerOnMultiVM_Task*. 
    """ # noqa: E501
    vm: List[ManagedObjectReference] = Field(description="The virtual machines to power on.  ***Required privileges:*** VirtualMachine.Interact.PowerOn  Refers instances of *VirtualMachine*. ")
    option: Optional[List[OptionValue]] = Field(default=None, description="An array of *OptionValue* options for this power-on session. The names and values of the options are defined in *ClusterPowerOnVmOption_enum*. ")
    __properties: ClassVar[List[str]] = ["vm", "option"]

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
        """Create an instance of PowerOnMultiVMRequestType from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in vm (list)
        _items = []
        if self.vm:
            for _item in self.vm:
                if _item:
                    _items.append(_item.to_dict())
            _dict['vm'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in option (list)
        _items = []
        if self.option:
            for _item in self.option:
                if _item:
                    _items.append(_item.to_dict())
            _dict['option'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of PowerOnMultiVMRequestType from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "vm": [ManagedObjectReference.from_dict(_item) for _item in obj.get("vm")] if obj.get("vm") is not None else None,
            "option": [OptionValue.from_dict(_item) for _item in obj.get("option")] if obj.get("option") is not None else None
        })
        return _obj


