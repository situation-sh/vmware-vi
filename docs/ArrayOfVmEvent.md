# ArrayOfVmEvent

A boxed array of *VmEvent*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[VmEvent]**](VmEvent.md) |  | 

## Example

```python
from vmware_vi.models.array_of_vm_event import ArrayOfVmEvent

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfVmEvent from a JSON string
array_of_vm_event_instance = ArrayOfVmEvent.from_json(json)
# print the JSON string representation of the object
print ArrayOfVmEvent.to_json()

# convert the object into a dict
array_of_vm_event_dict = array_of_vm_event_instance.to_dict()
# create an instance of ArrayOfVmEvent from a dict
array_of_vm_event_form_dict = array_of_vm_event.from_dict(array_of_vm_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


