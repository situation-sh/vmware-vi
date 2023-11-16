# ArrayOfAlarmAcknowledgedEvent

A boxed array of *AlarmAcknowledgedEvent*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[AlarmAcknowledgedEvent]**](AlarmAcknowledgedEvent.md) |  | 

## Example

```python
from vmware_vi.models.array_of_alarm_acknowledged_event import ArrayOfAlarmAcknowledgedEvent

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfAlarmAcknowledgedEvent from a JSON string
array_of_alarm_acknowledged_event_instance = ArrayOfAlarmAcknowledgedEvent.from_json(json)
# print the JSON string representation of the object
print ArrayOfAlarmAcknowledgedEvent.to_json()

# convert the object into a dict
array_of_alarm_acknowledged_event_dict = array_of_alarm_acknowledged_event_instance.to_dict()
# create an instance of ArrayOfAlarmAcknowledgedEvent from a dict
array_of_alarm_acknowledged_event_form_dict = array_of_alarm_acknowledged_event.from_dict(array_of_alarm_acknowledged_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


