# PerfMetricSeriesCSV

This data object type represents a *PerfMetricSeries* encoded in CSV format. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **str** | An array of sample values in CSV format  | [optional] 

## Example

```python
from vmware_vi.models.perf_metric_series_csv import PerfMetricSeriesCSV

# TODO update the JSON string below
json = "{}"
# create an instance of PerfMetricSeriesCSV from a JSON string
perf_metric_series_csv_instance = PerfMetricSeriesCSV.from_json(json)
# print the JSON string representation of the object
print PerfMetricSeriesCSV.to_json()

# convert the object into a dict
perf_metric_series_csv_dict = perf_metric_series_csv_instance.to_dict()
# create an instance of PerfMetricSeriesCSV from a dict
perf_metric_series_csv_form_dict = perf_metric_series_csv.from_dict(perf_metric_series_csv_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


