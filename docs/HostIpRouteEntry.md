# HostIpRouteEntry

IpRouteEntry.  Routing entries are individual static routes which combined with the default route form all of the routing rules for a host.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**network** | **str** | Network of the routing entry Of the format \&quot;10.20.120.0\&quot; or \&quot;2001:db8::1428:57\&quot;  ***Since:*** vSphere API 4.0  | 
**prefix_length** | **int** | Prefix length of the network (this is the 22 in 10.20.120.0/22)  ***Since:*** vSphere API 4.0  | 
**gateway** | **str** | Gateway for the routing entry  ***Since:*** vSphere API 4.0  | 
**device_name** | **str** | If available the property indicates the device associated with the routing entry.  This property can only be read from the server. It will be ignored if set by the client.  ***Since:*** vSphere API 4.1  | [optional] 

## Example

```python
from vmware_vi.models.host_ip_route_entry import HostIpRouteEntry

# TODO update the JSON string below
json = "{}"
# create an instance of HostIpRouteEntry from a JSON string
host_ip_route_entry_instance = HostIpRouteEntry.from_json(json)
# print the JSON string representation of the object
print HostIpRouteEntry.to_json()

# convert the object into a dict
host_ip_route_entry_dict = host_ip_route_entry_instance.to_dict()
# create an instance of HostIpRouteEntry from a dict
host_ip_route_entry_form_dict = host_ip_route_entry.from_dict(host_ip_route_entry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


