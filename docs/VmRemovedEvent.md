# VmRemovedEvent

This event records a virtual machine removed from VirtualCenter management. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.vm_removed_event import VmRemovedEvent

# TODO update the JSON string below
json = "{}"
# create an instance of VmRemovedEvent from a JSON string
vm_removed_event_instance = VmRemovedEvent.from_json(json)
# print the JSON string representation of the object
print VmRemovedEvent.to_json()

# convert the object into a dict
vm_removed_event_dict = vm_removed_event_instance.to_dict()
# create an instance of VmRemovedEvent from a dict
vm_removed_event_form_dict = vm_removed_event.from_dict(vm_removed_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


