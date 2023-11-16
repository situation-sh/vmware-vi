# ArrayOfPerfCompositeMetric

A boxed array of *PerfCompositeMetric*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[PerfCompositeMetric]**](PerfCompositeMetric.md) |  | 

## Example

```python
from vmware_vi.models.array_of_perf_composite_metric import ArrayOfPerfCompositeMetric

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfPerfCompositeMetric from a JSON string
array_of_perf_composite_metric_instance = ArrayOfPerfCompositeMetric.from_json(json)
# print the JSON string representation of the object
print ArrayOfPerfCompositeMetric.to_json()

# convert the object into a dict
array_of_perf_composite_metric_dict = array_of_perf_composite_metric_instance.to_dict()
# create an instance of ArrayOfPerfCompositeMetric from a dict
array_of_perf_composite_metric_form_dict = array_of_perf_composite_metric.from_dict(array_of_perf_composite_metric_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


