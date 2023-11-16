# ArrayOfNetIpRouteConfigInfoGateway

A boxed array of *NetIpRouteConfigInfoGateway*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[NetIpRouteConfigInfoGateway]**](NetIpRouteConfigInfoGateway.md) |  | 

## Example

```python
from vmware_vi.models.array_of_net_ip_route_config_info_gateway import ArrayOfNetIpRouteConfigInfoGateway

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfNetIpRouteConfigInfoGateway from a JSON string
array_of_net_ip_route_config_info_gateway_instance = ArrayOfNetIpRouteConfigInfoGateway.from_json(json)
# print the JSON string representation of the object
print ArrayOfNetIpRouteConfigInfoGateway.to_json()

# convert the object into a dict
array_of_net_ip_route_config_info_gateway_dict = array_of_net_ip_route_config_info_gateway_instance.to_dict()
# create an instance of ArrayOfNetIpRouteConfigInfoGateway from a dict
array_of_net_ip_route_config_info_gateway_form_dict = array_of_net_ip_route_config_info_gateway.from_dict(array_of_net_ip_route_config_info_gateway_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


