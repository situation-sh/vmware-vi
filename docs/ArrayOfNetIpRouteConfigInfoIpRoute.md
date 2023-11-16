# ArrayOfNetIpRouteConfigInfoIpRoute

A boxed array of *NetIpRouteConfigInfoIpRoute*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[NetIpRouteConfigInfoIpRoute]**](NetIpRouteConfigInfoIpRoute.md) |  | 

## Example

```python
from vmware_vi.models.array_of_net_ip_route_config_info_ip_route import ArrayOfNetIpRouteConfigInfoIpRoute

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfNetIpRouteConfigInfoIpRoute from a JSON string
array_of_net_ip_route_config_info_ip_route_instance = ArrayOfNetIpRouteConfigInfoIpRoute.from_json(json)
# print the JSON string representation of the object
print ArrayOfNetIpRouteConfigInfoIpRoute.to_json()

# convert the object into a dict
array_of_net_ip_route_config_info_ip_route_dict = array_of_net_ip_route_config_info_ip_route_instance.to_dict()
# create an instance of ArrayOfNetIpRouteConfigInfoIpRoute from a dict
array_of_net_ip_route_config_info_ip_route_form_dict = array_of_net_ip_route_config_info_ip_route.from_dict(array_of_net_ip_route_config_info_ip_route_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


