# HostVmfsSpec

This data object type describes the VMware File System (VMFS) creation specification.  Once created, these properties for the most part cannot be changed. There are a few exceptions. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**extent** | [**HostScsiDiskPartition**](HostScsiDiskPartition.md) |  | 
**block_size_mb** | **int** | Deprecated as of vSphere API 6.5, use *HostVmfsSpec.blockSize* instead.  The block size of VMFS in megabytes (MB).  Determines the maximum file size. If this optional property is not set, the maximum file size defaults to the maximum file size for the platform.  In VMFS2, the valid block sizes 1MB, 2MB, 4MB, 8MB, 16MB, 32MB, 64MB, 128MB, and 256MB. In VMFS3, the valid block sizes are 1MB, 2MB, 4MB, and 8MB. In VMFS5, the only valid block size is 1MB.  | [optional] 
**major_version** | **int** | Major version number of VMFS.  This can be changed if the VMFS is upgraded, but this is an irreversible change.  | 
**volume_name** | **str** | Volume name of VMFS.  | 
**block_size** | **int** | The block size of VMFS in kilotypes (KB).  Determines the maximum file size. If this optional property is not set, the maximum file size defaults to the maximum file size for the platform.  In VMFS3, the valid block sizes are 1MB, 2MB, 4MB, and 8MB. In VMFS5, the only valid block size is 1MB. In VMFS6, the valid block sizes are 64KB and 1MB.  ***Since:*** vSphere API 6.5  | [optional] 
**unmap_granularity** | **int** | The granularity of VMFS unmap operations.  VMFS unmap reclaims unused storage space. The unit is KB. The minimum unmap granularity is 8KB. The maximum unmap granularity is determined by the block size of VMFS *HostVmfsVolume.blockSize*.  ***Since:*** vSphere API 6.5  | [optional] 
**unmap_priority** | **str** | VMFS unmap priority.  VMFS unmap reclaims unused storage space. This determines the processing rate of unmaps. See *HostVmfsVolumeUnmapPriority_enum* for supported values.  ***Since:*** vSphere API 6.5  | [optional] 
**unmap_bandwidth_spec** | [**VmfsUnmapBandwidthSpec**](VmfsUnmapBandwidthSpec.md) |  | [optional] 

## Example

```python
from vmware_vi.models.host_vmfs_spec import HostVmfsSpec

# TODO update the JSON string below
json = "{}"
# create an instance of HostVmfsSpec from a JSON string
host_vmfs_spec_instance = HostVmfsSpec.from_json(json)
# print the JSON string representation of the object
print HostVmfsSpec.to_json()

# convert the object into a dict
host_vmfs_spec_dict = host_vmfs_spec_instance.to_dict()
# create an instance of HostVmfsSpec from a dict
host_vmfs_spec_form_dict = host_vmfs_spec.from_dict(host_vmfs_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


