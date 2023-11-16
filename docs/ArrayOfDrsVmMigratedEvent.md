# ArrayOfDrsVmMigratedEvent

A boxed array of *DrsVmMigratedEvent*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[DrsVmMigratedEvent]**](DrsVmMigratedEvent.md) |  | 

## Example

```python
from vmware_vi.models.array_of_drs_vm_migrated_event import ArrayOfDrsVmMigratedEvent

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfDrsVmMigratedEvent from a JSON string
array_of_drs_vm_migrated_event_instance = ArrayOfDrsVmMigratedEvent.from_json(json)
# print the JSON string representation of the object
print ArrayOfDrsVmMigratedEvent.to_json()

# convert the object into a dict
array_of_drs_vm_migrated_event_dict = array_of_drs_vm_migrated_event_instance.to_dict()
# create an instance of ArrayOfDrsVmMigratedEvent from a dict
array_of_drs_vm_migrated_event_form_dict = array_of_drs_vm_migrated_event.from_dict(array_of_drs_vm_migrated_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


