# QueryPerfCompositeRequestType

The parameters of *PerformanceManager.QueryPerfComposite*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**query_spec** | [**PerfQuerySpec**](PerfQuerySpec.md) |  | 

## Example

```python
from vmware_vi.models.query_perf_composite_request_type import QueryPerfCompositeRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of QueryPerfCompositeRequestType from a JSON string
query_perf_composite_request_type_instance = QueryPerfCompositeRequestType.from_json(json)
# print the JSON string representation of the object
print QueryPerfCompositeRequestType.to_json()

# convert the object into a dict
query_perf_composite_request_type_dict = query_perf_composite_request_type_instance.to_dict()
# create an instance of QueryPerfCompositeRequestType from a dict
query_perf_composite_request_type_form_dict = query_perf_composite_request_type.from_dict(query_perf_composite_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


