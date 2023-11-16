# VirtualDiskSeSparseBackingInfo

Backing type for virtual disks that use the space efficient sparse format.  Space for space efficient sparse disks is allocated on demand and optimizations are applied to achieve additional space savings. The effective space usage of such a disk can be obtained from *VirtualMachineFileLayoutEx*.  ***Since:*** vSphere API 5.1 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**disk_mode** | **str** | The disk persistence mode.  Valid modes are: - *persistent* - *independent_persistent* - *independent_nonpersistent* - *nonpersistent* - *undoable* - *append*    See also *VirtualDiskMode_enum*.  ***Since:*** vSphere API 5.1  | 
**write_through** | **bool** | Flag to indicate whether writes should go directly to the file system or should be buffered.  ***Since:*** vSphere API 5.1  | [optional] 
**uuid** | **str** | Disk UUID for the virtual disk, if available.  ***Since:*** vSphere API 5.1  | [optional] 
**content_id** | **str** | Content ID of the virtual disk file, if available.  A content ID indicates the logical contents of the disk backing and its parents.  This property is only guaranteed to be up to date if this disk backing is not currently being written to by any virtual machine.  The only supported operation is comparing if two content IDs are equal or not. The guarantee provided by the content ID is that if two disk backings have the same content ID and are not currently being written to, then reads issued from the guest operating system to those disk backings will return the same data.  ***Since:*** vSphere API 5.1  | [optional] 
**change_id** | **str** | The change ID of the virtual disk for the corresponding snapshot or virtual machine.  This can be used to track incremental changes to a virtual disk. See *VirtualMachine.QueryChangedDiskAreas*.  ***Since:*** vSphere API 5.1  | [optional] 
**parent** | [**VirtualDiskSeSparseBackingInfo**](VirtualDiskSeSparseBackingInfo.md) |  | [optional] 
**delta_disk_format** | **str** | The format of the delta disk.  This field is valid only for a delta disk.  See *DeltaDiskFormat* for the supported formats. If not specified, the default value used is *redoLogFormat*.  ***Since:*** vSphere API 5.1  | [optional] 
**digest_enabled** | **bool** | Indicates whether the disk backing has digest file enabled.  ***Since:*** vSphere API 5.1  | [optional] 
**grain_size** | **int** | Specify the grain size in kB.  The default size is 4 kB.  ***Since:*** vSphere API 5.1  | [optional] 
**key_id** | [**CryptoKeyId**](CryptoKeyId.md) |  | [optional] 

## Example

```python
from vmware_vi.models.virtual_disk_se_sparse_backing_info import VirtualDiskSeSparseBackingInfo

# TODO update the JSON string below
json = "{}"
# create an instance of VirtualDiskSeSparseBackingInfo from a JSON string
virtual_disk_se_sparse_backing_info_instance = VirtualDiskSeSparseBackingInfo.from_json(json)
# print the JSON string representation of the object
print VirtualDiskSeSparseBackingInfo.to_json()

# convert the object into a dict
virtual_disk_se_sparse_backing_info_dict = virtual_disk_se_sparse_backing_info_instance.to_dict()
# create an instance of VirtualDiskSeSparseBackingInfo from a dict
virtual_disk_se_sparse_backing_info_form_dict = virtual_disk_se_sparse_backing_info.from_dict(virtual_disk_se_sparse_backing_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


