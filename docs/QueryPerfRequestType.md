# QueryPerfRequestType

The parameters of *PerformanceManager.QueryPerf*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**query_spec** | [**List[PerfQuerySpec]**](PerfQuerySpec.md) | An array of *PerfQuerySpec* objects. Each *PerfQuerySpec* object specifies a managed object reference for an entity, plus optional criteria for filtering results. Only metrics for entities that can be resolved and that are valid *performance providers* are returned in any result.  Each *PerfQuerySpec* object in the array submitted in this operation can query for different metrics. Or, select all types of statistics for a single managed entity.  Raw data feed workaround: Normally, QueryPerf will return performance statistics stored in the VirtualCenter database. However this may not be suitable for certain applications. For example, applications that treat VirtualCenter as a raw data source, query for performance statistics regularly (say every 5 minutes) and extract the data for external archival and reporting. Such applications need better query performance. These applications should query statistics using QueryPerf for the base historical interval (5 minutes by default) having a start and end time range within 30 minutes from the current VirtualCenter server system time. These QueryPerf calls will have better performance than other QueryPerf calls.  | 

## Example

```python
from vmware_vi.models.query_perf_request_type import QueryPerfRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of QueryPerfRequestType from a JSON string
query_perf_request_type_instance = QueryPerfRequestType.from_json(json)
# print the JSON string representation of the object
print QueryPerfRequestType.to_json()

# convert the object into a dict
query_perf_request_type_dict = query_perf_request_type_instance.to_dict()
# create an instance of QueryPerfRequestType from a dict
query_perf_request_type_form_dict = query_perf_request_type.from_dict(query_perf_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


