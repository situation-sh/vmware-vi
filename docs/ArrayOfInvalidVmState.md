# ArrayOfInvalidVmState

A boxed array of *InvalidVmState*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[InvalidVmState]**](InvalidVmState.md) |  | 

## Example

```python
from vmware_vi.models.array_of_invalid_vm_state import ArrayOfInvalidVmState

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfInvalidVmState from a JSON string
array_of_invalid_vm_state_instance = ArrayOfInvalidVmState.from_json(json)
# print the JSON string representation of the object
print ArrayOfInvalidVmState.to_json()

# convert the object into a dict
array_of_invalid_vm_state_dict = array_of_invalid_vm_state_instance.to_dict()
# create an instance of ArrayOfInvalidVmState from a dict
array_of_invalid_vm_state_form_dict = array_of_invalid_vm_state.from_dict(array_of_invalid_vm_state_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


