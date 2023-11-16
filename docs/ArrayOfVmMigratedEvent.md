# ArrayOfVmMigratedEvent

A boxed array of *VmMigratedEvent*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[VmMigratedEvent]**](VmMigratedEvent.md) |  | 

## Example

```python
from vmware_vi.models.array_of_vm_migrated_event import ArrayOfVmMigratedEvent

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfVmMigratedEvent from a JSON string
array_of_vm_migrated_event_instance = ArrayOfVmMigratedEvent.from_json(json)
# print the JSON string representation of the object
print ArrayOfVmMigratedEvent.to_json()

# convert the object into a dict
array_of_vm_migrated_event_dict = array_of_vm_migrated_event_instance.to_dict()
# create an instance of ArrayOfVmMigratedEvent from a dict
array_of_vm_migrated_event_form_dict = array_of_vm_migrated_event.from_dict(array_of_vm_migrated_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


