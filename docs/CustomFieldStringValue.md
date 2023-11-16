# CustomFieldStringValue

Subtype for string values (currently the only supported type). 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **str** | Value assigned to the custom field.  | 

## Example

```python
from vmware_vi.models.custom_field_string_value import CustomFieldStringValue

# TODO update the JSON string below
json = "{}"
# create an instance of CustomFieldStringValue from a JSON string
custom_field_string_value_instance = CustomFieldStringValue.from_json(json)
# print the JSON string representation of the object
print CustomFieldStringValue.to_json()

# convert the object into a dict
custom_field_string_value_dict = custom_field_string_value_instance.to_dict()
# create an instance of CustomFieldStringValue from a dict
custom_field_string_value_form_dict = custom_field_string_value.from_dict(custom_field_string_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


