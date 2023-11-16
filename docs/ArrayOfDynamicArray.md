# ArrayOfDynamicArray

A boxed array of *DynamicArray*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[DynamicArray]**](DynamicArray.md) |  | 

## Example

```python
from vmware_vi.models.array_of_dynamic_array import ArrayOfDynamicArray

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfDynamicArray from a JSON string
array_of_dynamic_array_instance = ArrayOfDynamicArray.from_json(json)
# print the JSON string representation of the object
print ArrayOfDynamicArray.to_json()

# convert the object into a dict
array_of_dynamic_array_dict = array_of_dynamic_array_instance.to_dict()
# create an instance of ArrayOfDynamicArray from a dict
array_of_dynamic_array_form_dict = array_of_dynamic_array.from_dict(array_of_dynamic_array_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


