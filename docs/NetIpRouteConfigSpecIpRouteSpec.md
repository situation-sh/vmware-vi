# NetIpRouteConfigSpecIpRouteSpec

Specify an individual host, network or default destination network reachable through a given gateway.  ***Since:*** vSphere API 4.1 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**network** | **str** | IP Address of the destination IP network.  IPv6 addresses are 128-bit addresses represented as eight fields of up to four hexadecimal digits. A colon separates each field (:). For example, 2001:DB8:101::230:6eff:fe04:d9ff. The address can also consist of symbol &#39;::&#39; to represent multiple 16-bit groups of contiguous 0&#39;s only once in an address as described in RFC 2373. To Specify a default network use the value: 0 with prefixLenth 0.  ***Since:*** vSphere API 4.1  | 
**prefix_length** | **int** | The prefix length.  For IPv4 the value range is 0-31. For IPv6 prefixLength is a decimal value range 0-127. The property represents the number of contiguous, higher-order bits of the address that make up the network portion of the IP address.  ***Since:*** vSphere API 4.1  | 
**gateway** | [**NetIpRouteConfigSpecGatewaySpec**](NetIpRouteConfigSpecGatewaySpec.md) |  | 
**operation** | **str** | Requires one of the values from *HostConfigChangeOperation_enum*.  ***Since:*** vSphere API 4.1  | 

## Example

```python
from vmware_vi.models.net_ip_route_config_spec_ip_route_spec import NetIpRouteConfigSpecIpRouteSpec

# TODO update the JSON string below
json = "{}"
# create an instance of NetIpRouteConfigSpecIpRouteSpec from a JSON string
net_ip_route_config_spec_ip_route_spec_instance = NetIpRouteConfigSpecIpRouteSpec.from_json(json)
# print the JSON string representation of the object
print NetIpRouteConfigSpecIpRouteSpec.to_json()

# convert the object into a dict
net_ip_route_config_spec_ip_route_spec_dict = net_ip_route_config_spec_ip_route_spec_instance.to_dict()
# create an instance of NetIpRouteConfigSpecIpRouteSpec from a dict
net_ip_route_config_spec_ip_route_spec_form_dict = net_ip_route_config_spec_ip_route_spec.from_dict(net_ip_route_config_spec_ip_route_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


