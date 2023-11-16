# ClusterResourceUsageSummary

This class contains cpu, memory and storage usage information at cluster level.  ***Since:*** vSphere API 6.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cpu_used_mhz** | **int** |  | 
**cpu_capacity_mhz** | **int** |  | 
**mem_used_mb** | **int** |  | 
**mem_capacity_mb** | **int** |  | 
**p_mem_available_mb** | **int** |  | [optional] 
**p_mem_capacity_mb** | **int** |  | [optional] 
**storage_used_mb** | **int** |  | 
**storage_capacity_mb** | **int** |  | 

## Example

```python
from vmware_vi.models.cluster_resource_usage_summary import ClusterResourceUsageSummary

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterResourceUsageSummary from a JSON string
cluster_resource_usage_summary_instance = ClusterResourceUsageSummary.from_json(json)
# print the JSON string representation of the object
print ClusterResourceUsageSummary.to_json()

# convert the object into a dict
cluster_resource_usage_summary_dict = cluster_resource_usage_summary_instance.to_dict()
# create an instance of ClusterResourceUsageSummary from a dict
cluster_resource_usage_summary_form_dict = cluster_resource_usage_summary.from_dict(cluster_resource_usage_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


