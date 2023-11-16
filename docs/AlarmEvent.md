# AlarmEvent

This event is an alarm events. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alarm** | [**AlarmEventArgument**](AlarmEventArgument.md) |  | 

## Example

```python
from vmware_vi.models.alarm_event import AlarmEvent

# TODO update the JSON string below
json = "{}"
# create an instance of AlarmEvent from a JSON string
alarm_event_instance = AlarmEvent.from_json(json)
# print the JSON string representation of the object
print AlarmEvent.to_json()

# convert the object into a dict
alarm_event_dict = alarm_event_instance.to_dict()
# create an instance of AlarmEvent from a dict
alarm_event_form_dict = alarm_event.from_dict(alarm_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


