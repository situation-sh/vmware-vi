# HostVmfsVolume

The VMFS file system. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**block_size_mb** | **int** | Deprecated as of vSphere API 6.5, use *HostVmfsVolume.blockSize* instead.  Block size of VMFS.  Determines maximum file size. The maximum number of blocks is typically fixed with each specific version of VMFS. To increase the maximum size of a VMFS file, increase the block size.  The minimum block size is 1MB.  | 
**block_size** | **int** | Block size of VMFS in KB.  Determines maximum file size. The maximum number of blocks is typically fixed with each specific version of VMFS. To increase the maximum size of a VMFS file, increase the block size.  The minimum block size is 1MB.  ***Since:*** vSphere API 6.5  | [optional] 
**unmap_granularity** | **int** | VMFS unmap reclaims unused storage space.  This property determines the granularity of unmap operations. The unit is KB. If not specified, the default value is the same as the block size of VMFS *HostVmfsVolume.blockSize*. This property cannot be changed after a VMFS volume is created.  ***Since:*** vSphere API 6.5  | [optional] 
**unmap_priority** | **str** | VMFS unmap reclaims unused storage space.  This property determines the processing rate of unmaps. See *HostVmfsVolumeUnmapPriority_enum* for supported values. If not specified, the default value is *low*, which means unmap is processed at low rate. This property can be updated by calling *HostStorageSystem.UpdateVmfsUnmapPriority*.  ***Since:*** vSphere API 6.5  | [optional] 
**unmap_bandwidth_spec** | [**VmfsUnmapBandwidthSpec**](VmfsUnmapBandwidthSpec.md) |  | [optional] 
**max_blocks** | **int** | Maximum number of blocks.  Determines maximum file size along with blockSize. See information about the blockSize.  | 
**major_version** | **int** | Major version number of VMFS.  | 
**version** | **str** | Version string.  Contains major and minor version numbers.  | 
**uuid** | **str** | The universally unique identifier assigned to VMFS.  | 
**extent** | [**List[HostScsiDiskPartition]**](HostScsiDiskPartition.md) | The list of partition names that comprise this disk&#39;s VMFS extents.  This property can be accessed via various enclosing objects. In VirtualCenter, where it can be accessed from multiple hosts, the value of this property may differ according to the context in which it is accessed. When accessed from the *VmfsDatastoreInfo* object, in VirtualCenter, this property reflects the extent information of any one of the hosts visible to the datastore.  For a VirtualCenter system which manages ESX Server 2.x and ESX Server 3.x hosts, this extent information is only correlatable across hosts if the extents are exposed on the same adapter on all hosts which can access them. To find the extent names for a specific host, this same property should be accessed via the host&#39;s *HostFileSystemVolume* object, by correlating the uuid of the VMFS datastore in the VmfsDatastoreInfo object to the uuid in the FileSystemVolume object.  For a Virtual Center system which manages only ESX Server hosts with versions 4.0 onwards , this extent information is correlatable across hosts, irrespective of the adapters the extents are exposed on.  | 
**vmfs_upgradable** | **bool** | Can the filesystem be upgraded to a newer version.  See also *HostStorageSystem.UpgradeVmfs*.  | 
**force_mounted_info** | [**HostForceMountedInfo**](HostForceMountedInfo.md) |  | [optional] 
**ssd** | **bool** | Indicates whether the volume is SSD backed.  If unset, the information whether the volume is SSD backed is unknown.  ***Since:*** vSphere API 5.0  | [optional] 
**local** | **bool** | Indicates whether the volume is backed by local disk.  If unset, the information of the volume is local-disk backed is unknown.  ***Since:*** vSphere API 5.5  | [optional] 
**scsi_disk_type** | **str** | The type of disk drives.  See *ScsiDiskType_enum* for supported types. If unset, the default disk drive type is *native512*.  ***Since:*** vSphere API 6.5  | [optional] 

## Example

```python
from vmware_vi.models.host_vmfs_volume import HostVmfsVolume

# TODO update the JSON string below
json = "{}"
# create an instance of HostVmfsVolume from a JSON string
host_vmfs_volume_instance = HostVmfsVolume.from_json(json)
# print the JSON string representation of the object
print HostVmfsVolume.to_json()

# convert the object into a dict
host_vmfs_volume_dict = host_vmfs_volume_instance.to_dict()
# create an instance of HostVmfsVolume from a dict
host_vmfs_volume_form_dict = host_vmfs_volume.from_dict(host_vmfs_volume_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


