# ArrayOfAnyType

A boxed array of *Any*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[Any]**](Any.md) |  | 

## Example

```python
from vmware_vi.models.array_of_any_type import ArrayOfAnyType

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfAnyType from a JSON string
array_of_any_type_instance = ArrayOfAnyType.from_json(json)
# print the JSON string representation of the object
print ArrayOfAnyType.to_json()

# convert the object into a dict
array_of_any_type_dict = array_of_any_type_instance.to_dict()
# create an instance of ArrayOfAnyType from a dict
array_of_any_type_form_dict = array_of_any_type.from_dict(array_of_any_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


