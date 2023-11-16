# ClusterUsageSummary

This class contains cluster usage summary that is populated by DRS and used by Cloud Placement Engine in VCD.  ***Since:*** vSphere API 6.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_cpu_capacity_mhz** | **int** | Total CPU capacity of the cluster.  ***Since:*** vSphere API 6.0  | 
**total_mem_capacity_mb** | **int** | Total memory capacity of the cluster.  ***Since:*** vSphere API 6.0  | 
**cpu_reservation_mhz** | **int** | Sum of CPU reservation of all the Resource Pools and powered-on VMs in the cluster.  ***Since:*** vSphere API 6.0  | 
**mem_reservation_mb** | **int** | Sum of memory reservation of all the Resource Pools and powered-on VMs in the cluster.  ***Since:*** vSphere API 6.0  | 
**powered_off_cpu_reservation_mhz** | **int** | Sum of CPU reservation of all the powered-off VMs in the cluster.  ***Since:*** vSphere API 6.0  | [optional] 
**powered_off_mem_reservation_mb** | **int** | Sum of memory reservation of all the powered-off VMs in the cluster.  ***Since:*** vSphere API 6.0  | [optional] 
**cpu_demand_mhz** | **int** | Sum of CPU demand of all the powered-on VMs in the cluster.  ***Since:*** vSphere API 6.0  | 
**mem_demand_mb** | **int** | Sum of memory demand of all the powered-on VMs in the cluster.  ***Since:*** vSphere API 6.0  | 
**stats_gen_number** | **int** | Generation number of the usage stats.  Updated during every DRS load balancing call.  ***Since:*** vSphere API 6.0  | 
**cpu_entitled_mhz** | **int** | This is the current CPU entitlement across the cluster  ***Since:*** vSphere API 6.0  | 
**mem_entitled_mb** | **int** | This is the current memory entitlement across the cluster  ***Since:*** vSphere API 6.0  | 
**powered_off_vm_count** | **int** | The number of powered off VMs in the cluster  ***Since:*** vSphere API 6.0  | 
**total_vm_count** | **int** | The number of VMs in the cluster  ***Since:*** vSphere API 6.0  | 

## Example

```python
from vmware_vi.models.cluster_usage_summary import ClusterUsageSummary

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterUsageSummary from a JSON string
cluster_usage_summary_instance = ClusterUsageSummary.from_json(json)
# print the JSON string representation of the object
print ClusterUsageSummary.to_json()

# convert the object into a dict
cluster_usage_summary_dict = cluster_usage_summary_instance.to_dict()
# create an instance of ClusterUsageSummary from a dict
cluster_usage_summary_form_dict = cluster_usage_summary.from_dict(cluster_usage_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


