# ArrayOfVmUuidConflictEvent

A boxed array of *VmUuidConflictEvent*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[VmUuidConflictEvent]**](VmUuidConflictEvent.md) |  | 

## Example

```python
from vmware_vi.models.array_of_vm_uuid_conflict_event import ArrayOfVmUuidConflictEvent

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfVmUuidConflictEvent from a JSON string
array_of_vm_uuid_conflict_event_instance = ArrayOfVmUuidConflictEvent.from_json(json)
# print the JSON string representation of the object
print ArrayOfVmUuidConflictEvent.to_json()

# convert the object into a dict
array_of_vm_uuid_conflict_event_dict = array_of_vm_uuid_conflict_event_instance.to_dict()
# create an instance of ArrayOfVmUuidConflictEvent from a dict
array_of_vm_uuid_conflict_event_form_dict = array_of_vm_uuid_conflict_event.from_dict(array_of_vm_uuid_conflict_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


