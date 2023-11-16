# HostFileSystemVolumeInfo

The *HostFileSystemVolumeInfo* data object describes the file system volume information for the host.  A file system volume refers to a storage abstraction that allows files to be created and organized. A host can have multiple file system volumes. File system volumes are typically mounted into a file namespace that allows all files in mounted file systems to be addressable from the host.  A file system volume is backed by disk storage. It could span one or more disks but need not use an entire disk.  A file system volume by definition must be mounted on the file system in order to exist. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**volume_type_list** | **List[str]** | The list of supported file system volume types.  | [optional] 
**mount_info** | [**List[HostFileSystemMountInfo]**](HostFileSystemMountInfo.md) | The list of file system volumes mounted on the host.  | [optional] 

## Example

```python
from vmware_vi.models.host_file_system_volume_info import HostFileSystemVolumeInfo

# TODO update the JSON string below
json = "{}"
# create an instance of HostFileSystemVolumeInfo from a JSON string
host_file_system_volume_info_instance = HostFileSystemVolumeInfo.from_json(json)
# print the JSON string representation of the object
print HostFileSystemVolumeInfo.to_json()

# convert the object into a dict
host_file_system_volume_info_dict = host_file_system_volume_info_instance.to_dict()
# create an instance of HostFileSystemVolumeInfo from a dict
host_file_system_volume_info_form_dict = host_file_system_volume_info.from_dict(host_file_system_volume_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


