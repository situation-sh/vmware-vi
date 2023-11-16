# VmNoCompatibleHostForSecondaryEvent

This event records that no compatible host was found to place a secondary VM.  A default alarm will be triggered upon this event, which by default would trigger a SNMP trap.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.vm_no_compatible_host_for_secondary_event import VmNoCompatibleHostForSecondaryEvent

# TODO update the JSON string below
json = "{}"
# create an instance of VmNoCompatibleHostForSecondaryEvent from a JSON string
vm_no_compatible_host_for_secondary_event_instance = VmNoCompatibleHostForSecondaryEvent.from_json(json)
# print the JSON string representation of the object
print VmNoCompatibleHostForSecondaryEvent.to_json()

# convert the object into a dict
vm_no_compatible_host_for_secondary_event_dict = vm_no_compatible_host_for_secondary_event_instance.to_dict()
# create an instance of VmNoCompatibleHostForSecondaryEvent from a dict
vm_no_compatible_host_for_secondary_event_form_dict = vm_no_compatible_host_for_secondary_event.from_dict(vm_no_compatible_host_for_secondary_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


