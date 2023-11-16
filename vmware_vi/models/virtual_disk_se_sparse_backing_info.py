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
from vmware_vi.models.crypto_key_id import CryptoKeyId
from vmware_vi.models.virtual_device_file_backing_info import VirtualDeviceFileBackingInfo
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class VirtualDiskSeSparseBackingInfo(VirtualDeviceFileBackingInfo):
    """
    Backing type for virtual disks that use the space efficient sparse format.  Space for space efficient sparse disks is allocated on demand and optimizations are applied to achieve additional space savings. The effective space usage of such a disk can be obtained from *VirtualMachineFileLayoutEx*.  ***Since:*** vSphere API 5.1 
    """ # noqa: E501
    disk_mode: StrictStr = Field(description="The disk persistence mode.  Valid modes are: - *persistent* - *independent_persistent* - *independent_nonpersistent* - *nonpersistent* - *undoable* - *append*    See also *VirtualDiskMode_enum*.  ***Since:*** vSphere API 5.1 ", alias="diskMode")
    write_through: Optional[StrictBool] = Field(default=None, description="Flag to indicate whether writes should go directly to the file system or should be buffered.  ***Since:*** vSphere API 5.1 ", alias="writeThrough")
    uuid: Optional[StrictStr] = Field(default=None, description="Disk UUID for the virtual disk, if available.  ***Since:*** vSphere API 5.1 ")
    content_id: Optional[StrictStr] = Field(default=None, description="Content ID of the virtual disk file, if available.  A content ID indicates the logical contents of the disk backing and its parents.  This property is only guaranteed to be up to date if this disk backing is not currently being written to by any virtual machine.  The only supported operation is comparing if two content IDs are equal or not. The guarantee provided by the content ID is that if two disk backings have the same content ID and are not currently being written to, then reads issued from the guest operating system to those disk backings will return the same data.  ***Since:*** vSphere API 5.1 ", alias="contentId")
    change_id: Optional[StrictStr] = Field(default=None, description="The change ID of the virtual disk for the corresponding snapshot or virtual machine.  This can be used to track incremental changes to a virtual disk. See *VirtualMachine.QueryChangedDiskAreas*.  ***Since:*** vSphere API 5.1 ", alias="changeId")
    parent: Optional[VirtualDiskSeSparseBackingInfo] = None
    delta_disk_format: Optional[StrictStr] = Field(default=None, description="The format of the delta disk.  This field is valid only for a delta disk.  See *DeltaDiskFormat* for the supported formats. If not specified, the default value used is *redoLogFormat*.  ***Since:*** vSphere API 5.1 ", alias="deltaDiskFormat")
    digest_enabled: Optional[StrictBool] = Field(default=None, description="Indicates whether the disk backing has digest file enabled.  ***Since:*** vSphere API 5.1 ", alias="digestEnabled")
    grain_size: Optional[StrictInt] = Field(default=None, description="Specify the grain size in kB.  The default size is 4 kB.  ***Since:*** vSphere API 5.1 ", alias="grainSize")
    key_id: Optional[CryptoKeyId] = Field(default=None, alias="keyId")
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
        """Create an instance of VirtualDiskSeSparseBackingInfo from a JSON string"""
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
        """Create an instance of VirtualDiskSeSparseBackingInfo from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "_typeName": obj.get("_typeName")
        })
        return _obj

# TODO: Rewrite to not use raise_errors
VirtualDiskSeSparseBackingInfo.model_rebuild(raise_errors=False)

