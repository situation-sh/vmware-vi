# ArrayOfHostNetworkResourceRuntime

A boxed array of *HostNetworkResourceRuntime*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[HostNetworkResourceRuntime]**](HostNetworkResourceRuntime.md) |  | 

## Example

```python
from vmware_vi.models.array_of_host_network_resource_runtime import ArrayOfHostNetworkResourceRuntime

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfHostNetworkResourceRuntime from a JSON string
array_of_host_network_resource_runtime_instance = ArrayOfHostNetworkResourceRuntime.from_json(json)
# print the JSON string representation of the object
print ArrayOfHostNetworkResourceRuntime.to_json()

# convert the object into a dict
array_of_host_network_resource_runtime_dict = array_of_host_network_resource_runtime_instance.to_dict()
# create an instance of ArrayOfHostNetworkResourceRuntime from a dict
array_of_host_network_resource_runtime_form_dict = array_of_host_network_resource_runtime.from_dict(array_of_host_network_resource_runtime_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


