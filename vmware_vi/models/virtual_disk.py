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
from vmware_vi.models.id import ID
from vmware_vi.models.shares_info import SharesInfo
from vmware_vi.models.storage_io_allocation_info import StorageIOAllocationInfo
from vmware_vi.models.virtual_device import VirtualDevice
from vmware_vi.models.virtual_disk_v_flash_cache_config_info import VirtualDiskVFlashCacheConfigInfo
from vmware_vi.models.virtual_machine_base_independent_filter_spec import VirtualMachineBaseIndependentFilterSpec
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class VirtualDisk(VirtualDevice):
    """
    This data object type contains information about a disk in a virtual machine.  The virtual disk backing object types describe the different virtual disk backings available. The disk format version in each case describes the version of the format that is used.  Supported virtual disk backings: <dl> <dt>Sparse disk format, version 1 and 2</dt> <dd>The virtual disk backing grows when needed. Supported only for VMware Server.</dd> <dt>Flat disk format, version 1 and 2</dt> <dd>The virtual disk backing is preallocated. Version 1 is supported only for VMware Server.</dd> <dt>Space efficient sparse disk format</dt> <dd>The virtual disk backing grows on demand and incorporates additional space optimizations.</dd> <dt>Raw disk format, version 2</dt> <dd>The virtual disk backing uses a full physical disk drive to back the virtual disk. Supported only for VMware Server.</dd> <dt>Partitioned raw disk format, version 2</dt> <dd>The virtual disk backing uses one or more partitions on a physical disk drive to back a virtual disk. Supported only for VMware Server.</dd> <dt>Raw disk mapping, version 1</dt> <dd>The virtual disk backing uses a raw device mapping to back the virtual disk. Supported for ESX Server 2.5 and 3.x.</dd> </dl> 
    """ # noqa: E501
    capacity_in_kb: StrictInt = Field(description="Deprecated as of vSphere API 5.5, use *VirtualDisk.capacityInBytes*.  Capacity of this virtual disk in kilobytes.  Information might be lost when actual disk size is rounded off to kilobytes. If the disk is on a Virtual Volume datastore the disk size must be a multiple of a megabyte. ", alias="capacityInKB")
    capacity_in_bytes: Optional[StrictInt] = Field(default=None, description="Capacity of this virtual disk in bytes.  Server will always populate this property. Clients must initialize it when creating a new non -RDM disk or in case they want to change the current capacity of an existing virtual disk, but can omit it otherwise. If the disk is on a Virtual Volume datastore the disk size must be a multiple of a megabyte.  ***Since:*** vSphere API 5.5 ", alias="capacityInBytes")
    shares: Optional[SharesInfo] = None
    storage_io_allocation: Optional[StorageIOAllocationInfo] = Field(default=None, alias="storageIOAllocation")
    disk_object_id: Optional[StrictStr] = Field(default=None, description="Deprecated as of vSphere API 6.5, use *VirtualDisk.vDiskId*.  Virtual disk durable and unmutable identifier.  Virtual disk has a UUID field but that can be set through VirtualDiskManager APIs. This identifier is a universally unique identifier which is not settable. VirtualDisk can remain in existence even if it is not associated with VM.  ***Since:*** vSphere API 5.5 ", alias="diskObjectId")
    v_flash_cache_config_info: Optional[VirtualDiskVFlashCacheConfigInfo] = Field(default=None, alias="vFlashCacheConfigInfo")
    iofilter: Optional[List[StrictStr]] = Field(default=None, description="IDs of the IO Filters associated with the virtual disk.  See *IoFilterInfo.id*. This information is provided when retrieving configuration information for an existing virtual machine. The client cannot modify this information on a virtual machine.  ***Since:*** vSphere API 6.0 ")
    v_disk_id: Optional[ID] = Field(default=None, alias="vDiskId")
    v_disk_version: Optional[StrictInt] = Field(default=None, description="Disk descriptor version of the virtual disk. ", alias="vDiskVersion")
    native_unmanaged_linked_clone: Optional[StrictBool] = Field(default=None, description="Indicates whether a disk with *VirtualDiskFlatVer2BackingInfo* backing is a linked clone from an unmanaged delta disk and hence the *VirtualDiskFlatVer2BackingInfo.parent* chain to this delta disk will not be available.  ***Since:*** vSphere API 6.7 ", alias="nativeUnmanagedLinkedClone")
    independent_filters: Optional[List[VirtualMachineBaseIndependentFilterSpec]] = Field(default=None, description="The IDs of the independent filters associated with the virtual disk.  This information is provided when retrieving configuration information for an existing virtual machine. The client cannot modify this information on a virtual machine.  ***Since:*** vSphere API 7.0.2.1 ", alias="independentFilters")
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
        """Create an instance of VirtualDisk from a JSON string"""
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
        """Create an instance of VirtualDisk from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "_typeName": obj.get("_typeName")
        })
        return _obj

