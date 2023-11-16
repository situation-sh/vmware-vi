# VmTimedoutStartingSecondaryEvent

This event records timeout when starting a secondary VM.  A default alarm will be triggered upon this event, which by default would trigger a SNMP trap.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**timeout** | **int** | The duration of the timeout in milliseconds.  ***Since:*** vSphere API 4.0  | [optional] 

## Example

```python
from vmware_vi.models.vm_timedout_starting_secondary_event import VmTimedoutStartingSecondaryEvent

# TODO update the JSON string below
json = "{}"
# create an instance of VmTimedoutStartingSecondaryEvent from a JSON string
vm_timedout_starting_secondary_event_instance = VmTimedoutStartingSecondaryEvent.from_json(json)
# print the JSON string representation of the object
print VmTimedoutStartingSecondaryEvent.to_json()

# convert the object into a dict
vm_timedout_starting_secondary_event_dict = vm_timedout_starting_secondary_event_instance.to_dict()
# create an instance of VmTimedoutStartingSecondaryEvent from a dict
vm_timedout_starting_secondary_event_form_dict = vm_timedout_starting_secondary_event.from_dict(vm_timedout_starting_secondary_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


