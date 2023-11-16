# CustomFieldDefAddedEvent

This event records the addition of a custom field definition. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.custom_field_def_added_event import CustomFieldDefAddedEvent

# TODO update the JSON string below
json = "{}"
# create an instance of CustomFieldDefAddedEvent from a JSON string
custom_field_def_added_event_instance = CustomFieldDefAddedEvent.from_json(json)
# print the JSON string representation of the object
print CustomFieldDefAddedEvent.to_json()

# convert the object into a dict
custom_field_def_added_event_dict = custom_field_def_added_event_instance.to_dict()
# create an instance of CustomFieldDefAddedEvent from a dict
custom_field_def_added_event_form_dict = custom_field_def_added_event.from_dict(custom_field_def_added_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


