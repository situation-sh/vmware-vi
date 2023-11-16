# VmMigratedEvent

This event records a virtual machine migration. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source_host** | [**HostEventArgument**](HostEventArgument.md) |  | 
**source_datacenter** | [**DatacenterEventArgument**](DatacenterEventArgument.md) |  | [optional] 
**source_datastore** | [**DatastoreEventArgument**](DatastoreEventArgument.md) |  | [optional] 

## Example

```python
from vmware_vi.models.vm_migrated_event import VmMigratedEvent

# TODO update the JSON string below
json = "{}"
# create an instance of VmMigratedEvent from a JSON string
vm_migrated_event_instance = VmMigratedEvent.from_json(json)
# print the JSON string representation of the object
print VmMigratedEvent.to_json()

# convert the object into a dict
vm_migrated_event_dict = vm_migrated_event_instance.to_dict()
# create an instance of VmMigratedEvent from a dict
vm_migrated_event_form_dict = vm_migrated_event.from_dict(vm_migrated_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


