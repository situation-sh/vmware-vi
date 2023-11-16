# NetIpRouteConfigSpecGatewaySpec

IpRoute report an individual host, network or default destination network reachable through a given gateway.  ***Since:*** vSphere API 4.1 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ip_address** | **str** |  | [optional] 
**device** | **str** |  | [optional] 

## Example

```python
from vmware_vi.models.net_ip_route_config_spec_gateway_spec import NetIpRouteConfigSpecGatewaySpec

# TODO update the JSON string below
json = "{}"
# create an instance of NetIpRouteConfigSpecGatewaySpec from a JSON string
net_ip_route_config_spec_gateway_spec_instance = NetIpRouteConfigSpecGatewaySpec.from_json(json)
# print the JSON string representation of the object
print NetIpRouteConfigSpecGatewaySpec.to_json()

# convert the object into a dict
net_ip_route_config_spec_gateway_spec_dict = net_ip_route_config_spec_gateway_spec_instance.to_dict()
# create an instance of NetIpRouteConfigSpecGatewaySpec from a dict
net_ip_route_config_spec_gateway_spec_form_dict = net_ip_route_config_spec_gateway_spec.from_dict(net_ip_route_config_spec_gateway_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


