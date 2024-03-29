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
from vmware_vi.models.file_info import FileInfo
from vmware_vi.models.vm_disk_file_encryption_info import VmDiskFileEncryptionInfo
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class VmDiskFileInfo(FileInfo):
    """
    This data object type describes a virtual disk primary file. 
    """ # noqa: E501
    disk_type: Optional[StrictStr] = Field(default=None, description="Disk type of the virtual disk.  The specified disk type is one of the backing information types for a virtual disk.  See also *VirtualDisk*. ", alias="diskType")
    capacity_kb: Optional[StrictInt] = Field(default=None, description="The capacity of a virtual disk from the point of view of a virtual machine. ", alias="capacityKb")
    hardware_version: Optional[StrictInt] = Field(default=None, description="The hardware version of the virtual disk file. ", alias="hardwareVersion")
    controller_type: Optional[StrictStr] = Field(default=None, description="Deprecated as of vSphere API 5.0, this property is no longer relevant and should not be used. With the current state of emulation, we don't care about the adapter type a disk is connected to, as disks may be shuffled around. For example, a disk may be unplugged from a buslogic controller and plugged into an lsilogic controller.  The controller type suitable for this virtual disk.  ***Since:*** VI API 2.5 ", alias="controllerType")
    disk_extents: Optional[List[StrictStr]] = Field(default=None, description="The extents of this virtual disk specified in absolute DS paths  ***Since:*** VI API 2.5 ", alias="diskExtents")
    thin: Optional[StrictBool] = Field(default=None, description="Indicates if the disk is thin-provisioned  ***Since:*** vSphere API 4.0 ")
    encryption: Optional[VmDiskFileEncryptionInfo] = None
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
        """Create an instance of VmDiskFileInfo from a JSON string"""
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
        """Create an instance of VmDiskFileInfo from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "_typeName": obj.get("_typeName")
        })
        return _obj


