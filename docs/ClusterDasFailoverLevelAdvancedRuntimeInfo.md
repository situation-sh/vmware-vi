# ClusterDasFailoverLevelAdvancedRuntimeInfo

Advanced runtime information related to the high availability service for a cluster that has been configured with a failover level admission control policy.  See *ClusterFailoverLevelAdmissionControlPolicy*.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**slot_info** | [**ClusterDasFailoverLevelAdvancedRuntimeInfoSlotInfo**](ClusterDasFailoverLevelAdvancedRuntimeInfoSlotInfo.md) |  | 
**total_slots** | **int** | The total number of slots available in the cluster.  See also *ClusterDasFailoverLevelAdvancedRuntimeInfoSlotInfo*.  ***Since:*** vSphere API 4.0  | 
**used_slots** | **int** | The number of slots currently being used.  See also *ClusterDasFailoverLevelAdvancedRuntimeInfoSlotInfo*.  ***Since:*** vSphere API 4.0  | 
**unreserved_slots** | **int** | The number of slots that are not used by currently powered on virtual machines and not reserved to satisfy the configured failover level.  This number gives an indication of how many additional virtual machines can be powered on in this cluster without violating the failover level (assuming the new virtual machine&#39;s reservations are satisfied by the current slot size). This value is computed as follows (where m is the configured failover level): Remove the m largest hosts (ie. the ones with the most slots) from the list of \&quot;good\&quot; hosts (see *ClusterDasFailoverLevelAdvancedRuntimeInfo.totalGoodHosts*). Sum up the number of slots on the remaining hosts and deduct the number of currently used slots (see *ClusterDasFailoverLevelAdvancedRuntimeInfo.usedSlots*). If this number is negative, use zero instead.  See also *ClusterDasFailoverLevelAdvancedRuntimeInfoSlotInfo*.  ***Since:*** vSphere API 4.0  | 
**total_vms** | **int** | The total number of powered on vms in the cluster.  ***Since:*** vSphere API 4.0  | 
**total_hosts** | **int** | The total number of hosts in the cluster.  ***Since:*** vSphere API 4.0  | 
**total_good_hosts** | **int** | The total number of connected hosts that are not in maintance mode and that do not have any DAS-related config issues on them.  ***Since:*** vSphere API 4.0  | 
**host_slots** | [**List[ClusterDasFailoverLevelAdvancedRuntimeInfoHostSlots]**](ClusterDasFailoverLevelAdvancedRuntimeInfoHostSlots.md) |  | [optional] 
**vms_requiring_multiple_slots** | [**List[ClusterDasFailoverLevelAdvancedRuntimeInfoVmSlots]**](ClusterDasFailoverLevelAdvancedRuntimeInfoVmSlots.md) | The list of virtual machines whose reservations and memory overhead are not satisfied by a single slot.  ***Since:*** vSphere API 5.1  | [optional] 

## Example

```python
from vmware_vi.models.cluster_das_failover_level_advanced_runtime_info import ClusterDasFailoverLevelAdvancedRuntimeInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterDasFailoverLevelAdvancedRuntimeInfo from a JSON string
cluster_das_failover_level_advanced_runtime_info_instance = ClusterDasFailoverLevelAdvancedRuntimeInfo.from_json(json)
# print the JSON string representation of the object
print ClusterDasFailoverLevelAdvancedRuntimeInfo.to_json()

# convert the object into a dict
cluster_das_failover_level_advanced_runtime_info_dict = cluster_das_failover_level_advanced_runtime_info_instance.to_dict()
# create an instance of ClusterDasFailoverLevelAdvancedRuntimeInfo from a dict
cluster_das_failover_level_advanced_runtime_info_form_dict = cluster_das_failover_level_advanced_runtime_info.from_dict(cluster_das_failover_level_advanced_runtime_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


