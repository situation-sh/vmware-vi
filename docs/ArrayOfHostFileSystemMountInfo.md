# ArrayOfHostFileSystemMountInfo

A boxed array of *HostFileSystemMountInfo*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[HostFileSystemMountInfo]**](HostFileSystemMountInfo.md) |  | 

## Example

```python
from vmware_vi.models.array_of_host_file_system_mount_info import ArrayOfHostFileSystemMountInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfHostFileSystemMountInfo from a JSON string
array_of_host_file_system_mount_info_instance = ArrayOfHostFileSystemMountInfo.from_json(json)
# print the JSON string representation of the object
print ArrayOfHostFileSystemMountInfo.to_json()

# convert the object into a dict
array_of_host_file_system_mount_info_dict = array_of_host_file_system_mount_info_instance.to_dict()
# create an instance of ArrayOfHostFileSystemMountInfo from a dict
array_of_host_file_system_mount_info_form_dict = array_of_host_file_system_mount_info.from_dict(array_of_host_file_system_mount_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


