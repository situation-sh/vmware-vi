# ArrayOfResourcePoolResourceUsage

A boxed array of *ResourcePoolResourceUsage*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[ResourcePoolResourceUsage]**](ResourcePoolResourceUsage.md) |  | 

## Example

```python
from vmware_vi.models.array_of_resource_pool_resource_usage import ArrayOfResourcePoolResourceUsage

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfResourcePoolResourceUsage from a JSON string
array_of_resource_pool_resource_usage_instance = ArrayOfResourcePoolResourceUsage.from_json(json)
# print the JSON string representation of the object
print ArrayOfResourcePoolResourceUsage.to_json()

# convert the object into a dict
array_of_resource_pool_resource_usage_dict = array_of_resource_pool_resource_usage_instance.to_dict()
# create an instance of ArrayOfResourcePoolResourceUsage from a dict
array_of_resource_pool_resource_usage_form_dict = array_of_resource_pool_resource_usage.from_dict(array_of_resource_pool_resource_usage_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


