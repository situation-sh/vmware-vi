# PerfEntityMetricCSV

This data object type stores metric values for a specific entity in CSV format. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sample_info_csv** | **str** | The *PerfSampleInfo* encoded in the following CSV format: \\[interval1\\], \\[date1\\], \\[interval2\\], \\[date2\\], and so on.  | 
**value** | [**List[PerfMetricSeriesCSV]**](PerfMetricSeriesCSV.md) | Metric values corresponding to the samples collected in this list.  | [optional] 

## Example

```python
from vmware_vi.models.perf_entity_metric_csv import PerfEntityMetricCSV

# TODO update the JSON string below
json = "{}"
# create an instance of PerfEntityMetricCSV from a JSON string
perf_entity_metric_csv_instance = PerfEntityMetricCSV.from_json(json)
# print the JSON string representation of the object
print PerfEntityMetricCSV.to_json()

# convert the object into a dict
perf_entity_metric_csv_dict = perf_entity_metric_csv_instance.to_dict()
# create an instance of PerfEntityMetricCSV from a dict
perf_entity_metric_csv_form_dict = perf_entity_metric_csv.from_dict(perf_entity_metric_csv_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


