# HostNetStackInstance

This class describes Network Stack Instance configuration  ***Since:*** vSphere API 5.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | Key of instance For instance which created by host, its value should be *HostNetStackInstanceSystemStackKey_enum*.  ***Since:*** vSphere API 5.5  | [optional] 
**name** | **str** | The display name  ***Since:*** vSphere API 5.5  | [optional] 
**dns_config** | [**HostDnsConfig**](HostDnsConfig.md) |  | [optional] 
**ip_route_config** | [**HostIpRouteConfig**](HostIpRouteConfig.md) |  | [optional] 
**requested_max_number_of_connections** | **int** | The maximum number of socket connection that are requested on this instance  ***Since:*** vSphere API 5.5  | [optional] 
**congestion_control_algorithm** | **str** | The TCP congest control algorithm used by this instance, See *HostNetStackInstanceCongestionControlAlgorithmType_enum* for valid values.  ***Since:*** vSphere API 5.5  | [optional] 
**ip_v6_enabled** | **bool** | Enable or disable IPv6 protocol on this stack instance.  This property is not supported currently.  ***Since:*** vSphere API 5.5  | [optional] 
**route_table_config** | [**HostIpRouteTableConfig**](HostIpRouteTableConfig.md) |  | [optional] 

## Example

```python
from vmware_vi.models.host_net_stack_instance import HostNetStackInstance

# TODO update the JSON string below
json = "{}"
# create an instance of HostNetStackInstance from a JSON string
host_net_stack_instance_instance = HostNetStackInstance.from_json(json)
# print the JSON string representation of the object
print HostNetStackInstance.to_json()

# convert the object into a dict
host_net_stack_instance_dict = host_net_stack_instance_instance.to_dict()
# create an instance of HostNetStackInstance from a dict
host_net_stack_instance_form_dict = host_net_stack_instance.from_dict(host_net_stack_instance_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


