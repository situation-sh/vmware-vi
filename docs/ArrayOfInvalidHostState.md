# ArrayOfInvalidHostState

A boxed array of *InvalidHostState*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[InvalidHostState]**](InvalidHostState.md) |  | 

## Example

```python
from vmware_vi.models.array_of_invalid_host_state import ArrayOfInvalidHostState

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfInvalidHostState from a JSON string
array_of_invalid_host_state_instance = ArrayOfInvalidHostState.from_json(json)
# print the JSON string representation of the object
print ArrayOfInvalidHostState.to_json()

# convert the object into a dict
array_of_invalid_host_state_dict = array_of_invalid_host_state_instance.to_dict()
# create an instance of ArrayOfInvalidHostState from a dict
array_of_invalid_host_state_form_dict = array_of_invalid_host_state.from_dict(array_of_invalid_host_state_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


