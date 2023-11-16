# ArrayOfHostIpRouteConfig

A boxed array of *HostIpRouteConfig*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[HostIpRouteConfig]**](HostIpRouteConfig.md) |  | 

## Example

```python
from vmware_vi.models.array_of_host_ip_route_config import ArrayOfHostIpRouteConfig

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfHostIpRouteConfig from a JSON string
array_of_host_ip_route_config_instance = ArrayOfHostIpRouteConfig.from_json(json)
# print the JSON string representation of the object
print ArrayOfHostIpRouteConfig.to_json()

# convert the object into a dict
array_of_host_ip_route_config_dict = array_of_host_ip_route_config_instance.to_dict()
# create an instance of ArrayOfHostIpRouteConfig from a dict
array_of_host_ip_route_config_form_dict = array_of_host_ip_route_config.from_dict(array_of_host_ip_route_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


