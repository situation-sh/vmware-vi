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
from pydantic import BaseModel
from pydantic import Field
from vmware_vi.models.v_mware_dvs_lacp_group_spec import VMwareDvsLacpGroupSpec
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class UpdateDVSLacpGroupConfigRequestType(BaseModel):
    """
    The parameters of *VmwareDistributedVirtualSwitch.UpdateDVSLacpGroupConfig_Task*. 
    """ # noqa: E501
    lacp_group_spec: List[VMwareDvsLacpGroupSpec] = Field(description="The Link Aggregation Control Protocol groups to be configured.  ***Since:*** vSphere API 5.5 ", alias="lacpGroupSpec")
    __properties: ClassVar[List[str]] = ["lacpGroupSpec"]

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
        """Create an instance of UpdateDVSLacpGroupConfigRequestType from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in lacp_group_spec (list)
        _items = []
        if self.lacp_group_spec:
            for _item in self.lacp_group_spec:
                if _item:
                    _items.append(_item.to_dict())
            _dict['lacpGroupSpec'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of UpdateDVSLacpGroupConfigRequestType from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "lacpGroupSpec": [VMwareDvsLacpGroupSpec.from_dict(_item) for _item in obj.get("lacpGroupSpec")] if obj.get("lacpGroupSpec") is not None else None
        })
        return _obj

