# VmOrphanedEvent

This event records a virtual machine for which no host is responsible. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.vm_orphaned_event import VmOrphanedEvent

# TODO update the JSON string below
json = "{}"
# create an instance of VmOrphanedEvent from a JSON string
vm_orphaned_event_instance = VmOrphanedEvent.from_json(json)
# print the JSON string representation of the object
print VmOrphanedEvent.to_json()

# convert the object into a dict
vm_orphaned_event_dict = vm_orphaned_event_instance.to_dict()
# create an instance of VmOrphanedEvent from a dict
vm_orphaned_event_form_dict = vm_orphaned_event.from_dict(vm_orphaned_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


