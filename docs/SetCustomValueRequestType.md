# SetCustomValueRequestType

The parameters of *ExtensibleManagedObject.setCustomValue*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | The name of the field whose value is to be updated.  | 
**value** | **str** | Value to be assigned to the custom field.  | 

## Example

```python
from vmware_vi.models.set_custom_value_request_type import SetCustomValueRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of SetCustomValueRequestType from a JSON string
set_custom_value_request_type_instance = SetCustomValueRequestType.from_json(json)
# print the JSON string representation of the object
print SetCustomValueRequestType.to_json()

# convert the object into a dict
set_custom_value_request_type_dict = set_custom_value_request_type_instance.to_dict()
# create an instance of SetCustomValueRequestType from a dict
set_custom_value_request_type_form_dict = set_custom_value_request_type.from_dict(set_custom_value_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


