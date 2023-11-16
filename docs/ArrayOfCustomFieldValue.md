# ArrayOfCustomFieldValue

A boxed array of *CustomFieldValue*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[CustomFieldValue]**](CustomFieldValue.md) |  | 

## Example

```python
from vmware_vi.models.array_of_custom_field_value import ArrayOfCustomFieldValue

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfCustomFieldValue from a JSON string
array_of_custom_field_value_instance = ArrayOfCustomFieldValue.from_json(json)
# print the JSON string representation of the object
print ArrayOfCustomFieldValue.to_json()

# convert the object into a dict
array_of_custom_field_value_dict = array_of_custom_field_value_instance.to_dict()
# create an instance of ArrayOfCustomFieldValue from a dict
array_of_custom_field_value_form_dict = array_of_custom_field_value.from_dict(array_of_custom_field_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

