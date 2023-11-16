# ArrayOfAlarmScriptFailedEvent

A boxed array of *AlarmScriptFailedEvent*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[AlarmScriptFailedEvent]**](AlarmScriptFailedEvent.md) |  | 

## Example

```python
from vmware_vi.models.array_of_alarm_script_failed_event import ArrayOfAlarmScriptFailedEvent

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfAlarmScriptFailedEvent from a JSON string
array_of_alarm_script_failed_event_instance = ArrayOfAlarmScriptFailedEvent.from_json(json)
# print the JSON string representation of the object
print ArrayOfAlarmScriptFailedEvent.to_json()

# convert the object into a dict
array_of_alarm_script_failed_event_dict = array_of_alarm_script_failed_event_instance.to_dict()
# create an instance of ArrayOfAlarmScriptFailedEvent from a dict
array_of_alarm_script_failed_event_form_dict = array_of_alarm_script_failed_event.from_dict(array_of_alarm_script_failed_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


