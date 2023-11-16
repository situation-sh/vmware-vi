# QueryAvailablePerfMetricRequestType

The parameters of *PerformanceManager.QueryAvailablePerfMetric*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entity** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | 
**begin_time** | **datetime** | Starting time (server time) for a period of time from which to return available metrics. If not specified, defaults to oldest available metric for the specified entity.  | [optional] 
**end_time** | **datetime** | Ending time (server time) for a period of time from which to return available performance metrics. If not specified, defaults to the most recently generated metric for the specified entity.  | [optional] 
**interval_id** | **int** | Period of time from which to retrieve metrics, defined by intervalId (rather than beginTime or endTime). Valid intervalIds include: - For real-time counters, the *refreshRate* of   the *performance   provider*. - For historical counters, the *samplingPeriod* of the *historical interval*.     If this parameter is not specified, the system returns available metrics for historical statistics&amp;#46;  | [optional] 

## Example

```python
from vmware_vi.models.query_available_perf_metric_request_type import QueryAvailablePerfMetricRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of QueryAvailablePerfMetricRequestType from a JSON string
query_available_perf_metric_request_type_instance = QueryAvailablePerfMetricRequestType.from_json(json)
# print the JSON string representation of the object
print QueryAvailablePerfMetricRequestType.to_json()

# convert the object into a dict
query_available_perf_metric_request_type_dict = query_available_perf_metric_request_type_instance.to_dict()
# create an instance of QueryAvailablePerfMetricRequestType from a dict
query_available_perf_metric_request_type_form_dict = query_available_perf_metric_request_type.from_dict(query_available_perf_metric_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


