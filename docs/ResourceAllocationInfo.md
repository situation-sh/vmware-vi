# ResourceAllocationInfo

The ResourceAllocationInfo data object specifies the reserved resource requirement as well as the limit (maximum allowed usage) for a given kind of resource.  This is specified for both memory allocation (specified in MB) and CPU allocation (specified in MHz).  For a *ResourcePool*, the ResourceAllocationInfo object describes both the guaranteed amount of the resource (*ResourceAllocationInfo.reservation*) and whether or not it is expandable (*ResourceAllocationInfo.expandableReservation*). If expandableReservation is true, then the resource pool can grow its reservation dynamically by borrowing unreserved resources from its parent resource pool. For the methods *ResourcePool.CreateResourcePool*, *ResourcePool.CreateVApp* and *ResourcePool.ImportVApp*, you must provide values for all properties except overheadLimit; they are not optional. (Currently, overheadLimit is for vCenter Server use only.)  If the limit is configured, it must be greater than or equal to the reservation. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reservation** | **int** | Amount of resource that is guaranteed available to the virtual machine or resource pool.  Reserved resources are not wasted if they are not used. If the utilization is less than the reservation, the resources can be utilized by other running virtual machines. Units are MB for memory, MHz for CPU.  | [optional] 
**expandable_reservation** | **bool** | In a resource pool with an expandable reservation, the reservation on a resource pool can grow beyond the specified value, if the parent resource pool has unreserved resources.  A non-expandable reservation is called a fixed reservation. This property is invalid for virtual machines.  | [optional] 
**limit** | **int** | The utilization of a virtual machine/resource pool will not exceed this limit, even if there are available resources.  This is typically used to ensure a consistent performance of virtual machines / resource pools independent of available resources. If set to -1, then there is no fixed limit on resource usage (only bounded by available resources and shares). Units are MB for memory, MHz for CPU.  | [optional] 
**shares** | [**SharesInfo**](SharesInfo.md) |  | [optional] 
**overhead_limit** | **int** | The maximum allowed overhead memory.  For a powered on virtual machine, the overhead memory reservation cannot be larger than its overheadLimit. This property is only applicable to powered on virtual machines and is not persisted across reboots. This property is not applicable for resource pools. If set to -1, then there is no limit on reservation. Units are MB.  Note: For vCenter Server use only. Not available for other clients at this time. The server will throw an exception if you attempt to set this property.  ***Since:*** VI API 2.5  | [optional] 

## Example

```python
from vmware_vi.models.resource_allocation_info import ResourceAllocationInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceAllocationInfo from a JSON string
resource_allocation_info_instance = ResourceAllocationInfo.from_json(json)
# print the JSON string representation of the object
print ResourceAllocationInfo.to_json()

# convert the object into a dict
resource_allocation_info_dict = resource_allocation_info_instance.to_dict()
# create an instance of ResourceAllocationInfo from a dict
resource_allocation_info_form_dict = resource_allocation_info.from_dict(resource_allocation_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


