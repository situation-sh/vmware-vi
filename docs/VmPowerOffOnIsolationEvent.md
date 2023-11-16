# VmPowerOffOnIsolationEvent

This event records when a virtual machine has been powered off on an isolated host in a HA cluster. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**isolated_host** | [**HostEventArgument**](HostEventArgument.md) |  | 

## Example

```python
from vmware_vi.models.vm_power_off_on_isolation_event import VmPowerOffOnIsolationEvent

# TODO update the JSON string below
json = "{}"
# create an instance of VmPowerOffOnIsolationEvent from a JSON string
vm_power_off_on_isolation_event_instance = VmPowerOffOnIsolationEvent.from_json(json)
# print the JSON string representation of the object
print VmPowerOffOnIsolationEvent.to_json()

# convert the object into a dict
vm_power_off_on_isolation_event_dict = vm_power_off_on_isolation_event_instance.to_dict()
# create an instance of VmPowerOffOnIsolationEvent from a dict
vm_power_off_on_isolation_event_form_dict = vm_power_off_on_isolation_event.from_dict(vm_power_off_on_isolation_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


