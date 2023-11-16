# ArrayOfHostSystemReconnectSpec

A boxed array of *HostSystemReconnectSpec*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[HostSystemReconnectSpec]**](HostSystemReconnectSpec.md) |  | 

## Example

```python
from vmware_vi.models.array_of_host_system_reconnect_spec import ArrayOfHostSystemReconnectSpec

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfHostSystemReconnectSpec from a JSON string
array_of_host_system_reconnect_spec_instance = ArrayOfHostSystemReconnectSpec.from_json(json)
# print the JSON string representation of the object
print ArrayOfHostSystemReconnectSpec.to_json()

# convert the object into a dict
array_of_host_system_reconnect_spec_dict = array_of_host_system_reconnect_spec_instance.to_dict()
# create an instance of ArrayOfHostSystemReconnectSpec from a dict
array_of_host_system_reconnect_spec_form_dict = array_of_host_system_reconnect_spec.from_dict(array_of_host_system_reconnect_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


