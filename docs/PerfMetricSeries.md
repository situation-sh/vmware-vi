# PerfMetricSeries

This is a generic data object type that stores values for a specific performance metric.  Useful data objects that store actual metric values extend this data object (see *PerfMetricIntSeries*). 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | [**PerfMetricId**](PerfMetricId.md) |  | 

## Example

```python
from vmware_vi.models.perf_metric_series import PerfMetricSeries

# TODO update the JSON string below
json = "{}"
# create an instance of PerfMetricSeries from a JSON string
perf_metric_series_instance = PerfMetricSeries.from_json(json)
# print the JSON string representation of the object
print PerfMetricSeries.to_json()

# convert the object into a dict
perf_metric_series_dict = perf_metric_series_instance.to_dict()
# create an instance of PerfMetricSeries from a dict
perf_metric_series_form_dict = perf_metric_series.from_dict(perf_metric_series_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


