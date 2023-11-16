# InvalidVmState

The VM has an invalid state.  ***Since:*** vSphere API 6.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vm** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | 

## Example

```python
from vmware_vi.models.invalid_vm_state import InvalidVmState

# TODO update the JSON string below
json = "{}"
# create an instance of InvalidVmState from a JSON string
invalid_vm_state_instance = InvalidVmState.from_json(json)
# print the JSON string representation of the object
print InvalidVmState.to_json()

# convert the object into a dict
invalid_vm_state_dict = invalid_vm_state_instance.to_dict()
# create an instance of InvalidVmState from a dict
invalid_vm_state_form_dict = invalid_vm_state.from_dict(invalid_vm_state_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


