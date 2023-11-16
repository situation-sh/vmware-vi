# ArrayOfVmFailedMigrateEvent

A boxed array of *VmFailedMigrateEvent*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[VmFailedMigrateEvent]**](VmFailedMigrateEvent.md) |  | 

## Example

```python
from vmware_vi.models.array_of_vm_failed_migrate_event import ArrayOfVmFailedMigrateEvent

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfVmFailedMigrateEvent from a JSON string
array_of_vm_failed_migrate_event_instance = ArrayOfVmFailedMigrateEvent.from_json(json)
# print the JSON string representation of the object
print ArrayOfVmFailedMigrateEvent.to_json()

# convert the object into a dict
array_of_vm_failed_migrate_event_dict = array_of_vm_failed_migrate_event_instance.to_dict()
# create an instance of ArrayOfVmFailedMigrateEvent from a dict
array_of_vm_failed_migrate_event_form_dict = array_of_vm_failed_migrate_event.from_dict(array_of_vm_failed_migrate_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


