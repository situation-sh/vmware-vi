# ArrayOfVmAutoRenameEvent

A boxed array of *VmAutoRenameEvent*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[VmAutoRenameEvent]**](VmAutoRenameEvent.md) |  | 

## Example

```python
from vmware_vi.models.array_of_vm_auto_rename_event import ArrayOfVmAutoRenameEvent

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfVmAutoRenameEvent from a JSON string
array_of_vm_auto_rename_event_instance = ArrayOfVmAutoRenameEvent.from_json(json)
# print the JSON string representation of the object
print ArrayOfVmAutoRenameEvent.to_json()

# convert the object into a dict
array_of_vm_auto_rename_event_dict = array_of_vm_auto_rename_event_instance.to_dict()
# create an instance of ArrayOfVmAutoRenameEvent from a dict
array_of_vm_auto_rename_event_form_dict = array_of_vm_auto_rename_event.from_dict(array_of_vm_auto_rename_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


