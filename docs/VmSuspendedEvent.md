# VmSuspendedEvent

This event records when a virtual machine finished suspending. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.vm_suspended_event import VmSuspendedEvent

# TODO update the JSON string below
json = "{}"
# create an instance of VmSuspendedEvent from a JSON string
vm_suspended_event_instance = VmSuspendedEvent.from_json(json)
# print the JSON string representation of the object
print VmSuspendedEvent.to_json()

# convert the object into a dict
vm_suspended_event_dict = vm_suspended_event_instance.to_dict()
# create an instance of VmSuspendedEvent from a dict
vm_suspended_event_form_dict = vm_suspended_event.from_dict(vm_suspended_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


