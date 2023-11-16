# VmFailedToResetEvent

This event records a failure to reset a virtual machine. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reason** | [**MethodFault**](MethodFault.md) |  | 

## Example

```python
from vmware_vi.models.vm_failed_to_reset_event import VmFailedToResetEvent

# TODO update the JSON string below
json = "{}"
# create an instance of VmFailedToResetEvent from a JSON string
vm_failed_to_reset_event_instance = VmFailedToResetEvent.from_json(json)
# print the JSON string representation of the object
print VmFailedToResetEvent.to_json()

# convert the object into a dict
vm_failed_to_reset_event_dict = vm_failed_to_reset_event_instance.to_dict()
# create an instance of VmFailedToResetEvent from a dict
vm_failed_to_reset_event_form_dict = vm_failed_to_reset_event.from_dict(vm_failed_to_reset_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


