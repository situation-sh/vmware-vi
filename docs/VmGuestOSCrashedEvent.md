# VmGuestOSCrashedEvent

This event notifies that a guest OS has crashed  ***Since:*** vSphere API 6.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.vm_guest_os_crashed_event import VmGuestOSCrashedEvent

# TODO update the JSON string below
json = "{}"
# create an instance of VmGuestOSCrashedEvent from a JSON string
vm_guest_os_crashed_event_instance = VmGuestOSCrashedEvent.from_json(json)
# print the JSON string representation of the object
print VmGuestOSCrashedEvent.to_json()

# convert the object into a dict
vm_guest_os_crashed_event_dict = vm_guest_os_crashed_event_instance.to_dict()
# create an instance of VmGuestOSCrashedEvent from a dict
vm_guest_os_crashed_event_form_dict = vm_guest_os_crashed_event.from_dict(vm_guest_os_crashed_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


