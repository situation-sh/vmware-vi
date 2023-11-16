# HostIpRouteTableInfo

IpRouteTableInfo.  This is the list of all static routes on the host  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ip_route** | [**List[HostIpRouteEntry]**](HostIpRouteEntry.md) | The array of IpRouteEntry  ***Since:*** vSphere API 4.0  | [optional] 
**ipv6_route** | [**List[HostIpRouteEntry]**](HostIpRouteEntry.md) |  | [optional] 

## Example

```python
from vmware_vi.models.host_ip_route_table_info import HostIpRouteTableInfo

# TODO update the JSON string below
json = "{}"
# create an instance of HostIpRouteTableInfo from a JSON string
host_ip_route_table_info_instance = HostIpRouteTableInfo.from_json(json)
# print the JSON string representation of the object
print HostIpRouteTableInfo.to_json()

# convert the object into a dict
host_ip_route_table_info_dict = host_ip_route_table_info_instance.to_dict()
# create an instance of HostIpRouteTableInfo from a dict
host_ip_route_table_info_form_dict = host_ip_route_table_info.from_dict(host_ip_route_table_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


