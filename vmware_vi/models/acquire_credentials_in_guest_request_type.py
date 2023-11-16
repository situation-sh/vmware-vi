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
from vmware_vi.models.guest_authentication import GuestAuthentication
from vmware_vi.models.managed_object_reference import ManagedObjectReference
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class AcquireCredentialsInGuestRequestType(BaseModel):
    """
    The parameters of *GuestAuthManager.AcquireCredentialsInGuest*. 
    """ # noqa: E501
    vm: ManagedObjectReference
    requested_auth: GuestAuthentication = Field(alias="requestedAuth")
    session_id: Optional[StrictInt] = Field(default=None, description="The sessionID number should be provided only when responding to a server challenge. The sessionID number to be used with the challenge is found in the *GuestAuthenticationChallenge* object. ", alias="sessionID")
    __properties: ClassVar[List[str]] = ["vm", "requestedAuth", "sessionID"]

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
        """Create an instance of AcquireCredentialsInGuestRequestType from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of vm
        if self.vm:
            _dict['vm'] = self.vm.to_dict()
        # override the default output from pydantic by calling `to_dict()` of requested_auth
        if self.requested_auth:
            _dict['requestedAuth'] = self.requested_auth.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of AcquireCredentialsInGuestRequestType from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "vm": ManagedObjectReference.from_dict(obj.get("vm")) if obj.get("vm") is not None else None,
            "requestedAuth": GuestAuthentication.from_dict(obj.get("requestedAuth")) if obj.get("requestedAuth") is not None else None,
            "sessionID": obj.get("sessionID")
        })
        return _obj


