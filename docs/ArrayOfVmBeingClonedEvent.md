# ArrayOfVmBeingClonedEvent

A boxed array of *VmBeingClonedEvent*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[VmBeingClonedEvent]**](VmBeingClonedEvent.md) |  | 

## Example

```python
from vmware_vi.models.array_of_vm_being_cloned_event import ArrayOfVmBeingClonedEvent

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfVmBeingClonedEvent from a JSON string
array_of_vm_being_cloned_event_instance = ArrayOfVmBeingClonedEvent.from_json(json)
# print the JSON string representation of the object
print ArrayOfVmBeingClonedEvent.to_json()

# convert the object into a dict
array_of_vm_being_cloned_event_dict = array_of_vm_being_cloned_event_instance.to_dict()
# create an instance of ArrayOfVmBeingClonedEvent from a dict
array_of_vm_being_cloned_event_form_dict = array_of_vm_being_cloned_event.from_dict(array_of_vm_being_cloned_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


