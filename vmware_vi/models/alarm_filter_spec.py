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
from pydantic import StrictStr
from pydantic import Field
from vmware_vi.models.data_object import DataObject
from vmware_vi.models.managed_entity_status_enum import ManagedEntityStatusEnum
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class AlarmFilterSpec(DataObject):
    """
    Alarm Filter used to filter/group alarms.  ***Since:*** vSphere API 6.7 
    """ # noqa: E501
    status: Optional[List[ManagedEntityStatusEnum]] = Field(default=None, description="Status array which could be used to filter alarms according to their triggered state.  If all triggered alarms need to be matched an empty array or ManagedEntity::red and ManagedEntity::yellow could be filled in the array.  ***Since:*** vSphere API 6.7 ")
    type_entity: Optional[StrictStr] = Field(default=None, description="Use values from *AlarmFilterSpecAlarmTypeByEntity_enum*  ***Since:*** vSphere API 6.7 ", alias="typeEntity")
    type_trigger: Optional[StrictStr] = Field(default=None, description="Use values from *AlarmFilterSpecAlarmTypeByTrigger_enum*  ***Since:*** vSphere API 6.7 ", alias="typeTrigger")
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
        """Create an instance of AlarmFilterSpec from a JSON string"""
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
        """Create an instance of AlarmFilterSpec from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "_typeName": obj.get("_typeName")
        })
        return _obj


