# VmRenamedEvent

This event records the renaming of a virtual machine. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**old_name** | **str** | The old name of the virtual machine.  | 
**new_name** | **str** | The new name of the virtual machine.  | 

## Example

```python
from vmware_vi.models.vm_renamed_event import VmRenamedEvent

# TODO update the JSON string below
json = "{}"
# create an instance of VmRenamedEvent from a JSON string
vm_renamed_event_instance = VmRenamedEvent.from_json(json)
# print the JSON string representation of the object
print VmRenamedEvent.to_json()

# convert the object into a dict
vm_renamed_event_dict = vm_renamed_event_instance.to_dict()
# create an instance of VmRenamedEvent from a dict
vm_renamed_event_form_dict = vm_renamed_event.from_dict(vm_renamed_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


