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
from pydantic import StrictStr
from pydantic import Field
from vmware_vi.models.data_object import DataObject
from vmware_vi.models.managed_object_reference import ManagedObjectReference
from vmware_vi.models.resource_allocation_info import ResourceAllocationInfo
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class ResourceConfigSpec(DataObject):
    """
    This data object type is a specification for a set of resources allocated to a virtual machine or a resource pool. 
    """ # noqa: E501
    entity: Optional[ManagedObjectReference] = None
    change_version: Optional[StrictStr] = Field(default=None, description="The changeVersion is a unique identifier for a given version of the configuration.  Each change to the configuration will update this value. This is typically implemented as an ever increasing count or a time-stamp. However, a client should always treat this as an opaque string.  If specified when updating the resource config., the changes will only be applied if the current changeVersion matches the specified changeVersion. This field can be used to guard against updates that has happened between the configInfo was read and until it is applied. ", alias="changeVersion")
    last_modified: Optional[datetime] = Field(default=None, description="Timestamp when the resources were last modified.  This is ignored when the object is used to update a configuration. ", alias="lastModified")
    cpu_allocation: ResourceAllocationInfo = Field(alias="cpuAllocation")
    memory_allocation: ResourceAllocationInfo = Field(alias="memoryAllocation")
    scale_descendants_shares: Optional[StrictStr] = Field(default=None, description="Specifies the scaling behavior of the shares of all descendant resource pools under a given resource pool.  See *ResourceConfigSpecScaleSharesBehavior_enum* for possible values. If any scaling behavior other than *disabled* is specified, the system will scale the CPU and memory shares allocated to each descendant resource pool with the total shares of all powered on virtual machines under each respective pool. The system will also use the *SharesInfo* set on each descendant resource pool as a multiplier for the scale. If a resource pool's shares are already scalable through the *ResourceConfigSpec.scaleDescendantsShares* setting on an ancestor resource pool, the system will not allow *ResourceConfigSpec.scaleDescendantsShares* to be set on the resource pool. The *ResourcePoolRuntimeInfo.sharesScalable* property indicates whether or not a resource pool's shares are scalable. This property does not apply to virtual machines.  ***Since:*** vSphere API 7.0 ", alias="scaleDescendantsShares")
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
        """Create an instance of ResourceConfigSpec from a JSON string"""
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
        """Create an instance of ResourceConfigSpec from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "_typeName": obj.get("_typeName")
        })
        return _obj


