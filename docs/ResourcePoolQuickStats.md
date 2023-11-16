# ResourcePoolQuickStats

A set of statistics that are typically updated with near real-time regularity.  These statistics are aggregates of the corresponding statistics of all virtual machines in the given resource pool, and unless otherwise noted, only make sense when at least one virtual machine in the given resource pool is powered on. This data object type does not support notification, for scalability reasons. Therefore, changes in QuickStats do not generate property collector updates. To monitor statistics values, use the statistics and alarms modules instead.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**overall_cpu_usage** | **int** | Basic CPU performance statistics, in MHz.  ***Since:*** vSphere API 4.0  | [optional] 
**overall_cpu_demand** | **int** | Basic CPU performance statistics, in MHz.  ***Since:*** vSphere API 4.0  | [optional] 
**guest_memory_usage** | **int** | Guest memory utilization statistics, in MB.  This is also known as active guest memory. The number can be between 0 and the configured memory size of a virtual machine.  ***Since:*** vSphere API 4.0  | [optional] 
**host_memory_usage** | **int** | Host memory utilization statistics, in MB.  This is also known as consummed host memory. This is between 0 and the configured resource limit. Valid while a virtual machine is running. This includes the overhead memory of a virtual machine.  ***Since:*** vSphere API 4.0  | [optional] 
**distributed_cpu_entitlement** | **int** | This is the amount of CPU resource, in MHz, that this VM is entitled to, as calculated by DRS.  Valid only for a VM managed by DRS.  ***Since:*** vSphere API 4.0  | [optional] 
**distributed_memory_entitlement** | **int** | This is the amount of memory, in MB, that this VM is entitled to, as calculated by DRS.  Valid only for a VM managed by DRS.  ***Since:*** vSphere API 4.0  | [optional] 
**static_cpu_entitlement** | **int** | The static CPU resource entitlement for a virtual machine.  This value is calculated based on this virtual machine&#39;s resource reservations, shares and limit, and doesn&#39;t take into account current usage. This is the worst case CPU allocation for this virtual machine, that is, the amount of CPU resource this virtual machine would receive if all virtual machines running in the cluster went to maximum consumption. Units are MHz.  ***Since:*** vSphere API 4.0  | [optional] 
**static_memory_entitlement** | **int** | The static memory resource entitlement for a virtual machine.  This value is calculated based on this virtual machine&#39;s resource reservations, shares and limit, and doesn&#39;t take into account current usage. This is the worst case memory allocation for this virtual machine, that is, the amount of memory this virtual machine would receive if all virtual machines running in the cluster went to maximum consumption. Units are MB.  ***Since:*** vSphere API 4.0  | [optional] 
**private_memory** | **int** | The portion of memory, in MB, that is granted to a virtual machine from non-shared host memory.  ***Since:*** vSphere API 4.0  | [optional] 
**shared_memory** | **int** | The portion of memory, in MB, that is granted to a virtual machine from host memory that is shared between VMs.  ***Since:*** vSphere API 4.0  | [optional] 
**swapped_memory** | **int** | The portion of memory, in MB, that is granted to a virtual machine from the host&#39;s swap space.  This is a sign that there is memory pressure on the host.  ***Since:*** vSphere API 4.0  | [optional] 
**ballooned_memory** | **int** | The size of the balloon driver in a virtual machine, in MB.  The host will inflate the balloon driver to reclaim physical memory from a virtual machine. This is a sign that there is memory pressure on the host.  ***Since:*** vSphere API 4.0  | [optional] 
**overhead_memory** | **int** | The amount of memory resource (in MB) that will be used by a virtual machine above its guest memory requirements.  This value is set if and only if a virtual machine is registered on a host that supports memory resource allocation features. For powered off VMs, this is the minimum overhead required to power on the VM on the registered host. For powered on VMs, this is the current overhead reservation, a value which is almost always larger than the minimum overhead, and which grows with time.  See also *HostSystem.QueryMemoryOverheadEx*.  ***Since:*** vSphere API 4.0  | [optional] 
**consumed_overhead_memory** | **int** | The amount of overhead memory, in MB, currently being consumed to run a VM.  This value is limited by the overhead memory reservation for a VM, stored in *ResourcePoolQuickStats.overheadMemory*.  ***Since:*** vSphere API 4.0  | [optional] 
**compressed_memory** | **int** | The amount of compressed memory currently consumed by VM, in KB.  ***Since:*** vSphere API 4.1  | [optional] 

## Example

```python
from vmware_vi.models.resource_pool_quick_stats import ResourcePoolQuickStats

# TODO update the JSON string below
json = "{}"
# create an instance of ResourcePoolQuickStats from a JSON string
resource_pool_quick_stats_instance = ResourcePoolQuickStats.from_json(json)
# print the JSON string representation of the object
print ResourcePoolQuickStats.to_json()

# convert the object into a dict
resource_pool_quick_stats_dict = resource_pool_quick_stats_instance.to_dict()
# create an instance of ResourcePoolQuickStats from a dict
resource_pool_quick_stats_form_dict = resource_pool_quick_stats.from_dict(resource_pool_quick_stats_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


