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
from vmware_vi.models.key_any_value import KeyAnyValue
from vmware_vi.models.profile_property_path import ProfilePropertyPath
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class ProfileDeferredPolicyOptionParameter(DataObject):
    """
    The *ProfileDeferredPolicyOptionParameter* data object contains information about a single deferred parameter for host configuration. - The Server verifies deferred parameter data when it calls the   *HostProfile*.*HostProfile.ExecuteHostProfile*   method. - The client supplies deferred parameter data for host configuration when it calls the   *HostProfileManager*.*HostProfileManager.ApplyHostConfig_Task*   method. - The vCenter Server stores deferred parameter data in answer files   (*AnswerFile*.*AnswerFile.userInput*).       ***Since:*** vSphere API 4.0 
    """ # noqa: E501
    input_path: ProfilePropertyPath = Field(alias="inputPath")
    parameter: Optional[List[KeyAnyValue]] = Field(default=None, description="List that contains values for the policy parameters.  During parameter verification, this property is unspecified if the client has not provided the values for this parameter. See *ProfileExecuteResult*.*ProfileExecuteResult.requireInput*.  ***Since:*** vSphere API 4.0 ")
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
        """Create an instance of ProfileDeferredPolicyOptionParameter from a JSON string"""
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
        """Create an instance of ProfileDeferredPolicyOptionParameter from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "_typeName": obj.get("_typeName")
        })
        return _obj


