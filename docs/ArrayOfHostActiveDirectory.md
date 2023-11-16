# ArrayOfHostActiveDirectory

A boxed array of *HostActiveDirectory*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[HostActiveDirectory]**](HostActiveDirectory.md) |  | 

## Example

```python
from vmware_vi.models.array_of_host_active_directory import ArrayOfHostActiveDirectory

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfHostActiveDirectory from a JSON string
array_of_host_active_directory_instance = ArrayOfHostActiveDirectory.from_json(json)
# print the JSON string representation of the object
print ArrayOfHostActiveDirectory.to_json()

# convert the object into a dict
array_of_host_active_directory_dict = array_of_host_active_directory_instance.to_dict()
# create an instance of ArrayOfHostActiveDirectory from a dict
array_of_host_active_directory_form_dict = array_of_host_active_directory.from_dict(array_of_host_active_directory_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


