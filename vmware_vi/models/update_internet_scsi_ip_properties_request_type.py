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
from pydantic import BaseModel, StrictStr
from pydantic import Field
from vmware_vi.models.host_internet_scsi_hba_ip_properties import HostInternetScsiHbaIPProperties
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class UpdateInternetScsiIPPropertiesRequestType(BaseModel):
    """
    The parameters of *HostStorageSystem.UpdateInternetScsiIPProperties*. 
    """ # noqa: E501
    i_scsi_hba_device: StrictStr = Field(description="The device of the Internet SCSI HBA adapter. ", alias="iScsiHbaDevice")
    ip_properties: HostInternetScsiHbaIPProperties = Field(alias="ipProperties")
    __properties: ClassVar[List[str]] = ["iScsiHbaDevice", "ipProperties"]

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
        """Create an instance of UpdateInternetScsiIPPropertiesRequestType from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of ip_properties
        if self.ip_properties:
            _dict['ipProperties'] = self.ip_properties.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of UpdateInternetScsiIPPropertiesRequestType from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "iScsiHbaDevice": obj.get("iScsiHbaDevice"),
            "ipProperties": HostInternetScsiHbaIPProperties.from_dict(obj.get("ipProperties")) if obj.get("ipProperties") is not None else None
        })
        return _obj


