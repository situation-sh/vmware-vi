# ClusterFailoverResourcesAdmissionControlPolicy

The *ClusterFailoverResourcesAdmissionControlPolicy* reserves a specified percentage of aggregate cluster resources for failover.  With the resources failover policy in place, vSphere HA uses the following calculations to control virtual machine migration in the cluster. 1. Calculate the total resource requirements for all powered-on    virtual machines in the cluster. 2. Calculate the total host resources available for virtual machines. 3. Calculate the Current CPU failover capacity, memory failover    capacity and optionally, persistent memory failover capacity    for the cluster. 4. Compare the current CPU failover capacity and current memory failover    capacity with the configured resource percentages    (*ClusterFailoverResourcesAdmissionControlPolicy.cpuFailoverResourcesPercent*    and    *ClusterFailoverResourcesAdmissionControlPolicy.memoryFailoverResourcesPercent*).    If either current capacity is less than the corresponding configured    capacity, HA does not allow the operation.     HA uses the actual reservations of the virtual machines. If a virtual machine does not have reservations, meaning that the reservation is 0, a default of 0MB memory and 256MHz CPU is applied. This is controlled by the same HA advanced options used for the failover level policy (*ClusterFailoverLevelAdmissionControlPolicy*).  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cpu_failover_resources_percent** | **int** | Percentage of CPU resources in the cluster to reserve for failover.  You can specify up to 100% of CPU resources for failover.  ***Since:*** vSphere API 4.0  | 
**memory_failover_resources_percent** | **int** | Percentage of memory resources in the cluster to reserve for failover.  You can specify up to 100% of memory resources for failover.  ***Since:*** vSphere API 4.0  | 
**failover_level** | **int** | Number of host failures that should be tolerated, still guaranteeing sufficient resources to restart virtual machines on available hosts.  If not set, we assume 1.  ***Since:*** vSphere API 6.5  | [optional] 
**auto_compute_percentages** | **bool** | Flag to enable user input values for *ClusterFailoverResourcesAdmissionControlPolicy.cpuFailoverResourcesPercent* and *ClusterFailoverResourcesAdmissionControlPolicy.memoryFailoverResourcesPercent* By default, this is true and the default calculation is using the *ClusterFailoverResourcesAdmissionControlPolicy.failoverLevel* hosts&#39; resources.  If users want to override the percentage values, they must disable the auto-compute by setting this field to false.  ***Since:*** vSphere API 6.5  | [optional] 
**p_mem_failover_resources_percent** | **int** | Percentage of persistent memory resources in the cluster to reserve for the failover.  You can specify up to 100% of persistent memory resources for failover.  ***Since:*** vSphere API 7.0.2.0  | [optional] 
**auto_compute_p_mem_failover_resources_percent** | **bool** | Flag to enable user input values for *ClusterFailoverResourcesAdmissionControlPolicy.pMemFailoverResourcesPercent* By default, this is true and the default calculation is done using the *ClusterFailoverResourcesAdmissionControlPolicy.failoverLevel* hosts&#39; resources.  If a user wants to override the percentage values, they must disable the auto-compute by setting this field to false.  ***Since:*** vSphere API 7.0.2.0  | [optional] 

## Example

```python
from vmware_vi.models.cluster_failover_resources_admission_control_policy import ClusterFailoverResourcesAdmissionControlPolicy

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterFailoverResourcesAdmissionControlPolicy from a JSON string
cluster_failover_resources_admission_control_policy_instance = ClusterFailoverResourcesAdmissionControlPolicy.from_json(json)
# print the JSON string representation of the object
print ClusterFailoverResourcesAdmissionControlPolicy.to_json()

# convert the object into a dict
cluster_failover_resources_admission_control_policy_dict = cluster_failover_resources_admission_control_policy_instance.to_dict()
# create an instance of ClusterFailoverResourcesAdmissionControlPolicy from a dict
cluster_failover_resources_admission_control_policy_form_dict = cluster_failover_resources_admission_control_policy.from_dict(cluster_failover_resources_admission_control_policy_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


