# ArrayOfPerfEntityMetric

A boxed array of *PerfEntityMetric*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[PerfEntityMetric]**](PerfEntityMetric.md) |  | 

## Example

```python
from vmware_vi.models.array_of_perf_entity_metric import ArrayOfPerfEntityMetric

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfPerfEntityMetric from a JSON string
array_of_perf_entity_metric_instance = ArrayOfPerfEntityMetric.from_json(json)
# print the JSON string representation of the object
print ArrayOfPerfEntityMetric.to_json()

# convert the object into a dict
array_of_perf_entity_metric_dict = array_of_perf_entity_metric_instance.to_dict()
# create an instance of ArrayOfPerfEntityMetric from a dict
array_of_perf_entity_metric_form_dict = array_of_perf_entity_metric.from_dict(array_of_perf_entity_metric_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


