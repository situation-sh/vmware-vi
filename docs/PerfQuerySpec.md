# PerfQuerySpec

This data object specifies the query parameters, including the managed object reference to the target entity for statistics retrieval. - If the optional *PerfQuerySpec.intervalId* is omitted, the metrics are   returned in their originally sampled interval.   - When an *PerfQuerySpec.intervalId* is specified, the server tries to     summarize the information for the specified *PerfQuerySpec.intervalId*.     However, if that interval does not exist or has no data, the     server summarizes the information using the best interval     available. - If the range between *PerfQuerySpec.startTime* and *PerfQuerySpec.endTime* crosses   multiple sample interval periods, the result contains data from the   longest interval in the period. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entity** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | 
**start_time** | **datetime** | The server time from which to obtain counters.  If not specified, defaults to the first available counter. When a startTime is specified, the returned samples do not include the sample at startTime.  | [optional] 
**end_time** | **datetime** | The time up to which statistics are retrieved.  Corresponds to server time. When endTime is omitted, the returned result includes up to the most recent metric value. When an endTime is specified, the returned samples include the sample at endTime.  | [optional] 
**max_sample** | **int** | Limits the number of samples returned.  Defaults to the most recent sample (or samples), unless a time range is specified. Use this property only in conjunction with the *PerfQuerySpec.intervalId* to obtain real-time statistics (set the *PerfQuerySpec.intervalId* to the *PerfProviderSummary.refreshRate*. This property is ignored for historical statistics, and is not valid for the *PerformanceManager.QueryPerfComposite* operation.  | [optional] 
**metric_id** | [**List[PerfMetricId]**](PerfMetricId.md) | The performance metrics to be retrieved.  This property is required for the *PerformanceManager.QueryPerfComposite* operation.  | [optional] 
**interval_id** | **int** | The interval (*PerfInterval.samplingPeriod*), in seconds, for the performance statistics&amp;#46; For aggregated information, use one of the historical intervals for this property.  See *PerfInterval* for more information. - To obtain the greatest detail, use the provider&amp;#146;s *PerfProviderSummary.refreshRate* for this   property.  | [optional] 
**format** | **str** | The format to be used while returning the statistics&amp;#46;  See also *PerfFormat_enum*.  | [optional] 

## Example

```python
from vmware_vi.models.perf_query_spec import PerfQuerySpec

# TODO update the JSON string below
json = "{}"
# create an instance of PerfQuerySpec from a JSON string
perf_query_spec_instance = PerfQuerySpec.from_json(json)
# print the JSON string representation of the object
print PerfQuerySpec.to_json()

# convert the object into a dict
perf_query_spec_dict = perf_query_spec_instance.to_dict()
# create an instance of PerfQuerySpec from a dict
perf_query_spec_form_dict = perf_query_spec.from_dict(perf_query_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


