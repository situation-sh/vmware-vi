# ArrayOfPerfMetricSeries

A boxed array of *PerfMetricSeries*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[PerfMetricSeries]**](PerfMetricSeries.md) |  | 

## Example

```python
from vmware_vi.models.array_of_perf_metric_series import ArrayOfPerfMetricSeries

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfPerfMetricSeries from a JSON string
array_of_perf_metric_series_instance = ArrayOfPerfMetricSeries.from_json(json)
# print the JSON string representation of the object
print ArrayOfPerfMetricSeries.to_json()

# convert the object into a dict
array_of_perf_metric_series_dict = array_of_perf_metric_series_instance.to_dict()
# create an instance of ArrayOfPerfMetricSeries from a dict
array_of_perf_metric_series_form_dict = array_of_perf_metric_series.from_dict(array_of_perf_metric_series_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


