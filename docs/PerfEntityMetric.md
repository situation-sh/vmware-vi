# PerfEntityMetric

This data object type stores values and metadata for metrics associated with a specific entity, in 'normal' format. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sample_info** | [**List[PerfSampleInfo]**](PerfSampleInfo.md) | A list of objects containing information (an interval and a timestamp) about the samples collected.  | [optional] 
**value** | [**List[PerfMetricSeries]**](PerfMetricSeries.md) | A list of values that corresponds to the samples collected.  | [optional] 

## Example

```python
from vmware_vi.models.perf_entity_metric import PerfEntityMetric

# TODO update the JSON string below
json = "{}"
# create an instance of PerfEntityMetric from a JSON string
perf_entity_metric_instance = PerfEntityMetric.from_json(json)
# print the JSON string representation of the object
print PerfEntityMetric.to_json()

# convert the object into a dict
perf_entity_metric_dict = perf_entity_metric_instance.to_dict()
# create an instance of PerfEntityMetric from a dict
perf_entity_metric_form_dict = perf_entity_metric.from_dict(perf_entity_metric_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


