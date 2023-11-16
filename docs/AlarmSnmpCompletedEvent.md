# AlarmSnmpCompletedEvent

This event records the completion of an alarm SNMP notification. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entity** | [**ManagedEntityEventArgument**](ManagedEntityEventArgument.md) |  | 

## Example

```python
from vmware_vi.models.alarm_snmp_completed_event import AlarmSnmpCompletedEvent

# TODO update the JSON string below
json = "{}"
# create an instance of AlarmSnmpCompletedEvent from a JSON string
alarm_snmp_completed_event_instance = AlarmSnmpCompletedEvent.from_json(json)
# print the JSON string representation of the object
print AlarmSnmpCompletedEvent.to_json()

# convert the object into a dict
alarm_snmp_completed_event_dict = alarm_snmp_completed_event_instance.to_dict()
# create an instance of AlarmSnmpCompletedEvent from a dict
alarm_snmp_completed_event_form_dict = alarm_snmp_completed_event.from_dict(alarm_snmp_completed_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


