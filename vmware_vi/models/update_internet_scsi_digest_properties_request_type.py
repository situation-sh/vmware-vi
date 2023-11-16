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
from vmware_vi.models.host_internet_scsi_hba_digest_properties import HostInternetScsiHbaDigestProperties
from vmware_vi.models.host_internet_scsi_hba_target_set import HostInternetScsiHbaTargetSet
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class UpdateInternetScsiDigestPropertiesRequestType(BaseModel):
    """
    The parameters of *HostStorageSystem.UpdateInternetScsiDigestProperties*. 
    """ # noqa: E501
    i_scsi_hba_device: StrictStr = Field(description="The device of the Internet SCSI HBA adapter. ", alias="iScsiHbaDevice")
    target_set: Optional[HostInternetScsiHbaTargetSet] = Field(default=None, alias="targetSet")
    digest_properties: HostInternetScsiHbaDigestProperties = Field(alias="digestProperties")
    __properties: ClassVar[List[str]] = ["iScsiHbaDevice", "targetSet", "digestProperties"]

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
        """Create an instance of UpdateInternetScsiDigestPropertiesRequestType from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of target_set
        if self.target_set:
            _dict['targetSet'] = self.target_set.to_dict()
        # override the default output from pydantic by calling `to_dict()` of digest_properties
        if self.digest_properties:
            _dict['digestProperties'] = self.digest_properties.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of UpdateInternetScsiDigestPropertiesRequestType from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "iScsiHbaDevice": obj.get("iScsiHbaDevice"),
            "targetSet": HostInternetScsiHbaTargetSet.from_dict(obj.get("targetSet")) if obj.get("targetSet") is not None else None,
            "digestProperties": HostInternetScsiHbaDigestProperties.from_dict(obj.get("digestProperties")) if obj.get("digestProperties") is not None else None
        })
        return _obj


