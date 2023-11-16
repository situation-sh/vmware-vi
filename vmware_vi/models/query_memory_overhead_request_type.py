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
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class QueryMemoryOverheadRequestType(BaseModel):
    """
    The parameters of *HostSystem.QueryMemoryOverhead*. 
    """ # noqa: E501
    memory_size: StrictInt = Field(description="The amount of virtual system RAM, in bytes. For an existing virtual machine, this value can be found (in megabytes) as the memoryMB property of the *VirtualHardware*. ", alias="memorySize")
    video_ram_size: Optional[StrictInt] = Field(default=None, description="The amount of virtual video RAM, in bytes. For an existing virtual machine on a host that supports advertising this property, this value can be found (in kilobytes) as the videoRamSizeInKB property of the *VirtualMachineVideoCard*. If this parameter is left unset, the default video RAM size for virtual machines on this host is assumed. ", alias="videoRamSize")
    num_vcpus: StrictInt = Field(description="The number of virtual CPUs. For an existing virtual machine, this value can be found as the numCPU property of the *VirtualHardware*. ", alias="numVcpus")
    __properties: ClassVar[List[str]] = ["memorySize", "videoRamSize", "numVcpus"]

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
        """Create an instance of QueryMemoryOverheadRequestType from a JSON string"""
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
        """Create an instance of QueryMemoryOverheadRequestType from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "memorySize": obj.get("memorySize"),
            "videoRamSize": obj.get("videoRamSize"),
            "numVcpus": obj.get("numVcpus")
        })
        return _obj


