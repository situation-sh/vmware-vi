# ArrayOfPerfMetricIntSeries

A boxed array of *PerfMetricIntSeries*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[PerfMetricIntSeries]**](PerfMetricIntSeries.md) |  | 

## Example

```python
from vmware_vi.models.array_of_perf_metric_int_series import ArrayOfPerfMetricIntSeries

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfPerfMetricIntSeries from a JSON string
array_of_perf_metric_int_series_instance = ArrayOfPerfMetricIntSeries.from_json(json)
# print the JSON string representation of the object
print ArrayOfPerfMetricIntSeries.to_json()

# convert the object into a dict
array_of_perf_metric_int_series_dict = array_of_perf_metric_int_series_instance.to_dict()
# create an instance of ArrayOfPerfMetricIntSeries from a dict
array_of_perf_metric_int_series_form_dict = array_of_perf_metric_int_series.from_dict(array_of_perf_metric_int_series_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


