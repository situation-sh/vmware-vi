# ArrayOfVmStoppingEvent

A boxed array of *VmStoppingEvent*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[VmStoppingEvent]**](VmStoppingEvent.md) |  | 

## Example

```python
from vmware_vi.models.array_of_vm_stopping_event import ArrayOfVmStoppingEvent

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfVmStoppingEvent from a JSON string
array_of_vm_stopping_event_instance = ArrayOfVmStoppingEvent.from_json(json)
# print the JSON string representation of the object
print ArrayOfVmStoppingEvent.to_json()

# convert the object into a dict
array_of_vm_stopping_event_dict = array_of_vm_stopping_event_instance.to_dict()
# create an instance of ArrayOfVmStoppingEvent from a dict
array_of_vm_stopping_event_form_dict = array_of_vm_stopping_event.from_dict(array_of_vm_stopping_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


