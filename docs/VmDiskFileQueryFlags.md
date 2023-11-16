# VmDiskFileQueryFlags

Details for the virtual disk primary file. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**disk_type** | **bool** | The flag to indicate whether the type of the physical disk backing the virtual disk is returned.  | 
**capacity_kb** | **bool** | The flag to indicate whether the capacity of the virtual disk from the point of view of a virtual machine is returned.  | 
**hardware_version** | **bool** | The flag to indicate whether the hardware version of the virtual disk file is returned.  | 
**controller_type** | **bool** | Deprecated as of vSphere API 5.0, this property is no longer relevant and should not be used. With the current state of emulation, we don&#39;t care about the adapter type a disk is connected to, as disks may be shuffled around. For example, a disk may be unplugged from a buslogic controller and plugged into an lsilogic controller.  The flag to indicate whether or not the controller type of the virtual disk file is returned.  ***Since:*** VI API 2.5  | [optional] 
**disk_extents** | **bool** | The flag to indicate whether or not the disk extents of the virtual disk are returned.  ***Since:*** VI API 2.5  | [optional] 
**thin** | **bool** | The flag to indicate whether the thin-ness of the disk is returned.  ***Since:*** vSphere API 4.0  | [optional] 
**encryption** | **bool** | The flag to indicate whether the encryption information of the virtual disk is returned.  ***Since:*** vSphere API 6.5  | [optional] 

## Example

```python
from vmware_vi.models.vm_disk_file_query_flags import VmDiskFileQueryFlags

# TODO update the JSON string below
json = "{}"
# create an instance of VmDiskFileQueryFlags from a JSON string
vm_disk_file_query_flags_instance = VmDiskFileQueryFlags.from_json(json)
# print the JSON string representation of the object
print VmDiskFileQueryFlags.to_json()

# convert the object into a dict
vm_disk_file_query_flags_dict = vm_disk_file_query_flags_instance.to_dict()
# create an instance of VmDiskFileQueryFlags from a dict
vm_disk_file_query_flags_form_dict = vm_disk_file_query_flags.from_dict(vm_disk_file_query_flags_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


