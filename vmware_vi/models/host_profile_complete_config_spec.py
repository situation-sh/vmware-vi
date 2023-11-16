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
from vmware_vi.models.compliance_profile import ComplianceProfile
from vmware_vi.models.host_apply_profile import HostApplyProfile
from vmware_vi.models.host_profile_config_info import HostProfileConfigInfo
from vmware_vi.models.host_profile_config_spec import HostProfileConfigSpec
from vmware_vi.models.managed_object_reference import ManagedObjectReference
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class HostProfileCompleteConfigSpec(HostProfileConfigSpec):
    """
    The *HostProfileCompleteConfigSpec* data object specifies the complete configuration for a host profile.  ***Since:*** vSphere API 4.0 
    """ # noqa: E501
    apply_profile: Optional[HostApplyProfile] = Field(default=None, alias="applyProfile")
    custom_comply_profile: Optional[ComplianceProfile] = Field(default=None, alias="customComplyProfile")
    disabled_expression_list_changed: StrictBool = Field(description="Flag indicating if this configuration specification contains changes in the *HostProfileCompleteConfigSpec.disabledExpressionList*.  If False, the Profile Engine ignores the contents of the disabled expression list.  ***Since:*** vSphere API 4.0 ", alias="disabledExpressionListChanged")
    disabled_expression_list: Optional[List[StrictStr]] = Field(default=None, description="List of expressions to be disabled.  Each entry in the list specifies a *ProfileExpression*.*ProfileExpression.id*. All expressions are enabled by default.  If you set *HostProfileCompleteConfigSpec.disabledExpressionListChanged* to True, the Profile Engine uses the contents of this list to replace the contents of the *HostProfile*.*Profile.config*.*HostProfileConfigInfo.disabledExpressionList*.  The expression list is contained in the *HostProfileConfigInfo.defaultComplyProfile*. The Profile Engine automatically generates the default compliance profile when you create a host profile.  ***Since:*** vSphere API 4.0 ", alias="disabledExpressionList")
    validator_host: Optional[ManagedObjectReference] = Field(default=None, alias="validatorHost")
    validating: Optional[StrictBool] = Field(default=None, description="If \"false\", then the host profile will be saved without being validated.  The default if not specified is \"true\". This option should be used with caution, since the resulting host profile will not be checked for errors.  ***Since:*** vSphere API 6.0 ")
    host_config: Optional[HostProfileConfigInfo] = Field(default=None, alias="hostConfig")
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
        """Create an instance of HostProfileCompleteConfigSpec from a JSON string"""
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
        """Create an instance of HostProfileCompleteConfigSpec from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "_typeName": obj.get("_typeName")
        })
        return _obj

