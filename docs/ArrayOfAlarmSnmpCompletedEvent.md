# ArrayOfAlarmSnmpCompletedEvent

A boxed array of *AlarmSnmpCompletedEvent*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[AlarmSnmpCompletedEvent]**](AlarmSnmpCompletedEvent.md) |  | 

## Example

```python
from vmware_vi.models.array_of_alarm_snmp_completed_event import ArrayOfAlarmSnmpCompletedEvent

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfAlarmSnmpCompletedEvent from a JSON string
array_of_alarm_snmp_completed_event_instance = ArrayOfAlarmSnmpCompletedEvent.from_json(json)
# print the JSON string representation of the object
print ArrayOfAlarmSnmpCompletedEvent.to_json()

# convert the object into a dict
array_of_alarm_snmp_completed_event_dict = array_of_alarm_snmp_completed_event_instance.to_dict()
# create an instance of ArrayOfAlarmSnmpCompletedEvent from a dict
array_of_alarm_snmp_completed_event_form_dict = array_of_alarm_snmp_completed_event.from_dict(array_of_alarm_snmp_completed_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


