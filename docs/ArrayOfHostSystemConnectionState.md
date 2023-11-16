# ArrayOfHostSystemConnectionState

A boxed array of *HostSystemConnectionState_enum*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[HostSystemConnectionStateEnum]**](HostSystemConnectionStateEnum.md) |  | 

## Example

```python
from vmware_vi.models.array_of_host_system_connection_state import ArrayOfHostSystemConnectionState

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfHostSystemConnectionState from a JSON string
array_of_host_system_connection_state_instance = ArrayOfHostSystemConnectionState.from_json(json)
# print the JSON string representation of the object
print ArrayOfHostSystemConnectionState.to_json()

# convert the object into a dict
array_of_host_system_connection_state_dict = array_of_host_system_connection_state_instance.to_dict()
# create an instance of ArrayOfHostSystemConnectionState from a dict
array_of_host_system_connection_state_form_dict = array_of_host_system_connection_state.from_dict(array_of_host_system_connection_state_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


