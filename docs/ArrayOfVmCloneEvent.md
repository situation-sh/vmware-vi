# ArrayOfVmCloneEvent

A boxed array of *VmCloneEvent*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[VmCloneEvent]**](VmCloneEvent.md) |  | 

## Example

```python
from vmware_vi.models.array_of_vm_clone_event import ArrayOfVmCloneEvent

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfVmCloneEvent from a JSON string
array_of_vm_clone_event_instance = ArrayOfVmCloneEvent.from_json(json)
# print the JSON string representation of the object
print ArrayOfVmCloneEvent.to_json()

# convert the object into a dict
array_of_vm_clone_event_dict = array_of_vm_clone_event_instance.to_dict()
# create an instance of ArrayOfVmCloneEvent from a dict
array_of_vm_clone_event_form_dict = array_of_vm_clone_event.from_dict(array_of_vm_clone_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


