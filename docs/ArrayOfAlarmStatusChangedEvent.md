# ArrayOfAlarmStatusChangedEvent

A boxed array of *AlarmStatusChangedEvent*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[AlarmStatusChangedEvent]**](AlarmStatusChangedEvent.md) |  | 

## Example

```python
from vmware_vi.models.array_of_alarm_status_changed_event import ArrayOfAlarmStatusChangedEvent

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfAlarmStatusChangedEvent from a JSON string
array_of_alarm_status_changed_event_instance = ArrayOfAlarmStatusChangedEvent.from_json(json)
# print the JSON string representation of the object
print ArrayOfAlarmStatusChangedEvent.to_json()

# convert the object into a dict
array_of_alarm_status_changed_event_dict = array_of_alarm_status_changed_event_instance.to_dict()
# create an instance of ArrayOfAlarmStatusChangedEvent from a dict
array_of_alarm_status_changed_event_form_dict = array_of_alarm_status_changed_event.from_dict(array_of_alarm_status_changed_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


