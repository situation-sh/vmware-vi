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
from vmware_vi.models.host_file_system_volume import HostFileSystemVolume
from vmware_vi.models.host_mount_info import HostMountInfo
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class HostFileSystemMountInfo(DataObject):
    """
    The *HostFileSystemMountInfo* data object describes a host mount point for a file system. 
    """ # noqa: E501
    mount_info: HostMountInfo = Field(alias="mountInfo")
    volume: HostFileSystemVolume
    v_storage_support: Optional[StrictStr] = Field(default=None, description="vStorage hardware acceleration support status.  This property represents the volume's capability for storage acceleration. See *FileSystemMountInfoVStorageSupportStatus_enum* for valid values.  If the ESX Server supports hardware acceleration, the Server can offload specific virtual machine management operations to a storage device with the hardware acceleration feature. With hardware assistance, the host performs storage operations faster and consumes less CPU, memory, and storage fabric bandwidth.  For vSphere 4.0 or earlier hosts, this value will be unset.  ***Since:*** vSphere API 4.1 ", alias="vStorageSupport")
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
        """Create an instance of HostFileSystemMountInfo from a JSON string"""
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
        """Create an instance of HostFileSystemMountInfo from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "_typeName": obj.get("_typeName")
        })
        return _obj


