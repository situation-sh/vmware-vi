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
from pydantic import StrictBool, StrictInt
from pydantic import Field
from vmware_vi.models.data_object import DataObject
from vmware_vi.models.shares_info import SharesInfo
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class ResourceAllocationInfo(DataObject):
    """
    The ResourceAllocationInfo data object specifies the reserved resource requirement as well as the limit (maximum allowed usage) for a given kind of resource.  This is specified for both memory allocation (specified in MB) and CPU allocation (specified in MHz).  For a *ResourcePool*, the ResourceAllocationInfo object describes both the guaranteed amount of the resource (*ResourceAllocationInfo.reservation*) and whether or not it is expandable (*ResourceAllocationInfo.expandableReservation*). If expandableReservation is true, then the resource pool can grow its reservation dynamically by borrowing unreserved resources from its parent resource pool. For the methods *ResourcePool.CreateResourcePool*, *ResourcePool.CreateVApp* and *ResourcePool.ImportVApp*, you must provide values for all properties except overheadLimit; they are not optional. (Currently, overheadLimit is for vCenter Server use only.)  If the limit is configured, it must be greater than or equal to the reservation. 
    """ # noqa: E501
    reservation: Optional[StrictInt] = Field(default=None, description="Amount of resource that is guaranteed available to the virtual machine or resource pool.  Reserved resources are not wasted if they are not used. If the utilization is less than the reservation, the resources can be utilized by other running virtual machines. Units are MB for memory, MHz for CPU. ")
    expandable_reservation: Optional[StrictBool] = Field(default=None, description="In a resource pool with an expandable reservation, the reservation on a resource pool can grow beyond the specified value, if the parent resource pool has unreserved resources.  A non-expandable reservation is called a fixed reservation. This property is invalid for virtual machines. ", alias="expandableReservation")
    limit: Optional[StrictInt] = Field(default=None, description="The utilization of a virtual machine/resource pool will not exceed this limit, even if there are available resources.  This is typically used to ensure a consistent performance of virtual machines / resource pools independent of available resources. If set to -1, then there is no fixed limit on resource usage (only bounded by available resources and shares). Units are MB for memory, MHz for CPU. ")
    shares: Optional[SharesInfo] = None
    overhead_limit: Optional[StrictInt] = Field(default=None, description="The maximum allowed overhead memory.  For a powered on virtual machine, the overhead memory reservation cannot be larger than its overheadLimit. This property is only applicable to powered on virtual machines and is not persisted across reboots. This property is not applicable for resource pools. If set to -1, then there is no limit on reservation. Units are MB.  Note: For vCenter Server use only. Not available for other clients at this time. The server will throw an exception if you attempt to set this property.  ***Since:*** VI API 2.5 ", alias="overheadLimit")
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
        """Create an instance of ResourceAllocationInfo from a JSON string"""
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
        """Create an instance of ResourceAllocationInfo from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "_typeName": obj.get("_typeName")
        })
        return _obj


