# VmCloneFailedEvent

This event records a failure to clone a virtual machine. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dest_folder** | [**FolderEventArgument**](FolderEventArgument.md) |  | 
**dest_name** | **str** | The name of the destination virtual machine.  | 
**dest_host** | [**HostEventArgument**](HostEventArgument.md) |  | 
**reason** | [**MethodFault**](MethodFault.md) |  | 

## Example

```python
from vmware_vi.models.vm_clone_failed_event import VmCloneFailedEvent

# TODO update the JSON string below
json = "{}"
# create an instance of VmCloneFailedEvent from a JSON string
vm_clone_failed_event_instance = VmCloneFailedEvent.from_json(json)
# print the JSON string representation of the object
print VmCloneFailedEvent.to_json()

# convert the object into a dict
vm_clone_failed_event_dict = vm_clone_failed_event_instance.to_dict()
# create an instance of VmCloneFailedEvent from a dict
vm_clone_failed_event_form_dict = vm_clone_failed_event.from_dict(vm_clone_failed_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


