# ArrayOfAlarmActionTriggeredEvent

A boxed array of *AlarmActionTriggeredEvent*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[AlarmActionTriggeredEvent]**](AlarmActionTriggeredEvent.md) |  | 

## Example

```python
from vmware_vi.models.array_of_alarm_action_triggered_event import ArrayOfAlarmActionTriggeredEvent

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfAlarmActionTriggeredEvent from a JSON string
array_of_alarm_action_triggered_event_instance = ArrayOfAlarmActionTriggeredEvent.from_json(json)
# print the JSON string representation of the object
print ArrayOfAlarmActionTriggeredEvent.to_json()

# convert the object into a dict
array_of_alarm_action_triggered_event_dict = array_of_alarm_action_triggered_event_instance.to_dict()
# create an instance of ArrayOfAlarmActionTriggeredEvent from a dict
array_of_alarm_action_triggered_event_form_dict = array_of_alarm_action_triggered_event.from_dict(array_of_alarm_action_triggered_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


