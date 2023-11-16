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
from pydantic import StrictBool, StrictInt, StrictStr
from pydantic import Field
from vmware_vi.models.data_object import DataObject
from vmware_vi.models.virtual_device import VirtualDevice
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class VirtualHardware(DataObject):
    """
    The VirtualHardware data object type contains the complete configuration of the hardware in a virtual machine. 
    """ # noqa: E501
    num_cpu: StrictInt = Field(description="Number of virtual CPUs present in this virtual machine. ", alias="numCPU")
    num_cores_per_socket: Optional[StrictInt] = Field(default=None, description="Number of cores used to distribute virtual CPUs among sockets in this virtual machine.  This field should be ignored for powered off VM with autoCoresPerSocket equals TRUE, because the virtual socket size will be assigned during power-on. This field could be unset for releases prior to 7.0 U3, and it implies numCoresPerSocket is 1. In other cases, this field represents the actual virtual socket size seen by the virtual machine.  ***Since:*** vSphere API 5.0 ", alias="numCoresPerSocket")
    auto_cores_per_socket: Optional[StrictBool] = Field(default=None, description="Cores per socket is automatically determined. ", alias="autoCoresPerSocket")
    memory_mb: StrictInt = Field(description="Memory size, in MB. ", alias="memoryMB")
    virtual_ich7_m_present: Optional[StrictBool] = Field(default=None, description="Does this virtual machine have Virtual Intel I/O Controller Hub 7  ***Since:*** vSphere API 5.0 ", alias="virtualICH7MPresent")
    virtual_smc_present: Optional[StrictBool] = Field(default=None, description="Does this virtual machine have System Management Controller  ***Since:*** vSphere API 5.0 ", alias="virtualSMCPresent")
    device: Optional[List[VirtualDevice]] = Field(default=None, description="The set of virtual devices belonging to the virtual machine.  This list is unordered. ")
    motherboard_layout: Optional[StrictStr] = Field(default=None, description="One of motherboardLayout choices.  Default is i440bxHostBridge. See *VirtualHardware.motherboardLayout* ", alias="motherboardLayout")
    simultaneous_threads: Optional[StrictInt] = Field(default=None, description="Number of SMT (Simultaneous multithreading) threads.  If unset, then system defaults are in use. ", alias="simultaneousThreads")
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
        """Create an instance of VirtualHardware from a JSON string"""
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
        """Create an instance of VirtualHardware from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "_typeName": obj.get("_typeName")
        })
        return _obj

