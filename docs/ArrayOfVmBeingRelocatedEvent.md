# ArrayOfVmBeingRelocatedEvent

A boxed array of *VmBeingRelocatedEvent*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[VmBeingRelocatedEvent]**](VmBeingRelocatedEvent.md) |  | 

## Example

```python
from vmware_vi.models.array_of_vm_being_relocated_event import ArrayOfVmBeingRelocatedEvent

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfVmBeingRelocatedEvent from a JSON string
array_of_vm_being_relocated_event_instance = ArrayOfVmBeingRelocatedEvent.from_json(json)
# print the JSON string representation of the object
print ArrayOfVmBeingRelocatedEvent.to_json()

# convert the object into a dict
array_of_vm_being_relocated_event_dict = array_of_vm_being_relocated_event_instance.to_dict()
# create an instance of ArrayOfVmBeingRelocatedEvent from a dict
array_of_vm_being_relocated_event_form_dict = array_of_vm_being_relocated_event.from_dict(array_of_vm_being_relocated_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


