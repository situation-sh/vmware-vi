# VmAutoRenameEvent

This event records that a virtual machine was automatically renamed because of a name conflict. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**old_name** | **str** | The name of the virtual machine before renaming.  | 
**new_name** | **str** | The name of the virtual machine after renaming.  | 

## Example

```python
from vmware_vi.models.vm_auto_rename_event import VmAutoRenameEvent

# TODO update the JSON string below
json = "{}"
# create an instance of VmAutoRenameEvent from a JSON string
vm_auto_rename_event_instance = VmAutoRenameEvent.from_json(json)
# print the JSON string representation of the object
print VmAutoRenameEvent.to_json()

# convert the object into a dict
vm_auto_rename_event_dict = vm_auto_rename_event_instance.to_dict()
# create an instance of VmAutoRenameEvent from a dict
vm_auto_rename_event_form_dict = vm_auto_rename_event.from_dict(vm_auto_rename_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


