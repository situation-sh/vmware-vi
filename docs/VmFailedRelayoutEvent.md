# VmFailedRelayoutEvent

This event records a specific failure to relay out a virtual machine, such as a failure to access the disk. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reason** | [**MethodFault**](MethodFault.md) |  | 

## Example

```python
from vmware_vi.models.vm_failed_relayout_event import VmFailedRelayoutEvent

# TODO update the JSON string below
json = "{}"
# create an instance of VmFailedRelayoutEvent from a JSON string
vm_failed_relayout_event_instance = VmFailedRelayoutEvent.from_json(json)
# print the JSON string representation of the object
print VmFailedRelayoutEvent.to_json()

# convert the object into a dict
vm_failed_relayout_event_dict = vm_failed_relayout_event_instance.to_dict()
# create an instance of VmFailedRelayoutEvent from a dict
vm_failed_relayout_event_form_dict = vm_failed_relayout_event.from_dict(vm_failed_relayout_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


