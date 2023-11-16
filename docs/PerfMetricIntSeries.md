# PerfMetricIntSeries

This data object type describes integer metric values.  The size of the array must match the size of *PerfEntityMetric.sampleInfo* property in the *PerfEntityMetric* that contains this series. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **List[int]** | An array of 64-bit integer values.  The size of the array matches the size as the *PerfSampleInfo*, because the values can only be interpreted in the context of the sample that generated the value.  | [optional] 

## Example

```python
from vmware_vi.models.perf_metric_int_series import PerfMetricIntSeries

# TODO update the JSON string below
json = "{}"
# create an instance of PerfMetricIntSeries from a JSON string
perf_metric_int_series_instance = PerfMetricIntSeries.from_json(json)
# print the JSON string representation of the object
print PerfMetricIntSeries.to_json()

# convert the object into a dict
perf_metric_int_series_dict = perf_metric_int_series_instance.to_dict()
# create an instance of PerfMetricIntSeries from a dict
perf_metric_int_series_form_dict = perf_metric_int_series.from_dict(perf_metric_int_series_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


