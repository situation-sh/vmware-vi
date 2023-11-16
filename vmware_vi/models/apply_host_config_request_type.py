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
from vmware_vi.models.host_config_spec import HostConfigSpec
from vmware_vi.models.managed_object_reference import ManagedObjectReference
from vmware_vi.models.profile_deferred_policy_option_parameter import ProfileDeferredPolicyOptionParameter
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class ApplyHostConfigRequestType(BaseModel):
    """
    The parameters of *HostProfileManager.ApplyHostConfig_Task*. 
    """ # noqa: E501
    host: ManagedObjectReference
    config_spec: HostConfigSpec = Field(alias="configSpec")
    user_input: Optional[List[ProfileDeferredPolicyOptionParameter]] = Field(default=None, description="Additional host-specific data to be applied to the host. This data is the complete list of deferred parameters verified by the *HostProfile*.*HostProfile.ExecuteHostProfile* method, contained in the *ProfileExecuteResult* object returned by the method.  ***Since:*** vSphere API 4.0 ", alias="userInput")
    __properties: ClassVar[List[str]] = ["host", "configSpec", "userInput"]

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
        """Create an instance of ApplyHostConfigRequestType from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of host
        if self.host:
            _dict['host'] = self.host.to_dict()
        # override the default output from pydantic by calling `to_dict()` of config_spec
        if self.config_spec:
            _dict['configSpec'] = self.config_spec.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in user_input (list)
        _items = []
        if self.user_input:
            for _item in self.user_input:
                if _item:
                    _items.append(_item.to_dict())
            _dict['userInput'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of ApplyHostConfigRequestType from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "host": ManagedObjectReference.from_dict(obj.get("host")) if obj.get("host") is not None else None,
            "configSpec": HostConfigSpec.from_dict(obj.get("configSpec")) if obj.get("configSpec") is not None else None,
            "userInput": [ProfileDeferredPolicyOptionParameter.from_dict(_item) for _item in obj.get("userInput")] if obj.get("userInput") is not None else None
        })
        return _obj


