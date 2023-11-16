# AlarmScriptCompleteEvent

This event records the completion of an alarm-triggered script. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entity** | [**ManagedEntityEventArgument**](ManagedEntityEventArgument.md) |  | 
**script** | **str** | The script triggered by the alarm.  | 

## Example

```python
from vmware_vi.models.alarm_script_complete_event import AlarmScriptCompleteEvent

# TODO update the JSON string below
json = "{}"
# create an instance of AlarmScriptCompleteEvent from a JSON string
alarm_script_complete_event_instance = AlarmScriptCompleteEvent.from_json(json)
# print the JSON string representation of the object
print AlarmScriptCompleteEvent.to_json()

# convert the object into a dict
alarm_script_complete_event_dict = alarm_script_complete_event_instance.to_dict()
# create an instance of AlarmScriptCompleteEvent from a dict
alarm_script_complete_event_form_dict = alarm_script_complete_event.from_dict(alarm_script_complete_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


