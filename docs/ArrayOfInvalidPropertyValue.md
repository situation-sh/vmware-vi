# ArrayOfInvalidPropertyValue

A boxed array of *InvalidPropertyValue*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[InvalidPropertyValue]**](InvalidPropertyValue.md) |  | 

## Example

```python
from vmware_vi.models.array_of_invalid_property_value import ArrayOfInvalidPropertyValue

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfInvalidPropertyValue from a JSON string
array_of_invalid_property_value_instance = ArrayOfInvalidPropertyValue.from_json(json)
# print the JSON string representation of the object
print ArrayOfInvalidPropertyValue.to_json()

# convert the object into a dict
array_of_invalid_property_value_dict = array_of_invalid_property_value_instance.to_dict()
# create an instance of ArrayOfInvalidPropertyValue from a dict
array_of_invalid_property_value_form_dict = array_of_invalid_property_value.from_dict(array_of_invalid_property_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


