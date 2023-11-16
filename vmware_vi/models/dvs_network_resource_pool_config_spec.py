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
from pydantic import StrictStr
from pydantic import Field
from vmware_vi.models.data_object import DataObject
from vmware_vi.models.dvs_network_resource_pool_allocation_info import DVSNetworkResourcePoolAllocationInfo
from vmware_vi.models.dynamic_property import DynamicProperty
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class DVSNetworkResourcePoolConfigSpec(DataObject):
    """
    The *DVSNetworkResourcePoolConfigSpec* data object contains properties to create or update a network resource pool for a distributed virtual switch.  ***Since:*** vSphere API 4.1 
    """ # noqa: E501
    dynamic_property: Optional[List[DynamicProperty]] = Field(default=None, description="Set of dynamic properties.  This property is optional because only the properties of an object that are unknown to a client will be part of this set. This property is not readonly just in case we want to send such properties from a client in the future. ", alias="dynamicProperty")
    key: StrictStr = Field(description="Key of the network resource pool.  The property is ignored for *DistributedVirtualSwitch*.*DistributedVirtualSwitch.AddNetworkResourcePool* operations.  ***Since:*** vSphere API 4.1 ")
    config_version: Optional[StrictStr] = Field(default=None, description="Unique identifier for a given version of the configuration.  Each change to the configuration will update this value. This is typically implemented as a non-decreasing count or a time-stamp. However, a client should always treat this as an opaque string.  If you specify the configuration version when you update the resource configuration, the Server will apply the changes only if the specified identifier matches the current *DVSNetworkResourcePool*.*DVSNetworkResourcePool.configVersion* value. You can use this field to guard against updates that may have occurred between the time when the client reads *DVSNetworkResourcePool.configVersion* and when the configuration is applied.  ***Since:*** vSphere API 4.1 ", alias="configVersion")
    allocation_info: Optional[DVSNetworkResourcePoolAllocationInfo] = Field(default=None, alias="allocationInfo")
    name: Optional[StrictStr] = Field(default=None, description="User defined name for the resource pool.  The property is required for *DistributedVirtualSwitch*.*DistributedVirtualSwitch.AddNetworkResourcePool* operations.  ***Since:*** vSphere API 5.0 ")
    description: Optional[StrictStr] = Field(default=None, description="User-defined description for the resource pool.  ***Since:*** vSphere API 5.0 ")
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
        """Create an instance of DVSNetworkResourcePoolConfigSpec from a JSON string"""
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
        """Create an instance of DVSNetworkResourcePoolConfigSpec from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "_typeName": obj.get("_typeName")
        })
        return _obj


