# DvsHostInfrastructureTrafficResource

This class defines the resource allocation for a host infrastructure traffic class on a physical NIC  ***Since:*** vSphere API 6.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | The key of the host infrastructure resource.  Possible value can be of *DistributedVirtualSwitchHostInfrastructureTrafficClass_enum*.  ***Since:*** vSphere API 6.0  | 
**description** | **str** | The description of the host infrastructure resource.  This property is ignored for update operation.  ***Since:*** vSphere API 6.0  | [optional] 
**allocation_info** | [**DvsHostInfrastructureTrafficResourceAllocation**](DvsHostInfrastructureTrafficResourceAllocation.md) |  | 

## Example

```python
from vmware_vi.models.dvs_host_infrastructure_traffic_resource import DvsHostInfrastructureTrafficResource

# TODO update the JSON string below
json = "{}"
# create an instance of DvsHostInfrastructureTrafficResource from a JSON string
dvs_host_infrastructure_traffic_resource_instance = DvsHostInfrastructureTrafficResource.from_json(json)
# print the JSON string representation of the object
print DvsHostInfrastructureTrafficResource.to_json()

# convert the object into a dict
dvs_host_infrastructure_traffic_resource_dict = dvs_host_infrastructure_traffic_resource_instance.to_dict()
# create an instance of DvsHostInfrastructureTrafficResource from a dict
dvs_host_infrastructure_traffic_resource_form_dict = dvs_host_infrastructure_traffic_resource.from_dict(dvs_host_infrastructure_traffic_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


