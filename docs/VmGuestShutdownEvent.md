# VmGuestShutdownEvent

This is a virtual machine guest shutdown request event. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.vm_guest_shutdown_event import VmGuestShutdownEvent

# TODO update the JSON string below
json = "{}"
# create an instance of VmGuestShutdownEvent from a JSON string
vm_guest_shutdown_event_instance = VmGuestShutdownEvent.from_json(json)
# print the JSON string representation of the object
print VmGuestShutdownEvent.to_json()

# convert the object into a dict
vm_guest_shutdown_event_dict = vm_guest_shutdown_event_instance.to_dict()
# create an instance of VmGuestShutdownEvent from a dict
vm_guest_shutdown_event_form_dict = vm_guest_shutdown_event.from_dict(vm_guest_shutdown_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


