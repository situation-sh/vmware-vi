# ArrayOfVmUuidAssignedEvent

A boxed array of *VmUuidAssignedEvent*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[VmUuidAssignedEvent]**](VmUuidAssignedEvent.md) |  | 

## Example

```python
from vmware_vi.models.array_of_vm_uuid_assigned_event import ArrayOfVmUuidAssignedEvent

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfVmUuidAssignedEvent from a JSON string
array_of_vm_uuid_assigned_event_instance = ArrayOfVmUuidAssignedEvent.from_json(json)
# print the JSON string representation of the object
print ArrayOfVmUuidAssignedEvent.to_json()

# convert the object into a dict
array_of_vm_uuid_assigned_event_dict = array_of_vm_uuid_assigned_event_instance.to_dict()
# create an instance of ArrayOfVmUuidAssignedEvent from a dict
array_of_vm_uuid_assigned_event_form_dict = array_of_vm_uuid_assigned_event.from_dict(array_of_vm_uuid_assigned_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


