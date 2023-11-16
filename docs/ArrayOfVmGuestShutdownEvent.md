# ArrayOfVmGuestShutdownEvent

A boxed array of *VmGuestShutdownEvent*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[VmGuestShutdownEvent]**](VmGuestShutdownEvent.md) |  | 

## Example

```python
from vmware_vi.models.array_of_vm_guest_shutdown_event import ArrayOfVmGuestShutdownEvent

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfVmGuestShutdownEvent from a JSON string
array_of_vm_guest_shutdown_event_instance = ArrayOfVmGuestShutdownEvent.from_json(json)
# print the JSON string representation of the object
print ArrayOfVmGuestShutdownEvent.to_json()

# convert the object into a dict
array_of_vm_guest_shutdown_event_dict = array_of_vm_guest_shutdown_event_instance.to_dict()
# create an instance of ArrayOfVmGuestShutdownEvent from a dict
array_of_vm_guest_shutdown_event_form_dict = array_of_vm_guest_shutdown_event.from_dict(array_of_vm_guest_shutdown_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


