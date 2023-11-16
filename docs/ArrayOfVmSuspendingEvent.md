# ArrayOfVmSuspendingEvent

A boxed array of *VmSuspendingEvent*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[VmSuspendingEvent]**](VmSuspendingEvent.md) |  | 

## Example

```python
from vmware_vi.models.array_of_vm_suspending_event import ArrayOfVmSuspendingEvent

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfVmSuspendingEvent from a JSON string
array_of_vm_suspending_event_instance = ArrayOfVmSuspendingEvent.from_json(json)
# print the JSON string representation of the object
print ArrayOfVmSuspendingEvent.to_json()

# convert the object into a dict
array_of_vm_suspending_event_dict = array_of_vm_suspending_event_instance.to_dict()
# create an instance of ArrayOfVmSuspendingEvent from a dict
array_of_vm_suspending_event_form_dict = array_of_vm_suspending_event.from_dict(array_of_vm_suspending_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


