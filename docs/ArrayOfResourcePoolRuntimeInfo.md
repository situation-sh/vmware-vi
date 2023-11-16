# ArrayOfResourcePoolRuntimeInfo

A boxed array of *ResourcePoolRuntimeInfo*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[ResourcePoolRuntimeInfo]**](ResourcePoolRuntimeInfo.md) |  | 

## Example

```python
from vmware_vi.models.array_of_resource_pool_runtime_info import ArrayOfResourcePoolRuntimeInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfResourcePoolRuntimeInfo from a JSON string
array_of_resource_pool_runtime_info_instance = ArrayOfResourcePoolRuntimeInfo.from_json(json)
# print the JSON string representation of the object
print ArrayOfResourcePoolRuntimeInfo.to_json()

# convert the object into a dict
array_of_resource_pool_runtime_info_dict = array_of_resource_pool_runtime_info_instance.to_dict()
# create an instance of ArrayOfResourcePoolRuntimeInfo from a dict
array_of_resource_pool_runtime_info_form_dict = array_of_resource_pool_runtime_info.from_dict(array_of_resource_pool_runtime_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


