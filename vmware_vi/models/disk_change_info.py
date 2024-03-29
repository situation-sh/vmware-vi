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
from pydantic import StrictInt
from pydantic import Field
from vmware_vi.models.data_object import DataObject
from vmware_vi.models.disk_change_extent import DiskChangeExtent
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class DiskChangeInfo(DataObject):
    """
    Data structure to describe areas in a disk associated with this VM that have been modified since a well-defined point in the past.  Returned by *VirtualMachine.QueryChangedDiskAreas*. This data structure describes a subset of the disk identified by startOffset and length. All areas that have been modified within this interval are listed under changedArea.  ***Since:*** vSphere API 4.0 
    """ # noqa: E501
    start_offset: StrictInt = Field(description="Start offset (in bytes) of disk area described by this data structure.  ***Since:*** vSphere API 4.0 ", alias="startOffset")
    length: StrictInt = Field(description="Length (in bytes) of disk area described by this data structure.  ***Since:*** vSphere API 4.0 ")
    changed_area: Optional[List[DiskChangeExtent]] = Field(default=None, description="Modified disk areas.  Might be empty if no parts of the disk between startOffset and startOffset + length were modified.  ***Since:*** vSphere API 4.0 ", alias="changedArea")
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
        """Create an instance of DiskChangeInfo from a JSON string"""
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
        """Create an instance of DiskChangeInfo from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "_typeName": obj.get("_typeName")
        })
        return _obj


