# IpPoolIpPoolConfigInfo

Specifications of either IPv4 or IPv6 configuration to be used on this network.  This is a part of network configuration.  IPv4 addresses are in dot-decimal notation, e.g.: 192.0.2.235  IPv6 addresses are in colon-hexadecimal notation, e.g.: 2001:0db8:85a3::0370:7334  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**subnet_address** | **str** | Address of the subnet.  For example: - IPv4: 192.168.5.0 - IPv6: 2001:0db8:85a3::    ***Since:*** vSphere API 4.0  | [optional] 
**netmask** | **str** | Netmask  For example: - IPv4: 255.255.255.0 - IPv6: ffff:ffff:ffff::    ***Since:*** vSphere API 4.0  | [optional] 
**gateway** | **str** | Gateway.  This can be an empty string - if no gateway is configured.  Examples: - IPv4: 192.168.5.1 - IPv6: 2001:0db8:85a3::1    ***Since:*** vSphere API 4.0  | [optional] 
**range** | **str** | IP range.  This is specified as a set of ranges separated with commas. One range is given by a start address, a hash (#), and the length of the range.  For example: - 192.0.2.235 # 20 is the IPv4 range from 192.0.2.235 to 192.0.2.254 - 2001::7334 # 20 is the IPv6 range from 2001::7334 to 2001::7347    ***Since:*** vSphere API 4.0  | [optional] 
**dns** | **List[str]** | DNS servers  For example: - IPv4: \\[\&quot;10.20.0.1\&quot;, \&quot;10.20.0.2\&quot;\\] - IPv6: \\[\&quot;2001:0db8:85a3::0370:7334\&quot;, \&quot;2001:0db8:85a3::0370:7335\&quot;\\]    If an empty list is passed, the existing value remains unchanged. To clear this list, pass an array containing the empty string as it&#39;s only element.  ***Since:*** vSphere API 4.0  | [optional] 
**dhcp_server_available** | **bool** | Whether a DHCP server is available on this network.  ***Since:*** vSphere API 4.0  | [optional] 
**ip_pool_enabled** | **bool** | IP addresses can only be allocated from the range if the IP pool is enabled.  ***Since:*** vSphere API 4.0  | [optional] 

## Example

```python
from vmware_vi.models.ip_pool_ip_pool_config_info import IpPoolIpPoolConfigInfo

# TODO update the JSON string below
json = "{}"
# create an instance of IpPoolIpPoolConfigInfo from a JSON string
ip_pool_ip_pool_config_info_instance = IpPoolIpPoolConfigInfo.from_json(json)
# print the JSON string representation of the object
print IpPoolIpPoolConfigInfo.to_json()

# convert the object into a dict
ip_pool_ip_pool_config_info_dict = ip_pool_ip_pool_config_info_instance.to_dict()
# create an instance of IpPoolIpPoolConfigInfo from a dict
ip_pool_ip_pool_config_info_form_dict = ip_pool_ip_pool_config_info.from_dict(ip_pool_ip_pool_config_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


