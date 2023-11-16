# InvalidState

An InvalidState fault is thrown if the operation failed due to the current state of the system. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.invalid_state import InvalidState

# TODO update the JSON string below
json = "{}"
# create an instance of InvalidState from a JSON string
invalid_state_instance = InvalidState.from_json(json)
# print the JSON string representation of the object
print InvalidState.to_json()

# convert the object into a dict
invalid_state_dict = invalid_state_instance.to_dict()
# create an instance of InvalidState from a dict
invalid_state_form_dict = invalid_state.from_dict(invalid_state_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


