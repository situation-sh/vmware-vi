# ResourcePoolResourceUsage

Specifies the resource usage for either memory or CPU.  For CPU the unit is MHz, for memory the unit is bytes.  In the typical case, where a resourcepool is in a consistent state, unreservedForVm will be equal to unreservedForPool. Hence, we can simply say talk about unreserved resources.  If the reservation on the resource pool is not expandable, then the following is true:                 reservation = reservationUsed + unreserved If the reservation on the resource pool is expandable, then the following is true:            reservation + parent.unreserved = reservationUsed + unreserved 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reservation_used** | **int** | Total amount of resources that have been used to satisfy the reservation requirements of all descendants of this resource pool (includes both resource pools and virtual machines).  | 
**reservation_used_for_vm** | **int** | Total amount of resources that have been used to satisfy the reservation requirements of running virtual machines in this resource pool or any of its child resource pools.  | 
**unreserved_for_pool** | **int** | Total amount of resources available to satisfy a reservation for a child resource pool.  In the undercommitted state, this is limited by the capacity at the root node. In the overcommitted case, this could be higher since we do not perform the dynamic capacity checks.  | 
**unreserved_for_vm** | **int** | Total amount of resources available to satisfy a reservation for a child virtual machine.  In general, this should be the same as *ResourcePoolResourceUsage.unreservedForPool*. However, in the overcommitted case, this is limited by the remaining available resources at the root node.  | 
**overall_usage** | **int** | Deprecated as of vSphere API 6.5. Use *ResourcePoolQuickStats.overallCpuUsage* and *ResourcePoolQuickStats.hostMemoryUsage*.  Close to real-time resource usage of all running child virtual machines, including virtual machines in child resource pools.  | 
**max_usage** | **int** | Current upper-bound on usage.  The upper-bound is based on the limit configured on this resource pool, as well as limits configured on any parent resource pool.  | 

## Example

```python
from vmware_vi.models.resource_pool_resource_usage import ResourcePoolResourceUsage

# TODO update the JSON string below
json = "{}"
# create an instance of ResourcePoolResourceUsage from a JSON string
resource_pool_resource_usage_instance = ResourcePoolResourceUsage.from_json(json)
# print the JSON string representation of the object
print ResourcePoolResourceUsage.to_json()

# convert the object into a dict
resource_pool_resource_usage_dict = resource_pool_resource_usage_instance.to_dict()
# create an instance of ResourcePoolResourceUsage from a dict
resource_pool_resource_usage_form_dict = resource_pool_resource_usage.from_dict(resource_pool_resource_usage_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


