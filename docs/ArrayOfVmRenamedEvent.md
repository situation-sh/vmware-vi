# ArrayOfVmRenamedEvent

A boxed array of *VmRenamedEvent*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[VmRenamedEvent]**](VmRenamedEvent.md) |  | 

## Example

```python
from vmware_vi.models.array_of_vm_renamed_event import ArrayOfVmRenamedEvent

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfVmRenamedEvent from a JSON string
array_of_vm_renamed_event_instance = ArrayOfVmRenamedEvent.from_json(json)
# print the JSON string representation of the object
print ArrayOfVmRenamedEvent.to_json()

# convert the object into a dict
array_of_vm_renamed_event_dict = array_of_vm_renamed_event_instance.to_dict()
# create an instance of ArrayOfVmRenamedEvent from a dict
array_of_vm_renamed_event_form_dict = array_of_vm_renamed_event.from_dict(array_of_vm_renamed_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


