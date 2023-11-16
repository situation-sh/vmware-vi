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
from vmware_vi.models.dvs_vm_vnic_resource_allocation import DvsVmVnicResourceAllocation
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class DvsVmVnicResourcePoolConfigSpec(DataObject):
    """
    The configuration specification data object to update the resource configuration for a virtual NIC network resource pool.  ***Since:*** vSphere API 6.0 
    """ # noqa: E501
    operation: StrictStr = Field(description="The type of operation on the virtual NIC network resource pool Possible value can be of *ConfigSpecOperation_enum*  ***Since:*** vSphere API 6.0 ")
    key: Optional[StrictStr] = Field(default=None, description="The key of the network resource pool.  The property is ignored for add operations.  ***Since:*** vSphere API 6.0 ")
    config_version: Optional[StrictStr] = Field(default=None, description="The configVersion is a unique identifier for a given version of the configuration.  Each change to the configuration will update this value. This is typically implemented as a non-decreasing count or a time-stamp. However, a client should always treat this as an opaque string.  If specified when updating the resource configuration, the changes will only be applied if the current configVersion matches the specified configVersion. This field can be used to guard against updates that that may have occurred between the time when configVersion was read and when it is applied.  ***Since:*** vSphere API 6.0 ", alias="configVersion")
    allocation_info: Optional[DvsVmVnicResourceAllocation] = Field(default=None, alias="allocationInfo")
    name: Optional[StrictStr] = Field(default=None, description="The name for the virtual NIC network resource pool.  The property is required for Add operations.  ***Since:*** vSphere API 6.0 ")
    description: Optional[StrictStr] = Field(default=None, description="The description for the virtual NIC network resource pool.  ***Since:*** vSphere API 6.0 ")
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
        """Create an instance of DvsVmVnicResourcePoolConfigSpec from a JSON string"""
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
        """Create an instance of DvsVmVnicResourcePoolConfigSpec from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "_typeName": obj.get("_typeName")
        })
        return _obj


