# VmBeingHotMigratedEvent

This event records that a virtual machine is being hot-migrated. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dest_host** | [**HostEventArgument**](HostEventArgument.md) |  | 
**dest_datacenter** | [**DatacenterEventArgument**](DatacenterEventArgument.md) |  | [optional] 
**dest_datastore** | [**DatastoreEventArgument**](DatastoreEventArgument.md) |  | [optional] 

## Example

```python
from vmware_vi.models.vm_being_hot_migrated_event import VmBeingHotMigratedEvent

# TODO update the JSON string below
json = "{}"
# create an instance of VmBeingHotMigratedEvent from a JSON string
vm_being_hot_migrated_event_instance = VmBeingHotMigratedEvent.from_json(json)
# print the JSON string representation of the object
print VmBeingHotMigratedEvent.to_json()

# convert the object into a dict
vm_being_hot_migrated_event_dict = vm_being_hot_migrated_event_instance.to_dict()
# create an instance of VmBeingHotMigratedEvent from a dict
vm_being_hot_migrated_event_form_dict = vm_being_hot_migrated_event.from_dict(vm_being_hot_migrated_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


