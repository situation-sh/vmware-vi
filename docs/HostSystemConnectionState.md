# HostSystemConnectionState

A boxed *HostSystemConnectionState_enum*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**HostSystemConnectionStateEnum**](HostSystemConnectionStateEnum.md) |  | 

## Example

```python
from vmware_vi.models.host_system_connection_state import HostSystemConnectionState

# TODO update the JSON string below
json = "{}"
# create an instance of HostSystemConnectionState from a JSON string
host_system_connection_state_instance = HostSystemConnectionState.from_json(json)
# print the JSON string representation of the object
print HostSystemConnectionState.to_json()

# convert the object into a dict
host_system_connection_state_dict = host_system_connection_state_instance.to_dict()
# create an instance of HostSystemConnectionState from a dict
host_system_connection_state_form_dict = host_system_connection_state.from_dict(host_system_connection_state_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


