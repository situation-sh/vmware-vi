# PerfCompositeMetric

*PerfCompositeMetric* includes an optional aggregated entity performance statistics and a list of composite entities performance statistics&#46; The aggregated entity statistics are optional because some entities, such as folders, do not have their own statistics&#46; 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entity** | [**PerfEntityMetricBase**](PerfEntityMetricBase.md) |  | [optional] 
**child_entity** | [**List[PerfEntityMetricBase]**](PerfEntityMetricBase.md) | A list of *metrics* of performance providers that comprise the aggregated entity.  For example, Host is an aggregated entity for virtual machines and virtual machine Folders. ResourcePools are aggregate entities for virtual machines. Host, Folder, and Cluster are aggregate entities for hosts in the cluster or folder.  | [optional] 

## Example

```python
from vmware_vi.models.perf_composite_metric import PerfCompositeMetric

# TODO update the JSON string below
json = "{}"
# create an instance of PerfCompositeMetric from a JSON string
perf_composite_metric_instance = PerfCompositeMetric.from_json(json)
# print the JSON string representation of the object
print PerfCompositeMetric.to_json()

# convert the object into a dict
perf_composite_metric_dict = perf_composite_metric_instance.to_dict()
# create an instance of PerfCompositeMetric from a dict
perf_composite_metric_form_dict = perf_composite_metric.from_dict(perf_composite_metric_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


