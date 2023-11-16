# QueryPerfCounterRequestType

The parameters of *PerformanceManager.QueryPerfCounter*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**counter_id** | **List[int]** | An array of one or more *counterIds* representing performance counters for which information is being retrieved.  | 

## Example

```python
from vmware_vi.models.query_perf_counter_request_type import QueryPerfCounterRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of QueryPerfCounterRequestType from a JSON string
query_perf_counter_request_type_instance = QueryPerfCounterRequestType.from_json(json)
# print the JSON string representation of the object
print QueryPerfCounterRequestType.to_json()

# convert the object into a dict
query_perf_counter_request_type_dict = query_perf_counter_request_type_instance.to_dict()
# create an instance of QueryPerfCounterRequestType from a dict
query_perf_counter_request_type_form_dict = query_perf_counter_request_type.from_dict(query_perf_counter_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


