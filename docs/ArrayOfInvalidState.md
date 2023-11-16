# ArrayOfInvalidState

A boxed array of *InvalidState*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[InvalidState]**](InvalidState.md) |  | 

## Example

```python
from vmware_vi.models.array_of_invalid_state import ArrayOfInvalidState

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfInvalidState from a JSON string
array_of_invalid_state_instance = ArrayOfInvalidState.from_json(json)
# print the JSON string representation of the object
print ArrayOfInvalidState.to_json()

# convert the object into a dict
array_of_invalid_state_dict = array_of_invalid_state_instance.to_dict()
# create an instance of ArrayOfInvalidState from a dict
array_of_invalid_state_form_dict = array_of_invalid_state.from_dict(array_of_invalid_state_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


