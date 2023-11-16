# ArrayOfOutOfBounds

A boxed array of *OutOfBounds*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[OutOfBounds]**](OutOfBounds.md) |  | 

## Example

```python
from vmware_vi.models.array_of_out_of_bounds import ArrayOfOutOfBounds

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfOutOfBounds from a JSON string
array_of_out_of_bounds_instance = ArrayOfOutOfBounds.from_json(json)
# print the JSON string representation of the object
print ArrayOfOutOfBounds.to_json()

# convert the object into a dict
array_of_out_of_bounds_dict = array_of_out_of_bounds_instance.to_dict()
# create an instance of ArrayOfOutOfBounds from a dict
array_of_out_of_bounds_form_dict = array_of_out_of_bounds.from_dict(array_of_out_of_bounds_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


