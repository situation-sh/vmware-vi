# ArrayOfHostNetworkConfigResult

A boxed array of *HostNetworkConfigResult*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[HostNetworkConfigResult]**](HostNetworkConfigResult.md) |  | 

## Example

```python
from vmware_vi.models.array_of_host_network_config_result import ArrayOfHostNetworkConfigResult

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfHostNetworkConfigResult from a JSON string
array_of_host_network_config_result_instance = ArrayOfHostNetworkConfigResult.from_json(json)
# print the JSON string representation of the object
print ArrayOfHostNetworkConfigResult.to_json()

# convert the object into a dict
array_of_host_network_config_result_dict = array_of_host_network_config_result_instance.to_dict()
# create an instance of ArrayOfHostNetworkConfigResult from a dict
array_of_host_network_config_result_form_dict = array_of_host_network_config_result.from_dict(array_of_host_network_config_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


