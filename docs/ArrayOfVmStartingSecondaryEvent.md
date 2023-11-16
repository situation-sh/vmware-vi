# ArrayOfVmStartingSecondaryEvent

A boxed array of *VmStartingSecondaryEvent*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[VmStartingSecondaryEvent]**](VmStartingSecondaryEvent.md) |  | 

## Example

```python
from vmware_vi.models.array_of_vm_starting_secondary_event import ArrayOfVmStartingSecondaryEvent

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfVmStartingSecondaryEvent from a JSON string
array_of_vm_starting_secondary_event_instance = ArrayOfVmStartingSecondaryEvent.from_json(json)
# print the JSON string representation of the object
print ArrayOfVmStartingSecondaryEvent.to_json()

# convert the object into a dict
array_of_vm_starting_secondary_event_dict = array_of_vm_starting_secondary_event_instance.to_dict()
# create an instance of ArrayOfVmStartingSecondaryEvent from a dict
array_of_vm_starting_secondary_event_form_dict = array_of_vm_starting_secondary_event.from_dict(array_of_vm_starting_secondary_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


