# StoragePerformanceSummary

Summary statistics for datastore performance The statistics are reported in aggregated quantiles over a time period  ***Since:*** vSphere API 5.1 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**interval** | **int** | Time period over which statistics are aggregated The reported time unit is in seconds  ***Since:*** vSphere API 5.1  | 
**percentile** | **List[int]** | Metric percentile specification.  A percentile is a value between 1 and 100. The metric value reported in the aggregated statistics corresponds with the percentile values in this field. For example, if the value of percentile\\[0\\] is P, and the value of the datastoreReadLatency\\[0\\] is L, then P% of all the read IOs performed during observation interval is less than L milliseconds.  ***Since:*** vSphere API 5.1  | 
**datastore_read_latency** | **List[float]** | Aggregated datastore latency in milliseconds for read operations  ***Since:*** vSphere API 5.1  | 
**datastore_write_latency** | **List[float]** | Aggregated datastore latency in milliseconds for write operations  ***Since:*** vSphere API 5.1  | 
**datastore_vm_latency** | **List[float]** | Aggregated datastore latency as observed by Vms using the datastore The reported latency is in milliseconds.  ***Since:*** vSphere API 5.1  | 
**datastore_read_iops** | **List[float]** | Aggregated datastore Read IO rate (Reads/second)  ***Since:*** vSphere API 5.1  | 
**datastore_write_iops** | **List[float]** | Aggregated datastore Write IO rate (Writes/second)  ***Since:*** vSphere API 5.1  | 
**sioc_activity_duration** | **int** | Cumulative SIOC activity to satisfy SIOC latency threshold setting.  This metric indicates the total time that SIOC is actively throttling IO requests. The SIOC throttling activity occurs whenever the datastore latency exceeds the SIOC latency threshold. If SIOC is not enabled on the datastore, the metric indicates the total time that SIOC would have been active. The unit of reporting is in milliseconds.  ***Since:*** vSphere API 5.1  | 

## Example

```python
from vmware_vi.models.storage_performance_summary import StoragePerformanceSummary

# TODO update the JSON string below
json = "{}"
# create an instance of StoragePerformanceSummary from a JSON string
storage_performance_summary_instance = StoragePerformanceSummary.from_json(json)
# print the JSON string representation of the object
print StoragePerformanceSummary.to_json()

# convert the object into a dict
storage_performance_summary_dict = storage_performance_summary_instance.to_dict()
# create an instance of StoragePerformanceSummary from a dict
storage_performance_summary_form_dict = storage_performance_summary.from_dict(storage_performance_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


