# VmUuidAssignedEvent

This event records the assignment of a new BIOS UUID to a virtual machine. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **str** | The new BIOS UUID.  | 

## Example

```python
from vmware_vi.models.vm_uuid_assigned_event import VmUuidAssignedEvent

# TODO update the JSON string below
json = "{}"
# create an instance of VmUuidAssignedEvent from a JSON string
vm_uuid_assigned_event_instance = VmUuidAssignedEvent.from_json(json)
# print the JSON string representation of the object
print VmUuidAssignedEvent.to_json()

# convert the object into a dict
vm_uuid_assigned_event_dict = vm_uuid_assigned_event_instance.to_dict()
# create an instance of VmUuidAssignedEvent from a dict
vm_uuid_assigned_event_form_dict = vm_uuid_assigned_event.from_dict(vm_uuid_assigned_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


