# ArrayOfPerfEntityMetricBase

A boxed array of *PerfEntityMetricBase*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[PerfEntityMetricBase]**](PerfEntityMetricBase.md) |  | 

## Example

```python
from vmware_vi.models.array_of_perf_entity_metric_base import ArrayOfPerfEntityMetricBase

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfPerfEntityMetricBase from a JSON string
array_of_perf_entity_metric_base_instance = ArrayOfPerfEntityMetricBase.from_json(json)
# print the JSON string representation of the object
print ArrayOfPerfEntityMetricBase.to_json()

# convert the object into a dict
array_of_perf_entity_metric_base_dict = array_of_perf_entity_metric_base_instance.to_dict()
# create an instance of ArrayOfPerfEntityMetricBase from a dict
array_of_perf_entity_metric_base_form_dict = array_of_perf_entity_metric_base.from_dict(array_of_perf_entity_metric_base_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


