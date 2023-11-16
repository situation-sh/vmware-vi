# ArrayOfVmPoweredOffEvent

A boxed array of *VmPoweredOffEvent*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[VmPoweredOffEvent]**](VmPoweredOffEvent.md) |  | 

## Example

```python
from vmware_vi.models.array_of_vm_powered_off_event import ArrayOfVmPoweredOffEvent

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfVmPoweredOffEvent from a JSON string
array_of_vm_powered_off_event_instance = ArrayOfVmPoweredOffEvent.from_json(json)
# print the JSON string representation of the object
print ArrayOfVmPoweredOffEvent.to_json()

# convert the object into a dict
array_of_vm_powered_off_event_dict = array_of_vm_powered_off_event_instance.to_dict()
# create an instance of ArrayOfVmPoweredOffEvent from a dict
array_of_vm_powered_off_event_form_dict = array_of_vm_powered_off_event.from_dict(array_of_vm_powered_off_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


