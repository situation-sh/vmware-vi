# ArrayOfInvalidType

A boxed array of *InvalidType*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[InvalidType]**](InvalidType.md) |  | 

## Example

```python
from vmware_vi.models.array_of_invalid_type import ArrayOfInvalidType

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfInvalidType from a JSON string
array_of_invalid_type_instance = ArrayOfInvalidType.from_json(json)
# print the JSON string representation of the object
print ArrayOfInvalidType.to_json()

# convert the object into a dict
array_of_invalid_type_dict = array_of_invalid_type_instance.to_dict()
# create an instance of ArrayOfInvalidType from a dict
array_of_invalid_type_form_dict = array_of_invalid_type.from_dict(array_of_invalid_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


