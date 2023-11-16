# ArrayOfAlarmEmailFailedEvent

A boxed array of *AlarmEmailFailedEvent*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[AlarmEmailFailedEvent]**](AlarmEmailFailedEvent.md) |  | 

## Example

```python
from vmware_vi.models.array_of_alarm_email_failed_event import ArrayOfAlarmEmailFailedEvent

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfAlarmEmailFailedEvent from a JSON string
array_of_alarm_email_failed_event_instance = ArrayOfAlarmEmailFailedEvent.from_json(json)
# print the JSON string representation of the object
print ArrayOfAlarmEmailFailedEvent.to_json()

# convert the object into a dict
array_of_alarm_email_failed_event_dict = array_of_alarm_email_failed_event_instance.to_dict()
# create an instance of ArrayOfAlarmEmailFailedEvent from a dict
array_of_alarm_email_failed_event_form_dict = array_of_alarm_email_failed_event.from_dict(array_of_alarm_email_failed_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


