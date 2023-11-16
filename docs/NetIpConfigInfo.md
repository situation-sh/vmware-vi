# NetIpConfigInfo

Protocol version independent address reporting data object for network interfaces.  ***Since:*** vSphere API 4.1 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ip_address** | [**List[NetIpConfigInfoIpAddress]**](NetIpConfigInfoIpAddress.md) | Zero, one or more manual (static) assigned IP addresses to be configured on a given interface.  ***Since:*** vSphere API 4.1  | [optional] 
**dhcp** | [**NetDhcpConfigInfo**](NetDhcpConfigInfo.md) |  | [optional] 
**auto_configuration_enabled** | **bool** | Enable or disable ICMPv6 router solictitation requests from a given interface to acquire an IPv6 address and default gateway route from zero, one or more routers on the connected network.  If not set then ICMPv6 is not available on this system, See vim.host.Network.Capabilities  ***Since:*** vSphere API 4.1  | [optional] 

## Example

```python
from vmware_vi.models.net_ip_config_info import NetIpConfigInfo

# TODO update the JSON string below
json = "{}"
# create an instance of NetIpConfigInfo from a JSON string
net_ip_config_info_instance = NetIpConfigInfo.from_json(json)
# print the JSON string representation of the object
print NetIpConfigInfo.to_json()

# convert the object into a dict
net_ip_config_info_dict = net_ip_config_info_instance.to_dict()
# create an instance of NetIpConfigInfo from a dict
net_ip_config_info_form_dict = net_ip_config_info.from_dict(net_ip_config_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


