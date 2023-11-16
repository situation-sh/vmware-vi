# CustomFieldDefEvent

This event records a custom field definition event. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**field_key** | **int** | The unique identifier of the custom field definition.  | 
**name** | **str** | The name of the custom field.  | 

## Example

```python
from vmware_vi.models.custom_field_def_event import CustomFieldDefEvent

# TODO update the JSON string below
json = "{}"
# create an instance of CustomFieldDefEvent from a JSON string
custom_field_def_event_instance = CustomFieldDefEvent.from_json(json)
# print the JSON string representation of the object
print CustomFieldDefEvent.to_json()

# convert the object into a dict
custom_field_def_event_dict = custom_field_def_event_instance.to_dict()
# create an instance of CustomFieldDefEvent from a dict
custom_field_def_event_form_dict = custom_field_def_event.from_dict(custom_field_def_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


