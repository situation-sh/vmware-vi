# HostIpRouteOp

Routing Entry Operation.  Routing entries are individual static routes which combined with the default route form all of the routing rules for a host.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**change_operation** | **str** | This property indicates the change operation to apply on this configuration specification.  See also *HostConfigChangeOperation_enum*.  ***Since:*** vSphere API 4.0  | 
**route** | [**HostIpRouteEntry**](HostIpRouteEntry.md) |  | 

## Example

```python
from vmware_vi.models.host_ip_route_op import HostIpRouteOp

# TODO update the JSON string below
json = "{}"
# create an instance of HostIpRouteOp from a JSON string
host_ip_route_op_instance = HostIpRouteOp.from_json(json)
# print the JSON string representation of the object
print HostIpRouteOp.to_json()

# convert the object into a dict
host_ip_route_op_dict = host_ip_route_op_instance.to_dict()
# create an instance of HostIpRouteOp from a dict
host_ip_route_op_form_dict = host_ip_route_op.from_dict(host_ip_route_op_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


