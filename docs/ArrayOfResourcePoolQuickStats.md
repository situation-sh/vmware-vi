# ArrayOfResourcePoolQuickStats

A boxed array of *ResourcePoolQuickStats*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[ResourcePoolQuickStats]**](ResourcePoolQuickStats.md) |  | 

## Example

```python
from vmware_vi.models.array_of_resource_pool_quick_stats import ArrayOfResourcePoolQuickStats

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfResourcePoolQuickStats from a JSON string
array_of_resource_pool_quick_stats_instance = ArrayOfResourcePoolQuickStats.from_json(json)
# print the JSON string representation of the object
print ArrayOfResourcePoolQuickStats.to_json()

# convert the object into a dict
array_of_resource_pool_quick_stats_dict = array_of_resource_pool_quick_stats_instance.to_dict()
# create an instance of ArrayOfResourcePoolQuickStats from a dict
array_of_resource_pool_quick_stats_form_dict = array_of_resource_pool_quick_stats.from_dict(array_of_resource_pool_quick_stats_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


