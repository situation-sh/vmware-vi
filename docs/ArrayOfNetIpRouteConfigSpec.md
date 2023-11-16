# ArrayOfNetIpRouteConfigSpec

A boxed array of *NetIpRouteConfigSpec*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[NetIpRouteConfigSpec]**](NetIpRouteConfigSpec.md) |  | 

## Example

```python
from vmware_vi.models.array_of_net_ip_route_config_spec import ArrayOfNetIpRouteConfigSpec

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfNetIpRouteConfigSpec from a JSON string
array_of_net_ip_route_config_spec_instance = ArrayOfNetIpRouteConfigSpec.from_json(json)
# print the JSON string representation of the object
print ArrayOfNetIpRouteConfigSpec.to_json()

# convert the object into a dict
array_of_net_ip_route_config_spec_dict = array_of_net_ip_route_config_spec_instance.to_dict()
# create an instance of ArrayOfNetIpRouteConfigSpec from a dict
array_of_net_ip_route_config_spec_form_dict = array_of_net_ip_route_config_spec.from_dict(array_of_net_ip_route_config_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


