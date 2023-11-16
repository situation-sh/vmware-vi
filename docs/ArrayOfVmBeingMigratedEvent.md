# ArrayOfVmBeingMigratedEvent

A boxed array of *VmBeingMigratedEvent*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[VmBeingMigratedEvent]**](VmBeingMigratedEvent.md) |  | 

## Example

```python
from vmware_vi.models.array_of_vm_being_migrated_event import ArrayOfVmBeingMigratedEvent

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfVmBeingMigratedEvent from a JSON string
array_of_vm_being_migrated_event_instance = ArrayOfVmBeingMigratedEvent.from_json(json)
# print the JSON string representation of the object
print ArrayOfVmBeingMigratedEvent.to_json()

# convert the object into a dict
array_of_vm_being_migrated_event_dict = array_of_vm_being_migrated_event_instance.to_dict()
# create an instance of ArrayOfVmBeingMigratedEvent from a dict
array_of_vm_being_migrated_event_form_dict = array_of_vm_being_migrated_event.from_dict(array_of_vm_being_migrated_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


