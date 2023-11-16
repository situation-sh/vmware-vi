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
from pydantic import BaseModel, StrictStr
from pydantic import Field
from vmware_vi.models.id import ID
from vmware_vi.models.managed_object_reference import ManagedObjectReference
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class HostRetrieveVStorageObjectMetadataRequestType(BaseModel):
    """
    The parameters of *HostVStorageObjectManager.HostRetrieveVStorageObjectMetadata*. 
    """ # noqa: E501
    id: ID
    datastore: ManagedObjectReference
    snapshot_id: Optional[ID] = Field(default=None, alias="snapshotId")
    prefix: Optional[StrictStr] = Field(default=None, description="The prefix of the metadata key that needs to be retrieved ")
    __properties: ClassVar[List[str]] = ["id", "datastore", "snapshotId", "prefix"]

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
        """Create an instance of HostRetrieveVStorageObjectMetadataRequestType from a JSON string"""
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
        """Create an instance of HostRetrieveVStorageObjectMetadataRequestType from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": ID.from_dict(obj.get("id")) if obj.get("id") is not None else None,
            "datastore": ManagedObjectReference.from_dict(obj.get("datastore")) if obj.get("datastore") is not None else None,
            "snapshotId": ID.from_dict(obj.get("snapshotId")) if obj.get("snapshotId") is not None else None,
            "prefix": obj.get("prefix")
        })
        return _obj


