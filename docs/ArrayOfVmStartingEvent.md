# ArrayOfVmStartingEvent

A boxed array of *VmStartingEvent*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[VmStartingEvent]**](VmStartingEvent.md) |  | 

## Example

```python
from vmware_vi.models.array_of_vm_starting_event import ArrayOfVmStartingEvent

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfVmStartingEvent from a JSON string
array_of_vm_starting_event_instance = ArrayOfVmStartingEvent.from_json(json)
# print the JSON string representation of the object
print ArrayOfVmStartingEvent.to_json()

# convert the object into a dict
array_of_vm_starting_event_dict = array_of_vm_starting_event_instance.to_dict()
# create an instance of ArrayOfVmStartingEvent from a dict
array_of_vm_starting_event_form_dict = array_of_vm_starting_event.from_dict(array_of_vm_starting_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


