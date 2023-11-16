# HostListSummaryQuickStats

Basic host statistics.  Included in the host statistics are fairness scores. Fairness scores are represented in units with relative values, meaning they are evaluated relative to the scores of other hosts. They should not be thought of as having any particular absolute value. Each fairness unit represents an increment of 0.001 in a fairness score. The further the fairness score diverges from 1, the less fair the allocation. Therefore, a fairness score of 990, representing 0.990, is more fair than a fairness score of 1015, which represents 1.015. This is because 1.015 is further from 1 than 0.990. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**overall_cpu_usage** | **int** | Aggregated CPU usage across all cores on the host in MHz.  This is only available if the host is connected.  | [optional] 
**overall_memory_usage** | **int** | Physical memory usage on the host in MB.  This is only available if the host is connected.  | [optional] 
**distributed_cpu_fairness** | **int** | The fairness of distributed CPU resource allocation on the host.  | [optional] 
**distributed_memory_fairness** | **int** | The fairness of distributed memory resource allocation on the host.  | [optional] 
**available_p_mem_capacity** | **int** | The available capacity in MB.  ***Since:*** vSphere API 6.7  | [optional] 
**uptime** | **int** | The system uptime of the host in seconds.  ***Since:*** vSphere API 4.1  | [optional] 

## Example

```python
from vmware_vi.models.host_list_summary_quick_stats import HostListSummaryQuickStats

# TODO update the JSON string below
json = "{}"
# create an instance of HostListSummaryQuickStats from a JSON string
host_list_summary_quick_stats_instance = HostListSummaryQuickStats.from_json(json)
# print the JSON string representation of the object
print HostListSummaryQuickStats.to_json()

# convert the object into a dict
host_list_summary_quick_stats_dict = host_list_summary_quick_stats_instance.to_dict()
# create an instance of HostListSummaryQuickStats from a dict
host_list_summary_quick_stats_form_dict = host_list_summary_quick_stats.from_dict(host_list_summary_quick_stats_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


