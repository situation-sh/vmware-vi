# ArrayOfResourceAllocationOption

A boxed array of *ResourceAllocationOption*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[ResourceAllocationOption]**](ResourceAllocationOption.md) |  | 

## Example

```python
from vmware_vi.models.array_of_resource_allocation_option import ArrayOfResourceAllocationOption

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfResourceAllocationOption from a JSON string
array_of_resource_allocation_option_instance = ArrayOfResourceAllocationOption.from_json(json)
# print the JSON string representation of the object
print ArrayOfResourceAllocationOption.to_json()

# convert the object into a dict
array_of_resource_allocation_option_dict = array_of_resource_allocation_option_instance.to_dict()
# create an instance of ArrayOfResourceAllocationOption from a dict
array_of_resource_allocation_option_form_dict = array_of_resource_allocation_option.from_dict(array_of_resource_allocation_option_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


