# NetIpRouteConfigInfoGateway

Next hop Gateway for a given route.  ***Since:*** vSphere API 4.1 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ip_address** | **str** |  | [optional] 
**device** | **str** |  | [optional] 

## Example

```python
from vmware_vi.models.net_ip_route_config_info_gateway import NetIpRouteConfigInfoGateway

# TODO update the JSON string below
json = "{}"
# create an instance of NetIpRouteConfigInfoGateway from a JSON string
net_ip_route_config_info_gateway_instance = NetIpRouteConfigInfoGateway.from_json(json)
# print the JSON string representation of the object
print NetIpRouteConfigInfoGateway.to_json()

# convert the object into a dict
net_ip_route_config_info_gateway_dict = net_ip_route_config_info_gateway_instance.to_dict()
# create an instance of NetIpRouteConfigInfoGateway from a dict
net_ip_route_config_info_gateway_form_dict = net_ip_route_config_info_gateway.from_dict(net_ip_route_config_info_gateway_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


