# ArrayOfNetIpRouteConfigSpecIpRouteSpec

A boxed array of *NetIpRouteConfigSpecIpRouteSpec*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[NetIpRouteConfigSpecIpRouteSpec]**](NetIpRouteConfigSpecIpRouteSpec.md) |  | 

## Example

```python
from vmware_vi.models.array_of_net_ip_route_config_spec_ip_route_spec import ArrayOfNetIpRouteConfigSpecIpRouteSpec

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfNetIpRouteConfigSpecIpRouteSpec from a JSON string
array_of_net_ip_route_config_spec_ip_route_spec_instance = ArrayOfNetIpRouteConfigSpecIpRouteSpec.from_json(json)
# print the JSON string representation of the object
print ArrayOfNetIpRouteConfigSpecIpRouteSpec.to_json()

# convert the object into a dict
array_of_net_ip_route_config_spec_ip_route_spec_dict = array_of_net_ip_route_config_spec_ip_route_spec_instance.to_dict()
# create an instance of ArrayOfNetIpRouteConfigSpecIpRouteSpec from a dict
array_of_net_ip_route_config_spec_ip_route_spec_form_dict = array_of_net_ip_route_config_spec_ip_route_spec.from_dict(array_of_net_ip_route_config_spec_ip_route_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


