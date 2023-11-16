# VmFailedMigrateEvent

This event records a failure to migrate a virtual machine. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dest_host** | [**HostEventArgument**](HostEventArgument.md) |  | 
**reason** | [**MethodFault**](MethodFault.md) |  | 
**dest_datacenter** | [**DatacenterEventArgument**](DatacenterEventArgument.md) |  | [optional] 
**dest_datastore** | [**DatastoreEventArgument**](DatastoreEventArgument.md) |  | [optional] 

## Example

```python
from vmware_vi.models.vm_failed_migrate_event import VmFailedMigrateEvent

# TODO update the JSON string below
json = "{}"
# create an instance of VmFailedMigrateEvent from a JSON string
vm_failed_migrate_event_instance = VmFailedMigrateEvent.from_json(json)
# print the JSON string representation of the object
print VmFailedMigrateEvent.to_json()

# convert the object into a dict
vm_failed_migrate_event_dict = vm_failed_migrate_event_instance.to_dict()
# create an instance of VmFailedMigrateEvent from a dict
vm_failed_migrate_event_form_dict = vm_failed_migrate_event.from_dict(vm_failed_migrate_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


