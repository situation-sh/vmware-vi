# QueryPerfCounterByLevelRequestType

The parameters of *PerformanceManager.QueryPerfCounterByLevel*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**level** | **int** | A number between 1 and 4 that specifies the collection level.  | 

## Example

```python
from vmware_vi.models.query_perf_counter_by_level_request_type import QueryPerfCounterByLevelRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of QueryPerfCounterByLevelRequestType from a JSON string
query_perf_counter_by_level_request_type_instance = QueryPerfCounterByLevelRequestType.from_json(json)
# print the JSON string representation of the object
print QueryPerfCounterByLevelRequestType.to_json()

# convert the object into a dict
query_perf_counter_by_level_request_type_dict = query_perf_counter_by_level_request_type_instance.to_dict()
# create an instance of QueryPerfCounterByLevelRequestType from a dict
query_perf_counter_by_level_request_type_form_dict = query_perf_counter_by_level_request_type.from_dict(query_perf_counter_by_level_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


