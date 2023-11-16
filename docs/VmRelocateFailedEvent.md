# VmRelocateFailedEvent

This event records a failure to relocate a virtual machine. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dest_host** | [**HostEventArgument**](HostEventArgument.md) |  | 
**reason** | [**MethodFault**](MethodFault.md) |  | 
**dest_datacenter** | [**DatacenterEventArgument**](DatacenterEventArgument.md) |  | [optional] 
**dest_datastore** | [**DatastoreEventArgument**](DatastoreEventArgument.md) |  | [optional] 

## Example

```python
from vmware_vi.models.vm_relocate_failed_event import VmRelocateFailedEvent

# TODO update the JSON string below
json = "{}"
# create an instance of VmRelocateFailedEvent from a JSON string
vm_relocate_failed_event_instance = VmRelocateFailedEvent.from_json(json)
# print the JSON string representation of the object
print VmRelocateFailedEvent.to_json()

# convert the object into a dict
vm_relocate_failed_event_dict = vm_relocate_failed_event_instance.to_dict()
# create an instance of VmRelocateFailedEvent from a dict
vm_relocate_failed_event_form_dict = vm_relocate_failed_event.from_dict(vm_relocate_failed_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


