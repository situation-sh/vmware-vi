# ClusterComputeResourceSummary

The *ClusterComputeResourceSummary* data object encapsulates runtime properties of a *ClusterComputeResource*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**current_failover_level** | **int** | Deprecated as of vSphere API 4.0, use *ClusterFailoverLevelAdmissionControlInfo.currentFailoverLevel*.  Current failover level.  This is the number of physical host failures that can be tolerated without impacting the ability to satisfy the minimums for all running virtual machines. This represents the current value, as opposed to desired value configured by the user.  | 
**admission_control_info** | [**ClusterDasAdmissionControlInfo**](ClusterDasAdmissionControlInfo.md) |  | [optional] 
**num_vmotions** | **int** | Total number of migrations with VMotion that have been done internal to this cluster.  | 
**target_balance** | **int** | The target balance, in terms of standard deviation, for a DRS cluster.  Units are thousandths. For example, 12 represents 0.012.  ***Since:*** vSphere API 4.0  | [optional] 
**current_balance** | **int** | The current balance, in terms of standard deviation, for a DRS cluster.  Units are thousandths. For example, 12 represents 0.012.  ***Since:*** vSphere API 4.0  | [optional] 
**drs_score** | **int** | The DRS score of this cluster, in percentage.  ***Since:*** vSphere API 7.0  | [optional] 
**num_vms_per_drs_score_bucket** | **List[int]** | The number of VMs in this cluster corresponding to each DRS score bucket.  The buckets are defined as follows: - 0% - 20% - 21% - 40% - 41% - 60% - 61% - 80% - 81% - 100%    ***Since:*** vSphere API 7.0  | [optional] 
**usage_summary** | [**ClusterUsageSummary**](ClusterUsageSummary.md) |  | [optional] 
**current_evc_mode_key** | **str** | The Enhanced VMotion Compatibility mode that is currently in effect for all hosts in this cluster; unset if no EVC mode is active.  See also *Capability.supportedEVCMode*.  ***Since:*** vSphere API 4.0  | [optional] 
**current_evc_graphics_mode_key** | **str** | The Enhanced VMotion Compatibility Graphics mode that is currently in effect for all hosts in this cluster; unset if no EVC mode is active.  See also *Capability.supportedEVCGraphicsMode*.  ***Since:*** vSphere API 7.0.1.0  | [optional] 
**das_data** | [**ClusterDasData**](ClusterDasData.md) |  | [optional] 
**cluster_maintenance_mode_status** | **str** | Configuration pertinent to state of the cluster maintenance mode.  Valid values are enumerated by the *ClusterMaintenanceModeStatus* type.  ***Since:*** vSphere API 7.0.0.2  | [optional] 
**vcs_health_status** | **str** | The health status of the vSphere Cluster Services in the cluster.  Supported values are enumerated by the *VcsHealthStatus* type.  ***Since:*** vSphere API 7.0.1.1  | [optional] 
**vcs_slots** | [**List[ClusterComputeResourceVcsSlots]**](ClusterComputeResourceVcsSlots.md) | An array of hosts and number of resource slots on the host for vSphere Cluster Services in the cluster.  The number of resource slots on the host includes both following types: 1\\. Number of vCS VMs running on the host (resource reserved and occupied). 2\\. Number of reserved and unoccupied slots (reserved for new vCS VMs).  ***Since:*** vSphere API 7.0.1.1  | [optional] 

## Example

```python
from vmware_vi.models.cluster_compute_resource_summary import ClusterComputeResourceSummary

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterComputeResourceSummary from a JSON string
cluster_compute_resource_summary_instance = ClusterComputeResourceSummary.from_json(json)
# print the JSON string representation of the object
print ClusterComputeResourceSummary.to_json()

# convert the object into a dict
cluster_compute_resource_summary_dict = cluster_compute_resource_summary_instance.to_dict()
# create an instance of ClusterComputeResourceSummary from a dict
cluster_compute_resource_summary_form_dict = cluster_compute_resource_summary.from_dict(cluster_compute_resource_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


