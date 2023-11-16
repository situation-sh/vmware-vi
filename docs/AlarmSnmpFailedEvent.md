# AlarmSnmpFailedEvent

This event records a failure to complete an alarm SNMP notification. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entity** | [**ManagedEntityEventArgument**](ManagedEntityEventArgument.md) |  | 
**reason** | [**MethodFault**](MethodFault.md) |  | 

## Example

```python
from vmware_vi.models.alarm_snmp_failed_event import AlarmSnmpFailedEvent

# TODO update the JSON string below
json = "{}"
# create an instance of AlarmSnmpFailedEvent from a JSON string
alarm_snmp_failed_event_instance = AlarmSnmpFailedEvent.from_json(json)
# print the JSON string representation of the object
print AlarmSnmpFailedEvent.to_json()

# convert the object into a dict
alarm_snmp_failed_event_dict = alarm_snmp_failed_event_instance.to_dict()
# create an instance of AlarmSnmpFailedEvent from a dict
alarm_snmp_failed_event_form_dict = alarm_snmp_failed_event.from_dict(alarm_snmp_failed_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


