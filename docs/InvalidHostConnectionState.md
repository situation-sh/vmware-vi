# InvalidHostConnectionState

The host has an invalid connection state.  ***Since:*** vSphere API 5.1 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.invalid_host_connection_state import InvalidHostConnectionState

# TODO update the JSON string below
json = "{}"
# create an instance of InvalidHostConnectionState from a JSON string
invalid_host_connection_state_instance = InvalidHostConnectionState.from_json(json)
# print the JSON string representation of the object
print InvalidHostConnectionState.to_json()

# convert the object into a dict
invalid_host_connection_state_dict = invalid_host_connection_state_instance.to_dict()
# create an instance of InvalidHostConnectionState from a dict
invalid_host_connection_state_form_dict = invalid_host_connection_state.from_dict(invalid_host_connection_state_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


