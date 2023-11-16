# VirtualMachineQuickStatsMemoryTierStats


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**memory_tier_type** | **str** | The memory tier type.  See *HostMemoryTierType_enum* for supported values.  ***Since:*** vSphere API 7.0.3.0  | 
**read_bandwidth** | **int** | Memory access bandwidth usage for the reads of the VM on this tier in MBps.  ***Since:*** vSphere API 7.0.3.0  | 

## Example

```python
from vmware_vi.models.virtual_machine_quick_stats_memory_tier_stats import VirtualMachineQuickStatsMemoryTierStats

# TODO update the JSON string below
json = "{}"
# create an instance of VirtualMachineQuickStatsMemoryTierStats from a JSON string
virtual_machine_quick_stats_memory_tier_stats_instance = VirtualMachineQuickStatsMemoryTierStats.from_json(json)
# print the JSON string representation of the object
print VirtualMachineQuickStatsMemoryTierStats.to_json()

# convert the object into a dict
virtual_machine_quick_stats_memory_tier_stats_dict = virtual_machine_quick_stats_memory_tier_stats_instance.to_dict()
# create an instance of VirtualMachineQuickStatsMemoryTierStats from a dict
virtual_machine_quick_stats_memory_tier_stats_form_dict = virtual_machine_quick_stats_memory_tier_stats.from_dict(virtual_machine_quick_stats_memory_tier_stats_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


