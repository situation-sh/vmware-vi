# VmBeingRelocatedEvent

This event records that a virtual machine is being relocated. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dest_host** | [**HostEventArgument**](HostEventArgument.md) |  | 
**dest_datacenter** | [**DatacenterEventArgument**](DatacenterEventArgument.md) |  | [optional] 
**dest_datastore** | [**DatastoreEventArgument**](DatastoreEventArgument.md) |  | [optional] 

## Example

```python
from vmware_vi.models.vm_being_relocated_event import VmBeingRelocatedEvent

# TODO update the JSON string below
json = "{}"
# create an instance of VmBeingRelocatedEvent from a JSON string
vm_being_relocated_event_instance = VmBeingRelocatedEvent.from_json(json)
# print the JSON string representation of the object
print VmBeingRelocatedEvent.to_json()

# convert the object into a dict
vm_being_relocated_event_dict = vm_being_relocated_event_instance.to_dict()
# create an instance of VmBeingRelocatedEvent from a dict
vm_being_relocated_event_form_dict = vm_being_relocated_event.from_dict(vm_being_relocated_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


