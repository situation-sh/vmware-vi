# QueryVsanStatisticsRequestType

The parameters of *HostVsanInternalSystem.QueryVsanStatistics*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**labels** | **List[str]** | List of labels of counters to retrieve.  | 

## Example

```python
from vmware_vi.models.query_vsan_statistics_request_type import QueryVsanStatisticsRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of QueryVsanStatisticsRequestType from a JSON string
query_vsan_statistics_request_type_instance = QueryVsanStatisticsRequestType.from_json(json)
# print the JSON string representation of the object
print QueryVsanStatisticsRequestType.to_json()

# convert the object into a dict
query_vsan_statistics_request_type_dict = query_vsan_statistics_request_type_instance.to_dict()
# create an instance of QueryVsanStatisticsRequestType from a dict
query_vsan_statistics_request_type_form_dict = query_vsan_statistics_request_type.from_dict(query_vsan_statistics_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


