# ArrayOfVmSecondaryAddedEvent

A boxed array of *VmSecondaryAddedEvent*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[VmSecondaryAddedEvent]**](VmSecondaryAddedEvent.md) |  | 

## Example

```python
from vmware_vi.models.array_of_vm_secondary_added_event import ArrayOfVmSecondaryAddedEvent

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfVmSecondaryAddedEvent from a JSON string
array_of_vm_secondary_added_event_instance = ArrayOfVmSecondaryAddedEvent.from_json(json)
# print the JSON string representation of the object
print ArrayOfVmSecondaryAddedEvent.to_json()

# convert the object into a dict
array_of_vm_secondary_added_event_dict = array_of_vm_secondary_added_event_instance.to_dict()
# create an instance of ArrayOfVmSecondaryAddedEvent from a dict
array_of_vm_secondary_added_event_form_dict = array_of_vm_secondary_added_event.from_dict(array_of_vm_secondary_added_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


