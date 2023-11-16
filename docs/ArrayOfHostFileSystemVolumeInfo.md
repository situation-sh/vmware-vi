# ArrayOfHostFileSystemVolumeInfo

A boxed array of *HostFileSystemVolumeInfo*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[HostFileSystemVolumeInfo]**](HostFileSystemVolumeInfo.md) |  | 

## Example

```python
from vmware_vi.models.array_of_host_file_system_volume_info import ArrayOfHostFileSystemVolumeInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfHostFileSystemVolumeInfo from a JSON string
array_of_host_file_system_volume_info_instance = ArrayOfHostFileSystemVolumeInfo.from_json(json)
# print the JSON string representation of the object
print ArrayOfHostFileSystemVolumeInfo.to_json()

# convert the object into a dict
array_of_host_file_system_volume_info_dict = array_of_host_file_system_volume_info_instance.to_dict()
# create an instance of ArrayOfHostFileSystemVolumeInfo from a dict
array_of_host_file_system_volume_info_form_dict = array_of_host_file_system_volume_info.from_dict(array_of_host_file_system_volume_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


