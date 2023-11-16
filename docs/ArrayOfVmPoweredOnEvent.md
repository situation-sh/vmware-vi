# ArrayOfVmPoweredOnEvent

A boxed array of *VmPoweredOnEvent*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[VmPoweredOnEvent]**](VmPoweredOnEvent.md) |  | 

## Example

```python
from vmware_vi.models.array_of_vm_powered_on_event import ArrayOfVmPoweredOnEvent

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfVmPoweredOnEvent from a JSON string
array_of_vm_powered_on_event_instance = ArrayOfVmPoweredOnEvent.from_json(json)
# print the JSON string representation of the object
print ArrayOfVmPoweredOnEvent.to_json()

# convert the object into a dict
array_of_vm_powered_on_event_dict = array_of_vm_powered_on_event_instance.to_dict()
# create an instance of ArrayOfVmPoweredOnEvent from a dict
array_of_vm_powered_on_event_form_dict = array_of_vm_powered_on_event.from_dict(array_of_vm_powered_on_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


