# NetIpRouteConfigInfo

This data object reports the IP Route Table.  ***Since:*** vSphere API 4.1 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ip_route** | [**List[NetIpRouteConfigInfoIpRoute]**](NetIpRouteConfigInfoIpRoute.md) | IP routing table for all address families.  ***Since:*** vSphere API 4.1  | [optional] 

## Example

```python
from vmware_vi.models.net_ip_route_config_info import NetIpRouteConfigInfo

# TODO update the JSON string below
json = "{}"
# create an instance of NetIpRouteConfigInfo from a JSON string
net_ip_route_config_info_instance = NetIpRouteConfigInfo.from_json(json)
# print the JSON string representation of the object
print NetIpRouteConfigInfo.to_json()

# convert the object into a dict
net_ip_route_config_info_dict = net_ip_route_config_info_instance.to_dict()
# create an instance of NetIpRouteConfigInfo from a dict
net_ip_route_config_info_form_dict = net_ip_route_config_info.from_dict(net_ip_route_config_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


