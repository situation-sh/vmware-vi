# ArrayOfVmRegisteredEvent

A boxed array of *VmRegisteredEvent*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[VmRegisteredEvent]**](VmRegisteredEvent.md) |  | 

## Example

```python
from vmware_vi.models.array_of_vm_registered_event import ArrayOfVmRegisteredEvent

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfVmRegisteredEvent from a JSON string
array_of_vm_registered_event_instance = ArrayOfVmRegisteredEvent.from_json(json)
# print the JSON string representation of the object
print ArrayOfVmRegisteredEvent.to_json()

# convert the object into a dict
array_of_vm_registered_event_dict = array_of_vm_registered_event_instance.to_dict()
# create an instance of ArrayOfVmRegisteredEvent from a dict
array_of_vm_registered_event_form_dict = array_of_vm_registered_event.from_dict(array_of_vm_registered_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


