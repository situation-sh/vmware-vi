# HostVirtualNicIpRouteSpec

The *HostVirtualNicIpRouteSpec* data object describes the IpRoute configuration used by virtual NIC.  ***Since:*** vSphere API 6.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ip_route_config** | [**HostIpRouteConfig**](HostIpRouteConfig.md) |  | [optional] 

## Example

```python
from vmware_vi.models.host_virtual_nic_ip_route_spec import HostVirtualNicIpRouteSpec

# TODO update the JSON string below
json = "{}"
# create an instance of HostVirtualNicIpRouteSpec from a JSON string
host_virtual_nic_ip_route_spec_instance = HostVirtualNicIpRouteSpec.from_json(json)
# print the JSON string representation of the object
print HostVirtualNicIpRouteSpec.to_json()

# convert the object into a dict
host_virtual_nic_ip_route_spec_dict = host_virtual_nic_ip_route_spec_instance.to_dict()
# create an instance of HostVirtualNicIpRouteSpec from a dict
host_virtual_nic_ip_route_spec_form_dict = host_virtual_nic_ip_route_spec.from_dict(host_virtual_nic_ip_route_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


