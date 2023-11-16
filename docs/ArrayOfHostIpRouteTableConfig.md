# ArrayOfHostIpRouteTableConfig

A boxed array of *HostIpRouteTableConfig*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[HostIpRouteTableConfig]**](HostIpRouteTableConfig.md) |  | 

## Example

```python
from vmware_vi.models.array_of_host_ip_route_table_config import ArrayOfHostIpRouteTableConfig

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfHostIpRouteTableConfig from a JSON string
array_of_host_ip_route_table_config_instance = ArrayOfHostIpRouteTableConfig.from_json(json)
# print the JSON string representation of the object
print ArrayOfHostIpRouteTableConfig.to_json()

# convert the object into a dict
array_of_host_ip_route_table_config_dict = array_of_host_ip_route_table_config_instance.to_dict()
# create an instance of ArrayOfHostIpRouteTableConfig from a dict
array_of_host_ip_route_table_config_form_dict = array_of_host_ip_route_table_config.from_dict(array_of_host_ip_route_table_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


