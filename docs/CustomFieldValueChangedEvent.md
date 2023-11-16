# CustomFieldValueChangedEvent

This event records a change to a custom field value for a particular entity. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entity** | [**ManagedEntityEventArgument**](ManagedEntityEventArgument.md) |  | 
**field_key** | **int** | The custom field whose value was changed for the entity.  | 
**name** | **str** | The name of the custom field at the time the value was changed.  | 
**value** | **str** | The new value that was set.  | 
**prev_state** | **str** | The previous service state.  ***Since:*** vSphere API 6.5  | [optional] 

## Example

```python
from vmware_vi.models.custom_field_value_changed_event import CustomFieldValueChangedEvent

# TODO update the JSON string below
json = "{}"
# create an instance of CustomFieldValueChangedEvent from a JSON string
custom_field_value_changed_event_instance = CustomFieldValueChangedEvent.from_json(json)
# print the JSON string representation of the object
print CustomFieldValueChangedEvent.to_json()

# convert the object into a dict
custom_field_value_changed_event_dict = custom_field_value_changed_event_instance.to_dict()
# create an instance of CustomFieldValueChangedEvent from a dict
custom_field_value_changed_event_form_dict = custom_field_value_changed_event.from_dict(custom_field_value_changed_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


