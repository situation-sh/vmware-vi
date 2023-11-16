# ArrayOfPerfMetricSeriesCSV

A boxed array of *PerfMetricSeriesCSV*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[PerfMetricSeriesCSV]**](PerfMetricSeriesCSV.md) |  | 

## Example

```python
from vmware_vi.models.array_of_perf_metric_series_csv import ArrayOfPerfMetricSeriesCSV

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfPerfMetricSeriesCSV from a JSON string
array_of_perf_metric_series_csv_instance = ArrayOfPerfMetricSeriesCSV.from_json(json)
# print the JSON string representation of the object
print ArrayOfPerfMetricSeriesCSV.to_json()

# convert the object into a dict
array_of_perf_metric_series_csv_dict = array_of_perf_metric_series_csv_instance.to_dict()
# create an instance of ArrayOfPerfMetricSeriesCSV from a dict
array_of_perf_metric_series_csv_form_dict = array_of_perf_metric_series_csv.from_dict(array_of_perf_metric_series_csv_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


