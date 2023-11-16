# ClusterFailoverResourcesAdmissionControlInfo

The current admission control related information if the cluster was configured with a FailoverResourcesAdmissionControlPolicy.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**current_cpu_failover_resources_percent** | **int** | The percentage of cpu resources in the cluster available for failover.  ***Since:*** vSphere API 4.0  | 
**current_memory_failover_resources_percent** | **int** | The percentage of memory resources in the cluster available for failover.  ***Since:*** vSphere API 4.0  | 
**current_p_mem_failover_resources_percent** | **int** | The percentage of persistent memory resources in the cluster available for failover.  ***Since:*** vSphere API 7.0.2.0  | [optional] 

## Example

```python
from vmware_vi.models.cluster_failover_resources_admission_control_info import ClusterFailoverResourcesAdmissionControlInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterFailoverResourcesAdmissionControlInfo from a JSON string
cluster_failover_resources_admission_control_info_instance = ClusterFailoverResourcesAdmissionControlInfo.from_json(json)
# print the JSON string representation of the object
print ClusterFailoverResourcesAdmissionControlInfo.to_json()

# convert the object into a dict
cluster_failover_resources_admission_control_info_dict = cluster_failover_resources_admission_control_info_instance.to_dict()
# create an instance of ClusterFailoverResourcesAdmissionControlInfo from a dict
cluster_failover_resources_admission_control_info_form_dict = cluster_failover_resources_admission_control_info.from_dict(cluster_failover_resources_admission_control_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


