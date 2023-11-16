# ArrayOfHostActiveDirectoryInfo

A boxed array of *HostActiveDirectoryInfo*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[HostActiveDirectoryInfo]**](HostActiveDirectoryInfo.md) |  | 

## Example

```python
from vmware_vi.models.array_of_host_active_directory_info import ArrayOfHostActiveDirectoryInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfHostActiveDirectoryInfo from a JSON string
array_of_host_active_directory_info_instance = ArrayOfHostActiveDirectoryInfo.from_json(json)
# print the JSON string representation of the object
print ArrayOfHostActiveDirectoryInfo.to_json()

# convert the object into a dict
array_of_host_active_directory_info_dict = array_of_host_active_directory_info_instance.to_dict()
# create an instance of ArrayOfHostActiveDirectoryInfo from a dict
array_of_host_active_directory_info_form_dict = array_of_host_active_directory_info.from_dict(array_of_host_active_directory_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


