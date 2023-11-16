# ArrayOfAlarmClearedEvent

A boxed array of *AlarmClearedEvent*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[AlarmClearedEvent]**](AlarmClearedEvent.md) |  | 

## Example

```python
from vmware_vi.models.array_of_alarm_cleared_event import ArrayOfAlarmClearedEvent

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfAlarmClearedEvent from a JSON string
array_of_alarm_cleared_event_instance = ArrayOfAlarmClearedEvent.from_json(json)
# print the JSON string representation of the object
print ArrayOfAlarmClearedEvent.to_json()

# convert the object into a dict
array_of_alarm_cleared_event_dict = array_of_alarm_cleared_event_instance.to_dict()
# create an instance of ArrayOfAlarmClearedEvent from a dict
array_of_alarm_cleared_event_form_dict = array_of_alarm_cleared_event.from_dict(array_of_alarm_cleared_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


