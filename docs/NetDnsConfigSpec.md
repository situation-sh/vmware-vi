# NetDnsConfigSpec

Domain Name Server (DNS) Configuration Specification - a data object for configuring the RFC 1034 client side DNS settings.  TBD: remove this section, only for discussing what goes into this object. Place properties here that are specific to the RFC/common to all systems. Properties that are platform specific should go into a separate config spec. http://technet.microsoft.com/en-us/library/cc778792.aspx http://en.wikipedia.org/wiki/Microsoft\\_DNS  ***Since:*** vSphere API 4.1 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dhcp** | **bool** | The flag to indicate whether or not dynamic host control protocol (DHCP) will be used to set DNS configuration automatically.  See vim.net.DhcpConfigSpec  ***Since:*** vSphere API 4.1  | [optional] 
**host_name** | **str** | The host name portion of DNS name.  For example, \&quot;esx01\&quot; part of esx01.example.com. The rules for forming a hostname are specified in RFC 1034.  ***Since:*** vSphere API 4.1  | [optional] 
**domain_name** | **str** | The domain name portion of the DNS name.  This would be the \&quot;example.com\&quot; part of esx01.example.com. The rules for forming a domain name are defined in RFC 1034.  ***Since:*** vSphere API 4.1  | [optional] 
**ip_address** | **List[str]** | Unicast IP address(s) of one or more DNS servers in order of use.  IPv4 addresses are specified using dotted decimal notation. For example, \&quot;192.0.2.1\&quot;. IPv6 addresses are 128-bit addresses represented as eight fields of up to four hexadecimal digits. A colon separates each field (:). For example, 2001:DB8:101::230:6eff:fe04:d9ff. The address can also consist of the symbol &#39;::&#39; to represent multiple 16-bit groups of contiguous 0&#39;s only once in an address as described in RFC 2373.  ***Since:*** vSphere API 4.1  | [optional] 
**search_domain** | **List[str]** | The domain in which to search for hosts in order of preference.  ***Since:*** vSphere API 4.1  | [optional] 

## Example

```python
from vmware_vi.models.net_dns_config_spec import NetDnsConfigSpec

# TODO update the JSON string below
json = "{}"
# create an instance of NetDnsConfigSpec from a JSON string
net_dns_config_spec_instance = NetDnsConfigSpec.from_json(json)
# print the JSON string representation of the object
print NetDnsConfigSpec.to_json()

# convert the object into a dict
net_dns_config_spec_dict = net_dns_config_spec_instance.to_dict()
# create an instance of NetDnsConfigSpec from a dict
net_dns_config_spec_form_dict = net_dns_config_spec.from_dict(net_dns_config_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


