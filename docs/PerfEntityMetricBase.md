# PerfEntityMetricBase

Base type for the various *PerfEntityMetric* encodings. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entity** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | 

## Example

```python
from vmware_vi.models.perf_entity_metric_base import PerfEntityMetricBase

# TODO update the JSON string below
json = "{}"
# create an instance of PerfEntityMetricBase from a JSON string
perf_entity_metric_base_instance = PerfEntityMetricBase.from_json(json)
# print the JSON string representation of the object
print PerfEntityMetricBase.to_json()

# convert the object into a dict
perf_entity_metric_base_dict = perf_entity_metric_base_instance.to_dict()
# create an instance of PerfEntityMetricBase from a dict
perf_entity_metric_base_form_dict = perf_entity_metric_base.from_dict(perf_entity_metric_base_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


