# ArrayOfVmInstanceUuidConflictEvent

A boxed array of *VmInstanceUuidConflictEvent*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[VmInstanceUuidConflictEvent]**](VmInstanceUuidConflictEvent.md) |  | 

## Example

```python
from vmware_vi.models.array_of_vm_instance_uuid_conflict_event import ArrayOfVmInstanceUuidConflictEvent

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfVmInstanceUuidConflictEvent from a JSON string
array_of_vm_instance_uuid_conflict_event_instance = ArrayOfVmInstanceUuidConflictEvent.from_json(json)
# print the JSON string representation of the object
print ArrayOfVmInstanceUuidConflictEvent.to_json()

# convert the object into a dict
array_of_vm_instance_uuid_conflict_event_dict = array_of_vm_instance_uuid_conflict_event_instance.to_dict()
# create an instance of ArrayOfVmInstanceUuidConflictEvent from a dict
array_of_vm_instance_uuid_conflict_event_form_dict = array_of_vm_instance_uuid_conflict_event.from_dict(array_of_vm_instance_uuid_conflict_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


