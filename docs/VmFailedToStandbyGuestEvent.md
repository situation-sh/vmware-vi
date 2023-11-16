# VmFailedToStandbyGuestEvent

This event records a failure to set the guest on a virtual machine to a standby state. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reason** | [**MethodFault**](MethodFault.md) |  | 

## Example

```python
from vmware_vi.models.vm_failed_to_standby_guest_event import VmFailedToStandbyGuestEvent

# TODO update the JSON string below
json = "{}"
# create an instance of VmFailedToStandbyGuestEvent from a JSON string
vm_failed_to_standby_guest_event_instance = VmFailedToStandbyGuestEvent.from_json(json)
# print the JSON string representation of the object
print VmFailedToStandbyGuestEvent.to_json()

# convert the object into a dict
vm_failed_to_standby_guest_event_dict = vm_failed_to_standby_guest_event_instance.to_dict()
# create an instance of VmFailedToStandbyGuestEvent from a dict
vm_failed_to_standby_guest_event_form_dict = vm_failed_to_standby_guest_event.from_dict(vm_failed_to_standby_guest_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


