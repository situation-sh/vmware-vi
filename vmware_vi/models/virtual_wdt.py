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
from pydantic import StrictBool
from pydantic import Field
from vmware_vi.models.virtual_device import VirtualDevice
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class VirtualWDT(VirtualDevice):
    """
    This data object type represents a watchdog timer in a virtual machine.  ***Since:*** vSphere API 7.0 
    """ # noqa: E501
    run_on_boot: StrictBool = Field(description="Flag to indicate if the virtual watchdog timer device should be initialized as the Enabled/Stopped or Enabled/Running sub-state.  If not set, the device will default to being initialized as the Enabled/Stopped sub-state.  ***Since:*** vSphere API 7.0 ", alias="runOnBoot")
    running: StrictBool = Field(description="Flag to indicate if the virtual watchdog timer device is currently in the Enabled/Running state.  The guest can cause state changes, which will result in this flag being either set or cleared.  ***Since:*** vSphere API 7.0 ")
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
        """Create an instance of VirtualWDT from a JSON string"""
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
        """Create an instance of VirtualWDT from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "_typeName": obj.get("_typeName")
        })
        return _obj


