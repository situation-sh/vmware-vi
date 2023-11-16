# ArrayOfHostRuntimeInfo

A boxed array of *HostRuntimeInfo*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[HostRuntimeInfo]**](HostRuntimeInfo.md) |  | 

## Example

```python
from vmware_vi.models.array_of_host_runtime_info import ArrayOfHostRuntimeInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfHostRuntimeInfo from a JSON string
array_of_host_runtime_info_instance = ArrayOfHostRuntimeInfo.from_json(json)
# print the JSON string representation of the object
print ArrayOfHostRuntimeInfo.to_json()

# convert the object into a dict
array_of_host_runtime_info_dict = array_of_host_runtime_info_instance.to_dict()
# create an instance of ArrayOfHostRuntimeInfo from a dict
array_of_host_runtime_info_form_dict = array_of_host_runtime_info.from_dict(array_of_host_runtime_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


