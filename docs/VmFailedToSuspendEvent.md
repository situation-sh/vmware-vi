# VmFailedToSuspendEvent

This event records a failure to suspend a virtual machine. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reason** | [**MethodFault**](MethodFault.md) |  | 

## Example

```python
from vmware_vi.models.vm_failed_to_suspend_event import VmFailedToSuspendEvent

# TODO update the JSON string below
json = "{}"
# create an instance of VmFailedToSuspendEvent from a JSON string
vm_failed_to_suspend_event_instance = VmFailedToSuspendEvent.from_json(json)
# print the JSON string representation of the object
print VmFailedToSuspendEvent.to_json()

# convert the object into a dict
vm_failed_to_suspend_event_dict = vm_failed_to_suspend_event_instance.to_dict()
# create an instance of VmFailedToSuspendEvent from a dict
vm_failed_to_suspend_event_form_dict = vm_failed_to_suspend_event.from_dict(vm_failed_to_suspend_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


