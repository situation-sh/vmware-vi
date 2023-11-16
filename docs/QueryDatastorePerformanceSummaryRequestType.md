# QueryDatastorePerformanceSummaryRequestType

The parameters of *StorageResourceManager.QueryDatastorePerformanceSummary*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**datastore** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | 

## Example

```python
from vmware_vi.models.query_datastore_performance_summary_request_type import QueryDatastorePerformanceSummaryRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of QueryDatastorePerformanceSummaryRequestType from a JSON string
query_datastore_performance_summary_request_type_instance = QueryDatastorePerformanceSummaryRequestType.from_json(json)
# print the JSON string representation of the object
print QueryDatastorePerformanceSummaryRequestType.to_json()

# convert the object into a dict
query_datastore_performance_summary_request_type_dict = query_datastore_performance_summary_request_type_instance.to_dict()
# create an instance of QueryDatastorePerformanceSummaryRequestType from a dict
query_datastore_performance_summary_request_type_form_dict = query_datastore_performance_summary_request_type.from_dict(query_datastore_performance_summary_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


