# QueryPerfProviderSummaryRequestType

The parameters of *PerformanceManager.QueryPerfProviderSummary*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entity** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | 

## Example

```python
from vmware_vi.models.query_perf_provider_summary_request_type import QueryPerfProviderSummaryRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of QueryPerfProviderSummaryRequestType from a JSON string
query_perf_provider_summary_request_type_instance = QueryPerfProviderSummaryRequestType.from_json(json)
# print the JSON string representation of the object
print QueryPerfProviderSummaryRequestType.to_json()

# convert the object into a dict
query_perf_provider_summary_request_type_dict = query_perf_provider_summary_request_type_instance.to_dict()
# create an instance of QueryPerfProviderSummaryRequestType from a dict
query_perf_provider_summary_request_type_form_dict = query_perf_provider_summary_request_type.from_dict(query_perf_provider_summary_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


