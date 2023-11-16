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
from pydantic import BaseModel, StrictBool, StrictStr
from pydantic import Field
from vmware_vi.models.host_connect_spec import HostConnectSpec
from vmware_vi.models.managed_object_reference import ManagedObjectReference
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class AddHostRequestType(BaseModel):
    """
    The parameters of *ClusterComputeResource.AddHost_Task*. 
    """ # noqa: E501
    spec: HostConnectSpec
    as_connected: StrictBool = Field(description="Flag to specify whether or not the host should be connected immediately after it is added. The host will not be added if a connection attempt is made and fails. ", alias="asConnected")
    resource_pool: Optional[ManagedObjectReference] = Field(default=None, alias="resourcePool")
    license: Optional[StrictStr] = Field(default=None, description="Provide a licenseKey or licenseKeyType. See *LicenseManager* ")
    __properties: ClassVar[List[str]] = ["spec", "asConnected", "resourcePool", "license"]

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
        """Create an instance of AddHostRequestType from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of spec
        if self.spec:
            _dict['spec'] = self.spec.to_dict()
        # override the default output from pydantic by calling `to_dict()` of resource_pool
        if self.resource_pool:
            _dict['resourcePool'] = self.resource_pool.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of AddHostRequestType from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "spec": HostConnectSpec.from_dict(obj.get("spec")) if obj.get("spec") is not None else None,
            "asConnected": obj.get("asConnected"),
            "resourcePool": ManagedObjectReference.from_dict(obj.get("resourcePool")) if obj.get("resourcePool") is not None else None,
            "license": obj.get("license")
        })
        return _obj


