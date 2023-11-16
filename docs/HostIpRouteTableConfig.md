# HostIpRouteTableConfig

IpRouteEntry.  Routing entries are individual static routes which combined with the default route form all of the routing rules for a host.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ip_route** | [**List[HostIpRouteOp]**](HostIpRouteOp.md) | The array of Routing ops (routes to be added/removed)  ***Since:*** vSphere API 4.0  | [optional] 
**ipv6_route** | [**List[HostIpRouteOp]**](HostIpRouteOp.md) |  | [optional] 

## Example

```python
from vmware_vi.models.host_ip_route_table_config import HostIpRouteTableConfig

# TODO update the JSON string below
json = "{}"
# create an instance of HostIpRouteTableConfig from a JSON string
host_ip_route_table_config_instance = HostIpRouteTableConfig.from_json(json)
# print the JSON string representation of the object
print HostIpRouteTableConfig.to_json()

# convert the object into a dict
host_ip_route_table_config_dict = host_ip_route_table_config_instance.to_dict()
# create an instance of HostIpRouteTableConfig from a dict
host_ip_route_table_config_form_dict = host_ip_route_table_config.from_dict(host_ip_route_table_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


