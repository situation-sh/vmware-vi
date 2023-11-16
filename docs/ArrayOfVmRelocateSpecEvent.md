# ArrayOfVmRelocateSpecEvent

A boxed array of *VmRelocateSpecEvent*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[VmRelocateSpecEvent]**](VmRelocateSpecEvent.md) |  | 

## Example

```python
from vmware_vi.models.array_of_vm_relocate_spec_event import ArrayOfVmRelocateSpecEvent

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfVmRelocateSpecEvent from a JSON string
array_of_vm_relocate_spec_event_instance = ArrayOfVmRelocateSpecEvent.from_json(json)
# print the JSON string representation of the object
print ArrayOfVmRelocateSpecEvent.to_json()

# convert the object into a dict
array_of_vm_relocate_spec_event_dict = array_of_vm_relocate_spec_event_instance.to_dict()
# create an instance of ArrayOfVmRelocateSpecEvent from a dict
array_of_vm_relocate_spec_event_form_dict = array_of_vm_relocate_spec_event.from_dict(array_of_vm_relocate_spec_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


