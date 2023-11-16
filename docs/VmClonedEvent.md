# VmClonedEvent

This event records the completion of a virtual machine cloning operation. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source_vm** | [**VmEventArgument**](VmEventArgument.md) |  | 

## Example

```python
from vmware_vi.models.vm_cloned_event import VmClonedEvent

# TODO update the JSON string below
json = "{}"
# create an instance of VmClonedEvent from a JSON string
vm_cloned_event_instance = VmClonedEvent.from_json(json)
# print the JSON string representation of the object
print VmClonedEvent.to_json()

# convert the object into a dict
vm_cloned_event_dict = vm_cloned_event_instance.to_dict()
# create an instance of VmClonedEvent from a dict
vm_cloned_event_form_dict = vm_cloned_event.from_dict(vm_cloned_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


