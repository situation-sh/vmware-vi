# ArrayOfVmEmigratingEvent

A boxed array of *VmEmigratingEvent*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[VmEmigratingEvent]**](VmEmigratingEvent.md) |  | 

## Example

```python
from vmware_vi.models.array_of_vm_emigrating_event import ArrayOfVmEmigratingEvent

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfVmEmigratingEvent from a JSON string
array_of_vm_emigrating_event_instance = ArrayOfVmEmigratingEvent.from_json(json)
# print the JSON string representation of the object
print ArrayOfVmEmigratingEvent.to_json()

# convert the object into a dict
array_of_vm_emigrating_event_dict = array_of_vm_emigrating_event_instance.to_dict()
# create an instance of ArrayOfVmEmigratingEvent from a dict
array_of_vm_emigrating_event_form_dict = array_of_vm_emigrating_event.from_dict(array_of_vm_emigrating_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


