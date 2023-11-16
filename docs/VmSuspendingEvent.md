# VmSuspendingEvent

This event records a virtual machine suspending. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.vm_suspending_event import VmSuspendingEvent

# TODO update the JSON string below
json = "{}"
# create an instance of VmSuspendingEvent from a JSON string
vm_suspending_event_instance = VmSuspendingEvent.from_json(json)
# print the JSON string representation of the object
print VmSuspendingEvent.to_json()

# convert the object into a dict
vm_suspending_event_dict = vm_suspending_event_instance.to_dict()
# create an instance of VmSuspendingEvent from a dict
vm_suspending_event_form_dict = vm_suspending_event.from_dict(vm_suspending_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


