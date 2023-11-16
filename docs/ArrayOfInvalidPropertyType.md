# ArrayOfInvalidPropertyType

A boxed array of *InvalidPropertyType*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[InvalidPropertyType]**](InvalidPropertyType.md) |  | 

## Example

```python
from vmware_vi.models.array_of_invalid_property_type import ArrayOfInvalidPropertyType

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfInvalidPropertyType from a JSON string
array_of_invalid_property_type_instance = ArrayOfInvalidPropertyType.from_json(json)
# print the JSON string representation of the object
print ArrayOfInvalidPropertyType.to_json()

# convert the object into a dict
array_of_invalid_property_type_dict = array_of_invalid_property_type_instance.to_dict()
# create an instance of ArrayOfInvalidPropertyType from a dict
array_of_invalid_property_type_form_dict = array_of_invalid_property_type.from_dict(array_of_invalid_property_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


