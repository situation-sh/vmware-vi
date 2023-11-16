# VmBeingClonedEvent

This event records a virtual machine being cloned. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dest_folder** | [**FolderEventArgument**](FolderEventArgument.md) |  | 
**dest_name** | **str** | The name of the destination virtual machine.  | 
**dest_host** | [**HostEventArgument**](HostEventArgument.md) |  | 

## Example

```python
from vmware_vi.models.vm_being_cloned_event import VmBeingClonedEvent

# TODO update the JSON string below
json = "{}"
# create an instance of VmBeingClonedEvent from a JSON string
vm_being_cloned_event_instance = VmBeingClonedEvent.from_json(json)
# print the JSON string representation of the object
print VmBeingClonedEvent.to_json()

# convert the object into a dict
vm_being_cloned_event_dict = vm_being_cloned_event_instance.to_dict()
# create an instance of VmBeingClonedEvent from a dict
vm_being_cloned_event_form_dict = vm_being_cloned_event.from_dict(vm_being_cloned_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


