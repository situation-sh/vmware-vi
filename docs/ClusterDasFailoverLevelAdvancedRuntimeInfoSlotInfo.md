# ClusterDasFailoverLevelAdvancedRuntimeInfoSlotInfo

A slot represents an amount of memory and cpu resources on a physical host for use by a virtual machine.  It is used in computing the resources to be reserved for failover.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**num_vcpus** | **int** | Deprecated as of vSphere API 5.0, the number of vcpus is no longer used for slot calculations.  The number of virtual cpus of a slot is defined as the maximum number of virtual cpus any powered on virtual machine has.  ***Since:*** vSphere API 4.0  | 
**cpu_mhz** | **int** | The cpu speed of a slot is defined as the maximum cpu reservation of any powered on virtual machine in the cluster, or any otherwise defined minimum, whichever is larger.  ***Since:*** vSphere API 4.0  | 
**memory_mb** | **int** | The memory size of a slot is defined as the maximum memory reservation plus memory overhead of any powered on virtual machine in the cluster, or any otherwise defined minimum, whichever is larger.  ***Since:*** vSphere API 4.0  | 

## Example

```python
from vmware_vi.models.cluster_das_failover_level_advanced_runtime_info_slot_info import ClusterDasFailoverLevelAdvancedRuntimeInfoSlotInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterDasFailoverLevelAdvancedRuntimeInfoSlotInfo from a JSON string
cluster_das_failover_level_advanced_runtime_info_slot_info_instance = ClusterDasFailoverLevelAdvancedRuntimeInfoSlotInfo.from_json(json)
# print the JSON string representation of the object
print ClusterDasFailoverLevelAdvancedRuntimeInfoSlotInfo.to_json()

# convert the object into a dict
cluster_das_failover_level_advanced_runtime_info_slot_info_dict = cluster_das_failover_level_advanced_runtime_info_slot_info_instance.to_dict()
# create an instance of ClusterDasFailoverLevelAdvancedRuntimeInfoSlotInfo from a dict
cluster_das_failover_level_advanced_runtime_info_slot_info_form_dict = cluster_das_failover_level_advanced_runtime_info_slot_info.from_dict(cluster_das_failover_level_advanced_runtime_info_slot_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


