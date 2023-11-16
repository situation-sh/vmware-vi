# ArrayOfMissingNetworkIpConfig

A boxed array of *MissingNetworkIpConfig*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[MissingNetworkIpConfig]**](MissingNetworkIpConfig.md) |  | 

## Example

```python
from vmware_vi.models.array_of_missing_network_ip_config import ArrayOfMissingNetworkIpConfig

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfMissingNetworkIpConfig from a JSON string
array_of_missing_network_ip_config_instance = ArrayOfMissingNetworkIpConfig.from_json(json)
# print the JSON string representation of the object
print ArrayOfMissingNetworkIpConfig.to_json()

# convert the object into a dict
array_of_missing_network_ip_config_dict = array_of_missing_network_ip_config_instance.to_dict()
# create an instance of ArrayOfMissingNetworkIpConfig from a dict
array_of_missing_network_ip_config_form_dict = array_of_missing_network_ip_config.from_dict(array_of_missing_network_ip_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


