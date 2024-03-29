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
from pydantic import BaseModel, StrictInt
from pydantic import Field
from vmware_vi.models.id import ID
from vmware_vi.models.managed_object_reference import ManagedObjectReference
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class AttachDiskRequestType(BaseModel):
    """
    The parameters of *VirtualMachine.AttachDisk_Task*. 
    """ # noqa: E501
    disk_id: ID = Field(alias="diskId")
    datastore: ManagedObjectReference
    controller_key: Optional[StrictInt] = Field(default=None, description="Key of the controller the disk will connect to. It can be unset if there is only one controller (SCSI or SATA) with the available slot in the virtual machine. If there are multiple SCSI or SATA controllers available, user must specify the controller; if there is no available controllers, a *MissingController* fault will be thrown. ", alias="controllerKey")
    unit_number: Optional[StrictInt] = Field(default=None, description="The unit number of the attached disk on its controller. If unset, the next available slot on the specified controller or the only available controller will be assigned to the attached disk. ", alias="unitNumber")
    __properties: ClassVar[List[str]] = ["diskId", "datastore", "controllerKey", "unitNumber"]

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
        """Create an instance of AttachDiskRequestType from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of disk_id
        if self.disk_id:
            _dict['diskId'] = self.disk_id.to_dict()
        # override the default output from pydantic by calling `to_dict()` of datastore
        if self.datastore:
            _dict['datastore'] = self.datastore.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of AttachDiskRequestType from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "diskId": ID.from_dict(obj.get("diskId")) if obj.get("diskId") is not None else None,
            "datastore": ManagedObjectReference.from_dict(obj.get("datastore")) if obj.get("datastore") is not None else None,
            "controllerKey": obj.get("controllerKey"),
            "unitNumber": obj.get("unitNumber")
        })
        return _obj


