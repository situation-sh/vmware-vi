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
from vmware_vi.models.privilege_policy_def import PrivilegePolicyDef
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class CustomFieldDef(DataObject):
    """
    Describes a custom field. 
    """ # noqa: E501
    key: StrictInt = Field(description="A unique ID used to reference this custom field in assignments.  This ID is unique for the lifetime of the field (even across rename operations). ")
    name: StrictStr = Field(description="Name of the field. ")
    type: StrictStr = Field(description="Type of the field. ")
    managed_object_type: Optional[StrictStr] = Field(default=None, description="Type of object for which the field is valid.  If not specified, the field is valid for all managed objects.  ***Since:*** VI API 2.5 ", alias="managedObjectType")
    field_def_privileges: Optional[PrivilegePolicyDef] = Field(default=None, alias="fieldDefPrivileges")
    field_instance_privileges: Optional[PrivilegePolicyDef] = Field(default=None, alias="fieldInstancePrivileges")
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
        """Create an instance of CustomFieldDef from a JSON string"""
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
        """Create an instance of CustomFieldDef from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "_typeName": obj.get("_typeName")
        })
        return _obj


