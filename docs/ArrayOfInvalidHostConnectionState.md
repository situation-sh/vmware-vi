# ArrayOfInvalidHostConnectionState

A boxed array of *InvalidHostConnectionState*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[InvalidHostConnectionState]**](InvalidHostConnectionState.md) |  | 

## Example

```python
from vmware_vi.models.array_of_invalid_host_connection_state import ArrayOfInvalidHostConnectionState

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfInvalidHostConnectionState from a JSON string
array_of_invalid_host_connection_state_instance = ArrayOfInvalidHostConnectionState.from_json(json)
# print the JSON string representation of the object
print ArrayOfInvalidHostConnectionState.to_json()

# convert the object into a dict
array_of_invalid_host_connection_state_dict = array_of_invalid_host_connection_state_instance.to_dict()
# create an instance of ArrayOfInvalidHostConnectionState from a dict
array_of_invalid_host_connection_state_form_dict = array_of_invalid_host_connection_state.from_dict(array_of_invalid_host_connection_state_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


