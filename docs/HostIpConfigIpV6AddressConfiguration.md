# HostIpConfigIpV6AddressConfiguration

The ipv6 address configuration  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ip_v6_address** | [**List[HostIpConfigIpV6Address]**](HostIpConfigIpV6Address.md) | Ipv6 adrresses configured on the interface.  The global addresses can be configured through DHCP, stateless or manual configuration. Link local addresses can be only configured with the origin set to *other*.  ***Since:*** vSphere API 4.0  | [optional] 
**auto_configuration_enabled** | **bool** | Specify if IPv6 address and routing information information be enabled or not as per RFC 2462.  ***Since:*** vSphere API 4.0  | [optional] 
**dhcp_v6_enabled** | **bool** | The flag to indicate whether or not DHCP (dynamic host control protocol) is enabled to obtain an ipV6 address.  If this property is set to true, an ipV6 address is configured through dhcpV6.  ***Since:*** vSphere API 4.0  | [optional] 

## Example

```python
from vmware_vi.models.host_ip_config_ip_v6_address_configuration import HostIpConfigIpV6AddressConfiguration

# TODO update the JSON string below
json = "{}"
# create an instance of HostIpConfigIpV6AddressConfiguration from a JSON string
host_ip_config_ip_v6_address_configuration_instance = HostIpConfigIpV6AddressConfiguration.from_json(json)
# print the JSON string representation of the object
print HostIpConfigIpV6AddressConfiguration.to_json()

# convert the object into a dict
host_ip_config_ip_v6_address_configuration_dict = host_ip_config_ip_v6_address_configuration_instance.to_dict()
# create an instance of HostIpConfigIpV6AddressConfiguration from a dict
host_ip_config_ip_v6_address_configuration_form_dict = host_ip_config_ip_v6_address_configuration.from_dict(host_ip_config_ip_v6_address_configuration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


