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
from pydantic import BaseModel, StrictInt, StrictStr
from pydantic import Field
from vmware_vi.models.id import ID
from vmware_vi.models.managed_object_reference import ManagedObjectReference
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class VstorageObjectVCenterQueryChangedDiskAreasRequestType(BaseModel):
    """
    The parameters of *VcenterVStorageObjectManager.VstorageObjectVCenterQueryChangedDiskAreas*. 
    """ # noqa: E501
    id: ID
    datastore: ManagedObjectReference
    snapshot_id: ID = Field(alias="snapshotId")
    start_offset: StrictInt = Field(description="Start Offset in bytes at which to start computing changes. Typically, callers will make multiple calls to this function, starting with startOffset 0 and then examine the \"length\" property in the returned DiskChangeInfo structure, repeatedly calling queryChangedDiskAreas until a map for the entire virtual disk has been obtained. ", alias="startOffset")
    change_id: StrictStr = Field(description="Identifier referring to a point in the past that should be used as the point in time at which to begin including changes to the disk in the result. A typical use case would be a backup application obtaining a changeId from a virtual disk's backing info when performing a backup. When a subsequent incremental backup is to be performed, this change Id can be used to obtain a list of changed areas on disk. ", alias="changeId")
    __properties: ClassVar[List[str]] = ["id", "datastore", "snapshotId", "startOffset", "changeId"]

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
        """Create an instance of VstorageObjectVCenterQueryChangedDiskAreasRequestType from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of id
        if self.id:
            _dict['id'] = self.id.to_dict()
        # override the default output from pydantic by calling `to_dict()` of datastore
        if self.datastore:
            _dict['datastore'] = self.datastore.to_dict()
        # override the default output from pydantic by calling `to_dict()` of snapshot_id
        if self.snapshot_id:
            _dict['snapshotId'] = self.snapshot_id.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of VstorageObjectVCenterQueryChangedDiskAreasRequestType from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": ID.from_dict(obj.get("id")) if obj.get("id") is not None else None,
            "datastore": ManagedObjectReference.from_dict(obj.get("datastore")) if obj.get("datastore") is not None else None,
            "snapshotId": ID.from_dict(obj.get("snapshotId")) if obj.get("snapshotId") is not None else None,
            "startOffset": obj.get("startOffset"),
            "changeId": obj.get("changeId")
        })
        return _obj


