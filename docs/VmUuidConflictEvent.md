# VmUuidConflictEvent

This event records a conflict of virtual machine BIOS UUIDs. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**conflicted_vm** | [**VmEventArgument**](VmEventArgument.md) |  | 
**uuid** | **str** | The BIOS UUID in conflict.  | 

## Example

```python
from vmware_vi.models.vm_uuid_conflict_event import VmUuidConflictEvent

# TODO update the JSON string below
json = "{}"
# create an instance of VmUuidConflictEvent from a JSON string
vm_uuid_conflict_event_instance = VmUuidConflictEvent.from_json(json)
# print the JSON string representation of the object
print VmUuidConflictEvent.to_json()

# convert the object into a dict
vm_uuid_conflict_event_dict = vm_uuid_conflict_event_instance.to_dict()
# create an instance of VmUuidConflictEvent from a dict
vm_uuid_conflict_event_form_dict = vm_uuid_conflict_event.from_dict(vm_uuid_conflict_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


