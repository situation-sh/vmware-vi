# ArrayOfHostSystemResourceInfo

A boxed array of *HostSystemResourceInfo*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[HostSystemResourceInfo]**](HostSystemResourceInfo.md) |  | 

## Example

```python
from vmware_vi.models.array_of_host_system_resource_info import ArrayOfHostSystemResourceInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfHostSystemResourceInfo from a JSON string
array_of_host_system_resource_info_instance = ArrayOfHostSystemResourceInfo.from_json(json)
# print the JSON string representation of the object
print ArrayOfHostSystemResourceInfo.to_json()

# convert the object into a dict
array_of_host_system_resource_info_dict = array_of_host_system_resource_info_instance.to_dict()
# create an instance of ArrayOfHostSystemResourceInfo from a dict
array_of_host_system_resource_info_form_dict = array_of_host_system_resource_info.from_dict(array_of_host_system_resource_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


