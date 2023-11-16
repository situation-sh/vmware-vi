# AlarmActionTriggeredEvent

This event records that an alarm was triggered. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source** | [**ManagedEntityEventArgument**](ManagedEntityEventArgument.md) |  | 
**entity** | [**ManagedEntityEventArgument**](ManagedEntityEventArgument.md) |  | 

## Example

```python
from vmware_vi.models.alarm_action_triggered_event import AlarmActionTriggeredEvent

# TODO update the JSON string below
json = "{}"
# create an instance of AlarmActionTriggeredEvent from a JSON string
alarm_action_triggered_event_instance = AlarmActionTriggeredEvent.from_json(json)
# print the JSON string representation of the object
print AlarmActionTriggeredEvent.to_json()

# convert the object into a dict
alarm_action_triggered_event_dict = alarm_action_triggered_event_instance.to_dict()
# create an instance of AlarmActionTriggeredEvent from a dict
alarm_action_triggered_event_form_dict = alarm_action_triggered_event.from_dict(alarm_action_triggered_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


