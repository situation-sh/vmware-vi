# InvalidHostState

The host has an invalid state.  ***Since:*** VI API 2.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**host** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | [optional] 

## Example

```python
from vmware_vi.models.invalid_host_state import InvalidHostState

# TODO update the JSON string below
json = "{}"
# create an instance of InvalidHostState from a JSON string
invalid_host_state_instance = InvalidHostState.from_json(json)
# print the JSON string representation of the object
print InvalidHostState.to_json()

# convert the object into a dict
invalid_host_state_dict = invalid_host_state_instance.to_dict()
# create an instance of InvalidHostState from a dict
invalid_host_state_form_dict = invalid_host_state.from_dict(invalid_host_state_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


