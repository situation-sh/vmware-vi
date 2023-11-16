# VirtualMachineQuickStats

A set of statistics that are typically updated with near real-time regularity.  This data object type does not support notification, for scalability reasons. Therefore, changes in QuickStats do not generate property collector updates. To monitor statistics values, use the statistics and alarms modules instead. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**overall_cpu_usage** | **int** | Basic CPU performance statistics, in MHz.  Valid while the virtual machine is running.  | [optional] 
**overall_cpu_demand** | **int** | Basic CPU performance statistics, in MHz.  Valid while the virtual machine is running.  ***Since:*** vSphere API 4.0  | [optional] 
**overall_cpu_readiness** | **int** | Percentage of time that the virtual machine was ready, but could not get scheduled to run on the physical CPU.  Valid while the virtual machine is running.  ***Since:*** vSphere API 7.0  | [optional] 
**guest_memory_usage** | **int** | Guest memory utilization statistics, in MB.  This is also known as active guest memory. The number can be between 0 and the configured memory size of the virtual machine. Valid while the virtual machine is running.  | [optional] 
**host_memory_usage** | **int** | Host memory utilization statistics, in MB.  This is also known as consumed host memory. This is between 0 and the configured resource limit. Valid while the virtual machine is running. This includes the overhead memory of the VM.  | [optional] 
**guest_heartbeat_status** | [**ManagedEntityStatusEnum**](ManagedEntityStatusEnum.md) |  | 
**distributed_cpu_entitlement** | **int** | This is the amount of CPU resource, in MHz, that this VM is entitled to, as calculated by DRS.  Valid only for a VM managed by DRS.  | [optional] 
**distributed_memory_entitlement** | **int** | This is the amount of memory, in MB, that this VM is entitled to, as calculated by DRS.  Valid only for a VM managed by DRS.  | [optional] 
**static_cpu_entitlement** | **int** | The static CPU resource entitlement for a virtual machine.  This value is calculated based on this virtual machine&#39;s resource reservations, shares and limit, and doesn&#39;t take into account current usage. This is the worst case CPU allocation for this virtual machine, that is, the amount of CPU resource this virtual machine would receive if all virtual machines running in the cluster went to maximum consumption. Units are MHz.  ***Since:*** vSphere API 4.0  | [optional] 
**static_memory_entitlement** | **int** | The static memory resource entitlement for a virtual machine.  This value is calculated based on this virtual machine&#39;s resource reservations, shares and limit, and doesn&#39;t take into account current usage. This is the worst case memory allocation for this virtual machine, that is, the amount of memory this virtual machine would receive if all virtual machines running in the cluster went to maximum consumption. Units are MB.  ***Since:*** vSphere API 4.0  | [optional] 
**granted_memory** | **int** | Amount of host physical memory that is mapped for a virtual machine, in MB.  The number can be between 0 and the configured memory size of the virtual machine. Valid while the virtual machine is running.  ***Since:*** vSphere API 7.0  | [optional] 
**private_memory** | **int** | The portion of memory, in MB, that is granted to this VM from non-shared host memory.  ***Since:*** vSphere API 4.0  | [optional] 
**shared_memory** | **int** | The portion of memory, in MB, that is granted to this VM from host memory that is shared between VMs.  ***Since:*** vSphere API 4.0  | [optional] 
**swapped_memory** | **int** | The portion of memory, in MB, that is granted to this VM from the host&#39;s swap space.  This is a sign that there is memory pressure on the host.  ***Since:*** vSphere API 4.0  | [optional] 
**ballooned_memory** | **int** | The size of the balloon driver in the VM, in MB.  The host will inflate the balloon driver to reclaim physical memory from the VM. This is a sign that there is memory pressure on the host.  ***Since:*** vSphere API 4.0  | [optional] 
**consumed_overhead_memory** | **int** | The amount of consumed overhead memory, in MB, for this VM.  ***Since:*** vSphere API 4.0  | [optional] 
**ft_log_bandwidth** | **int** | The network bandwidth used for logging between the primary and secondary fault tolerance VMs.  The unit is kilobytes per second.  ***Since:*** vSphere API 4.0  | [optional] 
**ft_secondary_latency** | **int** | The amount of time in wallclock that the VCPU of the secondary fault tolerance VM is behind the VCPU of the primary VM.  The unit is millisecond.  ***Since:*** vSphere API 4.0  | [optional] 
**ft_latency_status** | [**ManagedEntityStatusEnum**](ManagedEntityStatusEnum.md) |  | [optional] 
**compressed_memory** | **int** | The amount of compressed memory currently consumed by VM, in Kb.  ***Since:*** vSphere API 4.1  | [optional] 
**uptime_seconds** | **int** | The system uptime of the VM in seconds.  ***Since:*** vSphere API 4.1  | [optional] 
**ssd_swapped_memory** | **int** | The amount of memory swapped to fast disk device such as SSD, in KB.  ***Since:*** vSphere API 5.0  | [optional] 
**active_memory** | **int** | The amount of memory that was recently touched by the VM, in MB.  ***Since:*** vSphere API 7.0.3.0  | [optional] 
**memory_tier_stats** | [**List[VirtualMachineQuickStatsMemoryTierStats]**](VirtualMachineQuickStatsMemoryTierStats.md) | Stats for each physical memory tier.  A physical memory tier consists of one or more logical memory tiers of the same *HostMemoryTierType_enum*. For example, the logical tiers can be tier0 (DRAM), tier1 (DRAM), and tier2 (PMEM), while the physical tiers are just DRAM and PMEM.  ***Since:*** vSphere API 7.0.3.0  | [optional] 

## Example

```python
from vmware_vi.models.virtual_machine_quick_stats import VirtualMachineQuickStats

# TODO update the JSON string below
json = "{}"
# create an instance of VirtualMachineQuickStats from a JSON string
virtual_machine_quick_stats_instance = VirtualMachineQuickStats.from_json(json)
# print the JSON string representation of the object
print VirtualMachineQuickStats.to_json()

# convert the object into a dict
virtual_machine_quick_stats_dict = virtual_machine_quick_stats_instance.to_dict()
# create an instance of VirtualMachineQuickStats from a dict
virtual_machine_quick_stats_form_dict = virtual_machine_quick_stats.from_dict(virtual_machine_quick_stats_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


