# NetIpConfigInfoIpAddress

Information about a specific IP Address.  ***Since:*** vSphere API 4.1 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ip_address** | **str** | IPv4 address is specified using dotted decimal notation.  For example, \&quot;192.0.2.1\&quot;. IPv6 addresses are 128-bit addresses represented as eight fields of up to four hexadecimal digits. A colon separates each field (:). For example, 2001:DB8:101::230:6eff:fe04:d9ff. The address can also consist of the symbol &#39;::&#39; to represent multiple 16-bit groups of contiguous 0&#39;s only once in an address as described in RFC 2373.  ***Since:*** vSphere API 4.1  | 
**prefix_length** | **int** | Denotes the length of a generic Internet network address prefix.  The prefix length for IPv4 the value range is 0-32. For IPv6 prefixLength is a decimal value range 0-128. A value of n corresponds to an IP address mask that has n contiguous 1-bits from the most significant bit (MSB), with all other bits set to 0. A value of zero is valid only if the calling context defines it.  ***Since:*** vSphere API 4.1  | 
**origin** | **str** | How this address was configured.  This can be one of the values from the enum IpAddressOrigin See *NetIpConfigInfoIpAddressOrigin_enum* for values.  ***Since:*** vSphere API 4.1  | [optional] 
**state** | **str** | The state of this ipAddress.  Can be one of *NetIpConfigInfoIpAddressStatus_enum*.  ***Since:*** vSphere API 4.1  | [optional] 
**lifetime** | **datetime** | The time when will this address expire.  Durning this time *state* may change states but is still visible from the network.  ***Since:*** vSphere API 4.1  | [optional] 

## Example

```python
from vmware_vi.models.net_ip_config_info_ip_address import NetIpConfigInfoIpAddress

# TODO update the JSON string below
json = "{}"
# create an instance of NetIpConfigInfoIpAddress from a JSON string
net_ip_config_info_ip_address_instance = NetIpConfigInfoIpAddress.from_json(json)
# print the JSON string representation of the object
print NetIpConfigInfoIpAddress.to_json()

# convert the object into a dict
net_ip_config_info_ip_address_dict = net_ip_config_info_ip_address_instance.to_dict()
# create an instance of NetIpConfigInfoIpAddress from a dict
net_ip_config_info_ip_address_form_dict = net_ip_config_info_ip_address.from_dict(net_ip_config_info_ip_address_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


