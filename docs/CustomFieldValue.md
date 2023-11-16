# CustomFieldValue

Base type for storing values. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **int** | The ID of the field to which this value belongs.  | 

## Example

```python
from vmware_vi.models.custom_field_value import CustomFieldValue

# TODO update the JSON string below
json = "{}"
# create an instance of CustomFieldValue from a JSON string
custom_field_value_instance = CustomFieldValue.from_json(json)
# print the JSON string representation of the object
print CustomFieldValue.to_json()

# convert the object into a dict
custom_field_value_dict = custom_field_value_instance.to_dict()
# create an instance of CustomFieldValue from a dict
custom_field_value_form_dict = custom_field_value.from_dict(custom_field_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


