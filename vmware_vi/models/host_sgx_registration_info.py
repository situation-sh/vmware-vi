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

from datetime import datetime
from typing import Any, ClassVar, Dict, List, Optional
from pydantic import StrictInt, StrictStr
from pydantic import Field
from vmware_vi.models.data_object import DataObject
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class HostSgxRegistrationInfo(DataObject):
    """
    Data object describing SGX host registration information. 
    """ # noqa: E501
    status: Optional[StrictStr] = Field(default=None, description="SGX host registration status.  Valid values come from *HostSgxRegistrationInfoRegistrationStatus_enum* enum. Set, except in case of an internal error. ")
    bios_error: Optional[StrictInt] = Field(default=None, description="BIOS error related to SGX host registration.  Set only if SGX registration status is incomplete. ", alias="biosError")
    registration_url: Optional[StrictStr] = Field(default=None, description="SGX host registration URL.  Unset if SGX registration status is not applicable or in case of an internal error. ", alias="registrationUrl")
    type: Optional[StrictStr] = Field(default=None, description="SGX host registration type.  Valid values come from *HostSgxRegistrationInfoRegistrationType_enum* enum. Unset if SGX registration status is not applicable, complete, or in case of an internal error. ")
    ppid: Optional[StrictStr] = Field(default=None, description="Platform Provisioning ID (PPID).  Hex-encoded representation of the the PPID (Platform Provisioning ID), returned as the response to a successful registration request. This field is populated only on the vCenter through which the host has been registered. ")
    last_registered_time: Optional[datetime] = Field(default=None, description="Timestamp of last successful registration from this vCenter. ", alias="lastRegisteredTime")
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
        """Create an instance of HostSgxRegistrationInfo from a JSON string"""
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
        """Create an instance of HostSgxRegistrationInfo from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "_typeName": obj.get("_typeName")
        })
        return _obj

