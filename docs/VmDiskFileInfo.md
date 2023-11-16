# VmDiskFileInfo

This data object type describes a virtual disk primary file. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**disk_type** | **str** | Disk type of the virtual disk.  The specified disk type is one of the backing information types for a virtual disk.  See also *VirtualDisk*.  | [optional] 
**capacity_kb** | **int** | The capacity of a virtual disk from the point of view of a virtual machine.  | [optional] 
**hardware_version** | **int** | The hardware version of the virtual disk file.  | [optional] 
**controller_type** | **str** | Deprecated as of vSphere API 5.0, this property is no longer relevant and should not be used. With the current state of emulation, we don&#39;t care about the adapter type a disk is connected to, as disks may be shuffled around. For example, a disk may be unplugged from a buslogic controller and plugged into an lsilogic controller.  The controller type suitable for this virtual disk.  ***Since:*** VI API 2.5  | [optional] 
**disk_extents** | **List[str]** | The extents of this virtual disk specified in absolute DS paths  ***Since:*** VI API 2.5  | [optional] 
**thin** | **bool** | Indicates if the disk is thin-provisioned  ***Since:*** vSphere API 4.0  | [optional] 
**encryption** | [**VmDiskFileEncryptionInfo**](VmDiskFileEncryptionInfo.md) |  | [optional] 

## Example

```python
from vmware_vi.models.vm_disk_file_info import VmDiskFileInfo

# TODO update the JSON string below
json = "{}"
# create an instance of VmDiskFileInfo from a JSON string
vm_disk_file_info_instance = VmDiskFileInfo.from_json(json)
# print the JSON string representation of the object
print VmDiskFileInfo.to_json()

# convert the object into a dict
vm_disk_file_info_dict = vm_disk_file_info_instance.to_dict()
# create an instance of VmDiskFileInfo from a dict
vm_disk_file_info_form_dict = vm_disk_file_info.from_dict(vm_disk_file_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


