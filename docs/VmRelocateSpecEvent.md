# VmRelocateSpecEvent

This event is the base event for relocate and clone base events. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.vm_relocate_spec_event import VmRelocateSpecEvent

# TODO update the JSON string below
json = "{}"
# create an instance of VmRelocateSpecEvent from a JSON string
vm_relocate_spec_event_instance = VmRelocateSpecEvent.from_json(json)
# print the JSON string representation of the object
print VmRelocateSpecEvent.to_json()

# convert the object into a dict
vm_relocate_spec_event_dict = vm_relocate_spec_event_instance.to_dict()
# create an instance of VmRelocateSpecEvent from a dict
vm_relocate_spec_event_form_dict = vm_relocate_spec_event.from_dict(vm_relocate_spec_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


