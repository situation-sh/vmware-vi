# VmGuestStandbyEvent

This is a virtual machine guest standby request event. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.vm_guest_standby_event import VmGuestStandbyEvent

# TODO update the JSON string below
json = "{}"
# create an instance of VmGuestStandbyEvent from a JSON string
vm_guest_standby_event_instance = VmGuestStandbyEvent.from_json(json)
# print the JSON string representation of the object
print VmGuestStandbyEvent.to_json()

# convert the object into a dict
vm_guest_standby_event_dict = vm_guest_standby_event_instance.to_dict()
# create an instance of VmGuestStandbyEvent from a dict
vm_guest_standby_event_form_dict = vm_guest_standby_event.from_dict(vm_guest_standby_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


