# NetIpRouteConfigSpec

Address family independent IP Route Table Configuration data object.  ***Since:*** vSphere API 4.1 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ip_route** | [**List[NetIpRouteConfigSpecIpRouteSpec]**](NetIpRouteConfigSpecIpRouteSpec.md) | The set of updates to apply to the routing table.  ***Since:*** vSphere API 4.1  | [optional] 

## Example

```python
from vmware_vi.models.net_ip_route_config_spec import NetIpRouteConfigSpec

# TODO update the JSON string below
json = "{}"
# create an instance of NetIpRouteConfigSpec from a JSON string
net_ip_route_config_spec_instance = NetIpRouteConfigSpec.from_json(json)
# print the JSON string representation of the object
print NetIpRouteConfigSpec.to_json()

# convert the object into a dict
net_ip_route_config_spec_dict = net_ip_route_config_spec_instance.to_dict()
# create an instance of NetIpRouteConfigSpec from a dict
net_ip_route_config_spec_form_dict = net_ip_route_config_spec.from_dict(net_ip_route_config_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


