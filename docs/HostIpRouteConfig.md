# HostIpRouteConfig

IP Route Configuration.  All IPv4 addresses, subnet addresses, and netmasks are specified as strings using dotted decimal notation. For example, \"192.0.2.1\". IPv6 addresses are 128-bit addresses represented as eight fields of up to four hexadecimal digits. A colon separates each field (:). For example, 2001:DB8:101::230:6eff:fe04:d9ff. The address can also consist of symbol '::' to represent multiple 16-bit groups of contiguous 0's only once in an address as described in RFC 2373. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**default_gateway** | **str** | The default gateway address.  | [optional] 
**gateway_device** | **str** | The gateway device.  This applies to service console gateway only, it is ignored otherwise.  | [optional] 
**ip_v6_default_gateway** | **str** | The default ipv6 gateway address  ***Since:*** vSphere API 4.0  | [optional] 
**ip_v6_gateway_device** | **str** | The ipv6 gateway device.  This applies to service console gateway only, it  ***Since:*** vSphere API 4.0  | [optional] 

## Example

```python
from vmware_vi.models.host_ip_route_config import HostIpRouteConfig

# TODO update the JSON string below
json = "{}"
# create an instance of HostIpRouteConfig from a JSON string
host_ip_route_config_instance = HostIpRouteConfig.from_json(json)
# print the JSON string representation of the object
print HostIpRouteConfig.to_json()

# convert the object into a dict
host_ip_route_config_dict = host_ip_route_config_instance.to_dict()
# create an instance of HostIpRouteConfig from a dict
host_ip_route_config_form_dict = host_ip_route_config.from_dict(host_ip_route_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


