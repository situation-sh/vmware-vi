# VirtualDiskRawDiskVer2BackingInfo

This data object type contains information about backing a virtual disk by using a host device, as used by VMware Server. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**descriptor_file_name** | **str** | The name of the raw disk descriptor file.  | 
**uuid** | **str** | Disk UUID for the virtual disk, if available.  ***Since:*** VI API 2.5  | [optional] 
**change_id** | **str** | The change ID of the virtual disk for the corresponding snapshot or virtual machine.  This can be used to track incremental changes to a virtual disk. See *VirtualMachine.QueryChangedDiskAreas*.  ***Since:*** vSphere API 4.0  | [optional] 
**sharing** | **str** | The sharing mode of the virtual disk.  See *VirtualDiskSharing_enum*. The default value is no sharing.  ***Since:*** vSphere API 6.0  | [optional] 

## Example

```python
from vmware_vi.models.virtual_disk_raw_disk_ver2_backing_info import VirtualDiskRawDiskVer2BackingInfo

# TODO update the JSON string below
json = "{}"
# create an instance of VirtualDiskRawDiskVer2BackingInfo from a JSON string
virtual_disk_raw_disk_ver2_backing_info_instance = VirtualDiskRawDiskVer2BackingInfo.from_json(json)
# print the JSON string representation of the object
print VirtualDiskRawDiskVer2BackingInfo.to_json()

# convert the object into a dict
virtual_disk_raw_disk_ver2_backing_info_dict = virtual_disk_raw_disk_ver2_backing_info_instance.to_dict()
# create an instance of VirtualDiskRawDiskVer2BackingInfo from a dict
virtual_disk_raw_disk_ver2_backing_info_form_dict = virtual_disk_raw_disk_ver2_backing_info.from_dict(virtual_disk_raw_disk_ver2_backing_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


