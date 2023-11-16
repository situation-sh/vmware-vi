# ArrayOfVmConnectedEvent

A boxed array of *VmConnectedEvent*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[VmConnectedEvent]**](VmConnectedEvent.md) |  | 

## Example

```python
from vmware_vi.models.array_of_vm_connected_event import ArrayOfVmConnectedEvent

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfVmConnectedEvent from a JSON string
array_of_vm_connected_event_instance = ArrayOfVmConnectedEvent.from_json(json)
# print the JSON string representation of the object
print ArrayOfVmConnectedEvent.to_json()

# convert the object into a dict
array_of_vm_connected_event_dict = array_of_vm_connected_event_instance.to_dict()
# create an instance of ArrayOfVmConnectedEvent from a dict
array_of_vm_connected_event_form_dict = array_of_vm_connected_event.from_dict(array_of_vm_connected_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


