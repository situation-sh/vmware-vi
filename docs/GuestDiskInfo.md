# GuestDiskInfo

Information about each local virtual disk configured in the guest operating system. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**disk_path** | **str** | Name of the virtual disk in the guest operating system.  For example: C:\\\\  | [optional] 
**capacity** | **int** | Total capacity of the disk, in bytes.  This is part of the virtual machine configuration.  | [optional] 
**free_space** | **int** | Free space on the disk, in bytes.  This is retrieved by VMware Tools.  | [optional] 
**filesystem_type** | **str** | Filesystem type, if known.  For example NTFS or ext3.  ***Since:*** vSphere API 7.0  | [optional] 
**mappings** | [**List[GuestInfoVirtualDiskMapping]**](GuestInfoVirtualDiskMapping.md) | VirtualDisks backing the guest partition, if known.  ***Since:*** vSphere API 7.0  | [optional] 

## Example

```python
from vmware_vi.models.guest_disk_info import GuestDiskInfo

# TODO update the JSON string below
json = "{}"
# create an instance of GuestDiskInfo from a JSON string
guest_disk_info_instance = GuestDiskInfo.from_json(json)
# print the JSON string representation of the object
print GuestDiskInfo.to_json()

# convert the object into a dict
guest_disk_info_dict = guest_disk_info_instance.to_dict()
# create an instance of GuestDiskInfo from a dict
guest_disk_info_form_dict = guest_disk_info.from_dict(guest_disk_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


