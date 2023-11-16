# HostDnsConfig

This data object type describes the DNS configuration.  All IPv4 addresses, subnet addresses, and netmasks are specified using dotted decimal notation. For example, \"192.0.2.1\". IPv6 addresses are 128-bit addresses represented as eight fields of up to four hexadecimal digits. A colon separates each field (:). For example, 2001:DB8:101::230:6eff:fe04:d9ff. The address can also consist of the symbol '::' to represent multiple 16-bit groups of contiguous 0's only once in an address as described in RFC 2373. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dhcp** | **bool** | The flag to indicate whether or not DHCP (dynamic host control protocol) is used to determine DNS configuration automatically.  | 
**virtual_nic_device** | **str** | If DHCP is enabled, the DHCP DNS of the vmkernel nic will override the system&#39;s DNS.  This field applies to both IPv4 and IPv6 DNS settings if *ipv6VirtualNicDevice* is unset, otherwise it is applicable only for IPv4 setting. This field is ignored if DHCP is disabled by the *dhcp* property.  | [optional] 
**ipv6_virtual_nic_device** | **str** | If DHCP is enabled, the IPv6 DHCP DNS of the vmkernel nic will override the system&#39;s IPv6 DNS.  This field is ignored if DHCP is disabled by the *dhcp* property.  ***Since:*** vSphere API 6.7  | [optional] 
**host_name** | **str** | The host name portion of DNS name.  For example, \&quot;esx01\&quot;.  **Note**: When DHCP is not enabled, the property can be set explicitly. When DHCP is enabled, the property reflects the current DNS configuration, but cannot be set. The hostName can&#39;t have character &#39;.&#39; in it when set explicitly.  | 
**domain_name** | **str** | The domain name portion of the DNS name.  For example, \&quot;vmware.com\&quot;.  **Note**: When DHCP is not enabled, the property can be set explicitly. When DHCP is enabled, the property reflects the current DNS configuration, but cannot be set.  | 
**address** | **List[str]** | The IP addresses of the DNS servers, placed in order of preference.  **Note**: When DHCP is not enabled, the property can be set explicitly. When DHCP is enabled, the property reflects the current DNS configuration, but cannot be set.  | [optional] 
**search_domain** | **List[str]** | The domain in which to search for hosts, placed in order of preference.  **Note**: When DHCP is not enabled, the property can be set explicitly. When DHCP is enabled, the property reflects the current DNS configuration, but cannot be set.  | [optional] 

## Example

```python
from vmware_vi.models.host_dns_config import HostDnsConfig

# TODO update the JSON string below
json = "{}"
# create an instance of HostDnsConfig from a JSON string
host_dns_config_instance = HostDnsConfig.from_json(json)
# print the JSON string representation of the object
print HostDnsConfig.to_json()

# convert the object into a dict
host_dns_config_dict = host_dns_config_instance.to_dict()
# create an instance of HostDnsConfig from a dict
host_dns_config_form_dict = host_dns_config.from_dict(host_dns_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


