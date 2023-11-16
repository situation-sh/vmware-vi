# ArrayOfResourcePoolSummary

A boxed array of *ResourcePoolSummary*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[ResourcePoolSummary]**](ResourcePoolSummary.md) |  | 

## Example

```python
from vmware_vi.models.array_of_resource_pool_summary import ArrayOfResourcePoolSummary

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfResourcePoolSummary from a JSON string
array_of_resource_pool_summary_instance = ArrayOfResourcePoolSummary.from_json(json)
# print the JSON string representation of the object
print ArrayOfResourcePoolSummary.to_json()

# convert the object into a dict
array_of_resource_pool_summary_dict = array_of_resource_pool_summary_instance.to_dict()
# create an instance of ArrayOfResourcePoolSummary from a dict
array_of_resource_pool_summary_form_dict = array_of_resource_pool_summary.from_dict(array_of_resource_pool_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


