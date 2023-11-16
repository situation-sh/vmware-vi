# VmInstanceUuidConflictEvent

This event records a conflict of virtual machine instance UUIDs.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**conflicted_vm** | [**VmEventArgument**](VmEventArgument.md) |  | 
**instance_uuid** | **str** | The instance UUID in conflict.  ***Since:*** vSphere API 4.0  | 

## Example

```python
from vmware_vi.models.vm_instance_uuid_conflict_event import VmInstanceUuidConflictEvent

# TODO update the JSON string below
json = "{}"
# create an instance of VmInstanceUuidConflictEvent from a JSON string
vm_instance_uuid_conflict_event_instance = VmInstanceUuidConflictEvent.from_json(json)
# print the JSON string representation of the object
print VmInstanceUuidConflictEvent.to_json()

# convert the object into a dict
vm_instance_uuid_conflict_event_dict = vm_instance_uuid_conflict_event_instance.to_dict()
# create an instance of VmInstanceUuidConflictEvent from a dict
vm_instance_uuid_conflict_event_form_dict = vm_instance_uuid_conflict_event.from_dict(vm_instance_uuid_conflict_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


