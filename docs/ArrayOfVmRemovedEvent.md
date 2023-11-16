# ArrayOfVmRemovedEvent

A boxed array of *VmRemovedEvent*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[VmRemovedEvent]**](VmRemovedEvent.md) |  | 

## Example

```python
from vmware_vi.models.array_of_vm_removed_event import ArrayOfVmRemovedEvent

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfVmRemovedEvent from a JSON string
array_of_vm_removed_event_instance = ArrayOfVmRemovedEvent.from_json(json)
# print the JSON string representation of the object
print ArrayOfVmRemovedEvent.to_json()

# convert the object into a dict
array_of_vm_removed_event_dict = array_of_vm_removed_event_instance.to_dict()
# create an instance of ArrayOfVmRemovedEvent from a dict
array_of_vm_removed_event_form_dict = array_of_vm_removed_event.from_dict(array_of_vm_removed_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


