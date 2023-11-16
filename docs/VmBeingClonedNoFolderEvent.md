# VmBeingClonedNoFolderEvent

This event records a virtual machine being cloned.  ***Since:*** vSphere API 4.1 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dest_name** | **str** | The name of the destination virtual machine.  ***Since:*** vSphere API 4.1  | 
**dest_host** | [**HostEventArgument**](HostEventArgument.md) |  | 

## Example

```python
from vmware_vi.models.vm_being_cloned_no_folder_event import VmBeingClonedNoFolderEvent

# TODO update the JSON string below
json = "{}"
# create an instance of VmBeingClonedNoFolderEvent from a JSON string
vm_being_cloned_no_folder_event_instance = VmBeingClonedNoFolderEvent.from_json(json)
# print the JSON string representation of the object
print VmBeingClonedNoFolderEvent.to_json()

# convert the object into a dict
vm_being_cloned_no_folder_event_dict = vm_being_cloned_no_folder_event_instance.to_dict()
# create an instance of VmBeingClonedNoFolderEvent from a dict
vm_being_cloned_no_folder_event_form_dict = vm_being_cloned_no_folder_event.from_dict(vm_being_cloned_no_folder_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


