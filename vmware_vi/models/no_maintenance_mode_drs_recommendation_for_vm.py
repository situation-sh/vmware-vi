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

from vmware_vi.models.vm_event import VmEvent
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class NoMaintenanceModeDrsRecommendationForVM(VmEvent):
    """
    This event records that DRS did not recommend a migration for a powered on virtual machine, even though its host is going into maintenance mode.  DRS may not be able to recommend a migration for a virtual machine for reasons, include but not limited to: - No other connected host is compatible with this virtual machine. - None of the other compatible hosts have sufficient resources   to satisfy the reservation requirements of this virtual machine. - Moving to any other host would violate a DRS rule. For example, all   other compatible hosts have some incompatible virtual machines   running. - DRS is disabled on this virtual machine. - This virtual machine was still in the process of migrating   into the host going into maintenance mode and was not   considered by DRS. - This virtual machine was in the process of migrating to another   host when the host tried to enter maintenance mode. 
    """ # noqa: E501
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
        """Create an instance of NoMaintenanceModeDrsRecommendationForVM from a JSON string"""
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
        """Create an instance of NoMaintenanceModeDrsRecommendationForVM from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "_typeName": obj.get("_typeName")
        })
        return _obj


