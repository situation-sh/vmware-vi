# NetDnsConfigInfo

Domain Name Server (DNS) Configuration Specification - a data object for reporting the configuration of RFC 1034 client side DNS settings.  ***Since:*** vSphere API 4.1 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dhcp** | **bool** | Indicates whether or not dynamic host control protocol (DHCP) is used to configure DNS configuration.  ***Since:*** vSphere API 4.1  | 
**host_name** | **str** | The host name portion of DNS name.  For example, \&quot;esx01\&quot; part of esx01.example.com.  ***Since:*** vSphere API 4.1  | 
**domain_name** | **str** | The domain name portion of the DNS name.  \&quot;example.com\&quot; part of esx01.example.com.  ***Since:*** vSphere API 4.1  | 
**ip_address** | **List[str]** | The IP addresses of the DNS servers in order of use.  IPv4 addresses are specified using dotted decimal notation. For example, \&quot;192.0.2.1\&quot;. IPv6 addresses are 128-bit addresses represented as eight fields of up to four hexadecimal digits. A colon separates each field (:). For example, 2001:DB8:101::230:6eff:fe04:d9ff. The address can also consist of the symbol &#39;::&#39; to represent multiple 16-bit groups of contiguous 0&#39;s only once in an address as described in RFC 2373.  ***Since:*** vSphere API 4.1  | [optional] 
**search_domain** | **List[str]** | The domain in which to search for hosts, placed in order of preference.  ***Since:*** vSphere API 4.1  | [optional] 

## Example

```python
from vmware_vi.models.net_dns_config_info import NetDnsConfigInfo

# TODO update the JSON string below
json = "{}"
# create an instance of NetDnsConfigInfo from a JSON string
net_dns_config_info_instance = NetDnsConfigInfo.from_json(json)
# print the JSON string representation of the object
print NetDnsConfigInfo.to_json()

# convert the object into a dict
net_dns_config_info_dict = net_dns_config_info_instance.to_dict()
# create an instance of NetDnsConfigInfo from a dict
net_dns_config_info_form_dict = net_dns_config_info.from_dict(net_dns_config_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


