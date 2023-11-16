# VirtualDiskFlatVer1BackingInfo

This data object type contains information about backing a virtual disk by using a virtual disk file on the host, in the flat file format used by GSX Server 2.x.  Flat disks are allocated when created, unlike sparse disks, which grow as needed. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**disk_mode** | **str** | The disk persistence mode.  Valid modes are: - *persistent* - *nonpersistent* - *undoable*    See also *VirtualDiskMode_enum*.  | 
**split** | **bool** | Flag to indicate the type of virtual disk file: split or monolithic.  If true, the virtual disk is stored in multiple files, each 2GB.  | [optional] 
**write_through** | **bool** | Flag to indicate whether writes should go directly to the file system or should be buffered.  | [optional] 
**content_id** | **str** | Content ID of the virtual disk file, if available.  A content ID indicates the logical contents of the disk backing and its parents.  This property is only guaranteed to be up to date if this disk backing is not currently being written to by any virtual machine.  The only supported operation is comparing if two content IDs are equal or not. The guarantee provided by the content ID is that if two disk backings have the same content ID and are not currently being written to, then reads issued from the guest operating system to those disk backings will return the same data.  ***Since:*** vSphere API 4.0  | [optional] 
**parent** | [**VirtualDiskFlatVer1BackingInfo**](VirtualDiskFlatVer1BackingInfo.md) |  | [optional] 

## Example

```python
from vmware_vi.models.virtual_disk_flat_ver1_backing_info import VirtualDiskFlatVer1BackingInfo

# TODO update the JSON string below
json = "{}"
# create an instance of VirtualDiskFlatVer1BackingInfo from a JSON string
virtual_disk_flat_ver1_backing_info_instance = VirtualDiskFlatVer1BackingInfo.from_json(json)
# print the JSON string representation of the object
print VirtualDiskFlatVer1BackingInfo.to_json()

# convert the object into a dict
virtual_disk_flat_ver1_backing_info_dict = virtual_disk_flat_ver1_backing_info_instance.to_dict()
# create an instance of VirtualDiskFlatVer1BackingInfo from a dict
virtual_disk_flat_ver1_backing_info_form_dict = virtual_disk_flat_ver1_backing_info.from_dict(virtual_disk_flat_ver1_backing_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


