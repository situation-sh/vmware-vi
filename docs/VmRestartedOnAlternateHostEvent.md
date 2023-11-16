# VmRestartedOnAlternateHostEvent

Deprecated as of vSphere API 5.0, the Server will generate the *EventEx* event with the *EventEx.eventTypeId* property set to \"com.vmware.vc.ha.VmRestartedByHAEvent\".  This event records that the virtual machine was restarted on a host, since its original host had failed. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source_host** | [**HostEventArgument**](HostEventArgument.md) |  | 

## Example

```python
from vmware_vi.models.vm_restarted_on_alternate_host_event import VmRestartedOnAlternateHostEvent

# TODO update the JSON string below
json = "{}"
# create an instance of VmRestartedOnAlternateHostEvent from a JSON string
vm_restarted_on_alternate_host_event_instance = VmRestartedOnAlternateHostEvent.from_json(json)
# print the JSON string representation of the object
print VmRestartedOnAlternateHostEvent.to_json()

# convert the object into a dict
vm_restarted_on_alternate_host_event_dict = vm_restarted_on_alternate_host_event_instance.to_dict()
# create an instance of VmRestartedOnAlternateHostEvent from a dict
vm_restarted_on_alternate_host_event_form_dict = vm_restarted_on_alternate_host_event.from_dict(vm_restarted_on_alternate_host_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


