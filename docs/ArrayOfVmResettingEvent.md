# ArrayOfVmResettingEvent

A boxed array of *VmResettingEvent*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[VmResettingEvent]**](VmResettingEvent.md) |  | 

## Example

```python
from vmware_vi.models.array_of_vm_resetting_event import ArrayOfVmResettingEvent

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfVmResettingEvent from a JSON string
array_of_vm_resetting_event_instance = ArrayOfVmResettingEvent.from_json(json)
# print the JSON string representation of the object
print ArrayOfVmResettingEvent.to_json()

# convert the object into a dict
array_of_vm_resetting_event_dict = array_of_vm_resetting_event_instance.to_dict()
# create an instance of ArrayOfVmResettingEvent from a dict
array_of_vm_resetting_event_form_dict = array_of_vm_resetting_event.from_dict(array_of_vm_resetting_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


