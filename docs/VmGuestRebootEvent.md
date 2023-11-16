# VmGuestRebootEvent

This is a virtual machine guest reboot request event. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.vm_guest_reboot_event import VmGuestRebootEvent

# TODO update the JSON string below
json = "{}"
# create an instance of VmGuestRebootEvent from a JSON string
vm_guest_reboot_event_instance = VmGuestRebootEvent.from_json(json)
# print the JSON string representation of the object
print VmGuestRebootEvent.to_json()

# convert the object into a dict
vm_guest_reboot_event_dict = vm_guest_reboot_event_instance.to_dict()
# create an instance of VmGuestRebootEvent from a dict
vm_guest_reboot_event_form_dict = vm_guest_reboot_event.from_dict(vm_guest_reboot_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


