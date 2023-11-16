# ArrayOfAlarmEvent

A boxed array of *AlarmEvent*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[AlarmEvent]**](AlarmEvent.md) |  | 

## Example

```python
from vmware_vi.models.array_of_alarm_event import ArrayOfAlarmEvent

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfAlarmEvent from a JSON string
array_of_alarm_event_instance = ArrayOfAlarmEvent.from_json(json)
# print the JSON string representation of the object
print ArrayOfAlarmEvent.to_json()

# convert the object into a dict
array_of_alarm_event_dict = array_of_alarm_event_instance.to_dict()
# create an instance of ArrayOfAlarmEvent from a dict
array_of_alarm_event_form_dict = array_of_alarm_event.from_dict(array_of_alarm_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


