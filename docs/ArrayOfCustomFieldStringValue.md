# ArrayOfCustomFieldStringValue

A boxed array of *CustomFieldStringValue*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[CustomFieldStringValue]**](CustomFieldStringValue.md) |  | 

## Example

```python
from vmware_vi.models.array_of_custom_field_string_value import ArrayOfCustomFieldStringValue

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfCustomFieldStringValue from a JSON string
array_of_custom_field_string_value_instance = ArrayOfCustomFieldStringValue.from_json(json)
# print the JSON string representation of the object
print ArrayOfCustomFieldStringValue.to_json()

# convert the object into a dict
array_of_custom_field_string_value_dict = array_of_custom_field_string_value_instance.to_dict()
# create an instance of ArrayOfCustomFieldStringValue from a dict
array_of_custom_field_string_value_form_dict = array_of_custom_field_string_value.from_dict(array_of_custom_field_string_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


