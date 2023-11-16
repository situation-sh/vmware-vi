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
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class VirtualMachineVirtualNuma(DataObject):
    """
    This data object describes the virtual NUMA configuration for this virtual machine and configured through ConfigSpec. 
    """ # noqa: E501
    cores_per_numa_node: Optional[StrictInt] = Field(default=None, description="Cores per vNUMA node for this VM.  The number of vNUMA nodes is calculated by total number of cores divided by corePerNumaNode. If set to be zero, it clears any manual override and autosize vNUMA node. If set to be non zero, VM uses the value as vNUMA node size. If unset, the VM continue to follow the behavior in last poweron. ", alias="coresPerNumaNode")
    expose_vnuma_on_cpu_hotadd: Optional[StrictBool] = Field(default=None, description="Capability to expose virtual NUMA when CPU hotadd is enabled.  If set to true, ESXi will consider exposing virtual NUMA to the VM when CPU hotadd is enabled. If set to false, ESXi will enforce the VM to have single virtual NUMA node when CPU hotadd is enabled. If unset, the VM continue to follow the behavior in last poweron. ", alias="exposeVnumaOnCpuHotadd")
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
        """Create an instance of VirtualMachineVirtualNuma from a JSON string"""
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
        """Create an instance of VirtualMachineVirtualNuma from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "_typeName": obj.get("_typeName")
        })
        return _obj

