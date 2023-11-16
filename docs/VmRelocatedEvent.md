# VmRelocatedEvent

This event records the completion of a virtual machine relocation. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source_host** | [**HostEventArgument**](HostEventArgument.md) |  | 
**source_datacenter** | [**DatacenterEventArgument**](DatacenterEventArgument.md) |  | [optional] 
**source_datastore** | [**DatastoreEventArgument**](DatastoreEventArgument.md) |  | [optional] 

## Example

```python
from vmware_vi.models.vm_relocated_event import VmRelocatedEvent

# TODO update the JSON string below
json = "{}"
# create an instance of VmRelocatedEvent from a JSON string
vm_relocated_event_instance = VmRelocatedEvent.from_json(json)
# print the JSON string representation of the object
print VmRelocatedEvent.to_json()

# convert the object into a dict
vm_relocated_event_dict = vm_relocated_event_instance.to_dict()
# create an instance of VmRelocatedEvent from a dict
vm_relocated_event_form_dict = vm_relocated_event.from_dict(vm_relocated_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


