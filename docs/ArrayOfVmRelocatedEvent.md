# ArrayOfVmRelocatedEvent

A boxed array of *VmRelocatedEvent*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[VmRelocatedEvent]**](VmRelocatedEvent.md) |  | 

## Example

```python
from vmware_vi.models.array_of_vm_relocated_event import ArrayOfVmRelocatedEvent

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfVmRelocatedEvent from a JSON string
array_of_vm_relocated_event_instance = ArrayOfVmRelocatedEvent.from_json(json)
# print the JSON string representation of the object
print ArrayOfVmRelocatedEvent.to_json()

# convert the object into a dict
array_of_vm_relocated_event_dict = array_of_vm_relocated_event_instance.to_dict()
# create an instance of ArrayOfVmRelocatedEvent from a dict
array_of_vm_relocated_event_form_dict = array_of_vm_relocated_event.from_dict(array_of_vm_relocated_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


