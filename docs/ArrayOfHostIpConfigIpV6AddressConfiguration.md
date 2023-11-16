# ArrayOfHostIpConfigIpV6AddressConfiguration

A boxed array of *HostIpConfigIpV6AddressConfiguration*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[HostIpConfigIpV6AddressConfiguration]**](HostIpConfigIpV6AddressConfiguration.md) |  | 

## Example

```python
from vmware_vi.models.array_of_host_ip_config_ip_v6_address_configuration import ArrayOfHostIpConfigIpV6AddressConfiguration

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfHostIpConfigIpV6AddressConfiguration from a JSON string
array_of_host_ip_config_ip_v6_address_configuration_instance = ArrayOfHostIpConfigIpV6AddressConfiguration.from_json(json)
# print the JSON string representation of the object
print ArrayOfHostIpConfigIpV6AddressConfiguration.to_json()

# convert the object into a dict
array_of_host_ip_config_ip_v6_address_configuration_dict = array_of_host_ip_config_ip_v6_address_configuration_instance.to_dict()
# create an instance of ArrayOfHostIpConfigIpV6AddressConfiguration from a dict
array_of_host_ip_config_ip_v6_address_configuration_form_dict = array_of_host_ip_config_ip_v6_address_configuration.from_dict(array_of_host_ip_config_ip_v6_address_configuration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


