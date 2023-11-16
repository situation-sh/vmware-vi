# ArrayOfNetIpRouteConfigSpecGatewaySpec

A boxed array of *NetIpRouteConfigSpecGatewaySpec*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[NetIpRouteConfigSpecGatewaySpec]**](NetIpRouteConfigSpecGatewaySpec.md) |  | 

## Example

```python
from vmware_vi.models.array_of_net_ip_route_config_spec_gateway_spec import ArrayOfNetIpRouteConfigSpecGatewaySpec

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfNetIpRouteConfigSpecGatewaySpec from a JSON string
array_of_net_ip_route_config_spec_gateway_spec_instance = ArrayOfNetIpRouteConfigSpecGatewaySpec.from_json(json)
# print the JSON string representation of the object
print ArrayOfNetIpRouteConfigSpecGatewaySpec.to_json()

# convert the object into a dict
array_of_net_ip_route_config_spec_gateway_spec_dict = array_of_net_ip_route_config_spec_gateway_spec_instance.to_dict()
# create an instance of ArrayOfNetIpRouteConfigSpecGatewaySpec from a dict
array_of_net_ip_route_config_spec_gateway_spec_form_dict = array_of_net_ip_route_config_spec_gateway_spec.from_dict(array_of_net_ip_route_config_spec_gateway_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


