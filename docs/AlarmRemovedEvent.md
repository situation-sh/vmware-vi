# AlarmRemovedEvent

This event records the removal of an alarm. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entity** | [**ManagedEntityEventArgument**](ManagedEntityEventArgument.md) |  | 

## Example

```python
from vmware_vi.models.alarm_removed_event import AlarmRemovedEvent

# TODO update the JSON string below
json = "{}"
# create an instance of AlarmRemovedEvent from a JSON string
alarm_removed_event_instance = AlarmRemovedEvent.from_json(json)
# print the JSON string representation of the object
print AlarmRemovedEvent.to_json()

# convert the object into a dict
alarm_removed_event_dict = alarm_removed_event_instance.to_dict()
# create an instance of AlarmRemovedEvent from a dict
alarm_removed_event_form_dict = alarm_removed_event.from_dict(alarm_removed_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


