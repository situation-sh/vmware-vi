# DrsVmMigratedEvent

This event records a virtual machine migration that was recommended by DRS. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.drs_vm_migrated_event import DrsVmMigratedEvent

# TODO update the JSON string below
json = "{}"
# create an instance of DrsVmMigratedEvent from a JSON string
drs_vm_migrated_event_instance = DrsVmMigratedEvent.from_json(json)
# print the JSON string representation of the object
print DrsVmMigratedEvent.to_json()

# convert the object into a dict
drs_vm_migrated_event_dict = drs_vm_migrated_event_instance.to_dict()
# create an instance of DrsVmMigratedEvent from a dict
drs_vm_migrated_event_form_dict = drs_vm_migrated_event.from_dict(drs_vm_migrated_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


