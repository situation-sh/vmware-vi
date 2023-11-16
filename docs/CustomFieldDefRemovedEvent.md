# CustomFieldDefRemovedEvent

This event records the removal of a custom field definition. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.custom_field_def_removed_event import CustomFieldDefRemovedEvent

# TODO update the JSON string below
json = "{}"
# create an instance of CustomFieldDefRemovedEvent from a JSON string
custom_field_def_removed_event_instance = CustomFieldDefRemovedEvent.from_json(json)
# print the JSON string representation of the object
print CustomFieldDefRemovedEvent.to_json()

# convert the object into a dict
custom_field_def_removed_event_dict = custom_field_def_removed_event_instance.to_dict()
# create an instance of CustomFieldDefRemovedEvent from a dict
custom_field_def_removed_event_form_dict = custom_field_def_removed_event.from_dict(custom_field_def_removed_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


