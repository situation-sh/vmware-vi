# ArrayOfVmDisconnectedEvent

A boxed array of *VmDisconnectedEvent*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[VmDisconnectedEvent]**](VmDisconnectedEvent.md) |  | 

## Example

```python
from vmware_vi.models.array_of_vm_disconnected_event import ArrayOfVmDisconnectedEvent

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfVmDisconnectedEvent from a JSON string
array_of_vm_disconnected_event_instance = ArrayOfVmDisconnectedEvent.from_json(json)
# print the JSON string representation of the object
print ArrayOfVmDisconnectedEvent.to_json()

# convert the object into a dict
array_of_vm_disconnected_event_dict = array_of_vm_disconnected_event_instance.to_dict()
# create an instance of ArrayOfVmDisconnectedEvent from a dict
array_of_vm_disconnected_event_form_dict = array_of_vm_disconnected_event.from_dict(array_of_vm_disconnected_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


