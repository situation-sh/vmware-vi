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
from vmware_vi.models.host_file_system_volume import HostFileSystemVolume
from vmware_vi.models.host_force_mounted_info import HostForceMountedInfo
from vmware_vi.models.host_scsi_disk_partition import HostScsiDiskPartition
from vmware_vi.models.vmfs_unmap_bandwidth_spec import VmfsUnmapBandwidthSpec
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class HostVmfsVolume(HostFileSystemVolume):
    """
    The VMFS file system. 
    """ # noqa: E501
    block_size_mb: StrictInt = Field(description="Deprecated as of vSphere API 6.5, use *HostVmfsVolume.blockSize* instead.  Block size of VMFS.  Determines maximum file size. The maximum number of blocks is typically fixed with each specific version of VMFS. To increase the maximum size of a VMFS file, increase the block size.  The minimum block size is 1MB. ", alias="blockSizeMb")
    block_size: Optional[StrictInt] = Field(default=None, description="Block size of VMFS in KB.  Determines maximum file size. The maximum number of blocks is typically fixed with each specific version of VMFS. To increase the maximum size of a VMFS file, increase the block size.  The minimum block size is 1MB.  ***Since:*** vSphere API 6.5 ", alias="blockSize")
    unmap_granularity: Optional[StrictInt] = Field(default=None, description="VMFS unmap reclaims unused storage space.  This property determines the granularity of unmap operations. The unit is KB. If not specified, the default value is the same as the block size of VMFS *HostVmfsVolume.blockSize*. This property cannot be changed after a VMFS volume is created.  ***Since:*** vSphere API 6.5 ", alias="unmapGranularity")
    unmap_priority: Optional[StrictStr] = Field(default=None, description="VMFS unmap reclaims unused storage space.  This property determines the processing rate of unmaps. See *HostVmfsVolumeUnmapPriority_enum* for supported values. If not specified, the default value is *low*, which means unmap is processed at low rate. This property can be updated by calling *HostStorageSystem.UpdateVmfsUnmapPriority*.  ***Since:*** vSphere API 6.5 ", alias="unmapPriority")
    unmap_bandwidth_spec: Optional[VmfsUnmapBandwidthSpec] = Field(default=None, alias="unmapBandwidthSpec")
    max_blocks: StrictInt = Field(description="Maximum number of blocks.  Determines maximum file size along with blockSize. See information about the blockSize. ", alias="maxBlocks")
    major_version: StrictInt = Field(description="Major version number of VMFS. ", alias="majorVersion")
    version: StrictStr = Field(description="Version string.  Contains major and minor version numbers. ")
    uuid: StrictStr = Field(description="The universally unique identifier assigned to VMFS. ")
    extent: List[HostScsiDiskPartition] = Field(description="The list of partition names that comprise this disk's VMFS extents.  This property can be accessed via various enclosing objects. In VirtualCenter, where it can be accessed from multiple hosts, the value of this property may differ according to the context in which it is accessed. When accessed from the *VmfsDatastoreInfo* object, in VirtualCenter, this property reflects the extent information of any one of the hosts visible to the datastore.  For a VirtualCenter system which manages ESX Server 2.x and ESX Server 3.x hosts, this extent information is only correlatable across hosts if the extents are exposed on the same adapter on all hosts which can access them. To find the extent names for a specific host, this same property should be accessed via the host's *HostFileSystemVolume* object, by correlating the uuid of the VMFS datastore in the VmfsDatastoreInfo object to the uuid in the FileSystemVolume object.  For a Virtual Center system which manages only ESX Server hosts with versions 4.0 onwards , this extent information is correlatable across hosts, irrespective of the adapters the extents are exposed on. ")
    vmfs_upgradable: StrictBool = Field(description="Can the filesystem be upgraded to a newer version.  See also *HostStorageSystem.UpgradeVmfs*. ", alias="vmfsUpgradable")
    force_mounted_info: Optional[HostForceMountedInfo] = Field(default=None, alias="forceMountedInfo")
    ssd: Optional[StrictBool] = Field(default=None, description="Indicates whether the volume is SSD backed.  If unset, the information whether the volume is SSD backed is unknown.  ***Since:*** vSphere API 5.0 ")
    local: Optional[StrictBool] = Field(default=None, description="Indicates whether the volume is backed by local disk.  If unset, the information of the volume is local-disk backed is unknown.  ***Since:*** vSphere API 5.5 ")
    scsi_disk_type: Optional[StrictStr] = Field(default=None, description="The type of disk drives.  See *ScsiDiskType_enum* for supported types. If unset, the default disk drive type is *native512*.  ***Since:*** vSphere API 6.5 ", alias="scsiDiskType")
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
        """Create an instance of HostVmfsVolume from a JSON string"""
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
        """Create an instance of HostVmfsVolume from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "_typeName": obj.get("_typeName")
        })
        return _obj


