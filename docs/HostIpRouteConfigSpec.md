# HostIpRouteConfigSpec

Dataobject specifying the configuration for IpRoute  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gateway_device_connection** | [**HostVirtualNicConnection**](HostVirtualNicConnection.md) |  | [optional] 
**ip_v6_gateway_device_connection** | [**HostVirtualNicConnection**](HostVirtualNicConnection.md) |  | [optional] 

## Example

```python
from vmware_vi.models.host_ip_route_config_spec import HostIpRouteConfigSpec

# TODO update the JSON string below
json = "{}"
# create an instance of HostIpRouteConfigSpec from a JSON string
host_ip_route_config_spec_instance = HostIpRouteConfigSpec.from_json(json)
# print the JSON string representation of the object
print HostIpRouteConfigSpec.to_json()

# convert the object into a dict
host_ip_route_config_spec_dict = host_ip_route_config_spec_instance.to_dict()
# create an instance of HostIpRouteConfigSpec from a dict
host_ip_route_config_spec_form_dict = host_ip_route_config_spec.from_dict(host_ip_route_config_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


