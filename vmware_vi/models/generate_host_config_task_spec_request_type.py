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
from vmware_vi.models.structured_customizations import StructuredCustomizations
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class GenerateHostConfigTaskSpecRequestType(BaseModel):
    """
    The parameters of *HostProfileManager.GenerateHostConfigTaskSpec_Task*. 
    """ # noqa: E501
    hosts_info: Optional[List[StructuredCustomizations]] = Field(default=None, description="List of host data for which configuration task list needs to be generated. The *StructuredCustomizations.customizations* value should be provided only if the host customization data for that host is invalid. If this property is not provided, the API will use the host customization data stored in VC and generate task list.  ***Since:*** vSphere API 6.5 ", alias="hostsInfo")
    __properties: ClassVar[List[str]] = ["hostsInfo"]

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
        """Create an instance of GenerateHostConfigTaskSpecRequestType from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in hosts_info (list)
        _items = []
        if self.hosts_info:
            for _item in self.hosts_info:
                if _item:
                    _items.append(_item.to_dict())
            _dict['hostsInfo'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of GenerateHostConfigTaskSpecRequestType from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "hostsInfo": [StructuredCustomizations.from_dict(_item) for _item in obj.get("hostsInfo")] if obj.get("hostsInfo") is not None else None
        })
        return _obj


