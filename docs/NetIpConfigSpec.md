# NetIpConfigSpec

Internet Protocol Address Configuration for version 4 and version 6.  ***Since:*** vSphere API 4.1 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ip_address** | [**List[NetIpConfigSpecIpAddressSpec]**](NetIpConfigSpecIpAddressSpec.md) | A set of manual (static) IP addresses to be configured on a given interface.  ***Since:*** vSphere API 4.1  | [optional] 
**dhcp** | [**NetDhcpConfigSpec**](NetDhcpConfigSpec.md) |  | [optional] 
**auto_configuration_enabled** | **bool** | Enable or disable ICMPv6 router solictitation requests from a given interface to acquire an IPv6 address and default gateway route from zero, one or more routers on the connected network.  ***Since:*** vSphere API 4.1  | [optional] 

## Example

```python
from vmware_vi.models.net_ip_config_spec import NetIpConfigSpec

# TODO update the JSON string below
json = "{}"
# create an instance of NetIpConfigSpec from a JSON string
net_ip_config_spec_instance = NetIpConfigSpec.from_json(json)
# print the JSON string representation of the object
print NetIpConfigSpec.to_json()

# convert the object into a dict
net_ip_config_spec_dict = net_ip_config_spec_instance.to_dict()
# create an instance of NetIpConfigSpec from a dict
net_ip_config_spec_form_dict = net_ip_config_spec.from_dict(net_ip_config_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


