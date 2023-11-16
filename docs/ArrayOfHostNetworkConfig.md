# ArrayOfHostNetworkConfig

A boxed array of *HostNetworkConfig*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[HostNetworkConfig]**](HostNetworkConfig.md) |  | 

## Example

```python
from vmware_vi.models.array_of_host_network_config import ArrayOfHostNetworkConfig

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfHostNetworkConfig from a JSON string
array_of_host_network_config_instance = ArrayOfHostNetworkConfig.from_json(json)
# print the JSON string representation of the object
print ArrayOfHostNetworkConfig.to_json()

# convert the object into a dict
array_of_host_network_config_dict = array_of_host_network_config_instance.to_dict()
# create an instance of ArrayOfHostNetworkConfig from a dict
array_of_host_network_config_form_dict = array_of_host_network_config.from_dict(array_of_host_network_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


