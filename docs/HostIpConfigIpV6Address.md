# HostIpConfigIpV6Address

The ipv6 address specification  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ip_address** | **str** | The ipv6 address.  When DHCP is enabled, this property reflects the current IP configuration and cannot be set.  ***Since:*** vSphere API 4.0  | 
**prefix_length** | **int** | The prefix length.  An ipv6 prefixLength is a decimal value that indicates the number of contiguous, higher-order bits of the address that make up the network portion of the address. For example, 10FA:6604:8136:6502::/64 is a possible IPv6 prefix. The prefix length in this case is 64.  ***Since:*** vSphere API 4.0  | 
**origin** | **str** | The type of the ipv6 address configuration on the interface.  This can be one of the types defined my the enum *HostIpConfigIpV6AddressConfigType_enum*.  ***Since:*** vSphere API 4.0  | [optional] 
**dad_state** | **str** | The state of this ipAddress.  Can be one of *HostIpConfigIpV6AddressStatus_enum*  ***Since:*** vSphere API 4.0  | [optional] 
**lifetime** | **datetime** | The time when will this address expire.  If not set the address lifetime is unlimited.  ***Since:*** vSphere API 4.0  | [optional] 
**operation** | **str** | Valid values are \&quot;add\&quot; and \&quot;remove\&quot;.  See *HostConfigChangeOperation_enum*.  ***Since:*** vSphere API 4.0  | [optional] 

## Example

```python
from vmware_vi.models.host_ip_config_ip_v6_address import HostIpConfigIpV6Address

# TODO update the JSON string below
json = "{}"
# create an instance of HostIpConfigIpV6Address from a JSON string
host_ip_config_ip_v6_address_instance = HostIpConfigIpV6Address.from_json(json)
# print the JSON string representation of the object
print HostIpConfigIpV6Address.to_json()

# convert the object into a dict
host_ip_config_ip_v6_address_dict = host_ip_config_ip_v6_address_instance.to_dict()
# create an instance of HostIpConfigIpV6Address from a dict
host_ip_config_ip_v6_address_form_dict = host_ip_config_ip_v6_address.from_dict(host_ip_config_ip_v6_address_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


