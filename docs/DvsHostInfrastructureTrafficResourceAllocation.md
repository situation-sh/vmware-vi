# DvsHostInfrastructureTrafficResourceAllocation

Resource allocation information for a host infrastructure traffic class.  ***Since:*** vSphere API 6.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**limit** | **int** | The maximum allowed usage for a traffic class belonging to this resource pool per host physical NIC.  The utilization of a traffic class will not exceed the specified limit even if there are available network resources. If this value is unset or set to -1 in an update operation, then there is no limit on the network resource usage (only bounded by available resource and shares). Units are in Mbits/sec.  ***Since:*** vSphere API 6.0  | [optional] 
**shares** | [**SharesInfo**](SharesInfo.md) |  | [optional] 
**reservation** | **int** | Amount of bandwidth resource that is guaranteed available to the host infrastructure traffic class.  If the utilization is less than the reservation, the extra bandwidth is used for other host infrastructure traffic class types. Reservation is not allowed to exceed the value of *DvsHostInfrastructureTrafficResourceAllocation.limit*, if *DvsHostInfrastructureTrafficResourceAllocation.limit* is set. Unit is Mbits/sec.  ***Since:*** vSphere API 6.0  | [optional] 

## Example

```python
from vmware_vi.models.dvs_host_infrastructure_traffic_resource_allocation import DvsHostInfrastructureTrafficResourceAllocation

# TODO update the JSON string below
json = "{}"
# create an instance of DvsHostInfrastructureTrafficResourceAllocation from a JSON string
dvs_host_infrastructure_traffic_resource_allocation_instance = DvsHostInfrastructureTrafficResourceAllocation.from_json(json)
# print the JSON string representation of the object
print DvsHostInfrastructureTrafficResourceAllocation.to_json()

# convert the object into a dict
dvs_host_infrastructure_traffic_resource_allocation_dict = dvs_host_infrastructure_traffic_resource_allocation_instance.to_dict()
# create an instance of DvsHostInfrastructureTrafficResourceAllocation from a dict
dvs_host_infrastructure_traffic_resource_allocation_form_dict = dvs_host_infrastructure_traffic_resource_allocation.from_dict(dvs_host_infrastructure_traffic_resource_allocation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


