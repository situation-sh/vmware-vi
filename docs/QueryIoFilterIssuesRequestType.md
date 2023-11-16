# QueryIoFilterIssuesRequestType

The parameters of *IoFilterManager.QueryIoFilterIssues*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filter_id** | **str** | The filter.  | 
**comp_res** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | 

## Example

```python
from vmware_vi.models.query_io_filter_issues_request_type import QueryIoFilterIssuesRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of QueryIoFilterIssuesRequestType from a JSON string
query_io_filter_issues_request_type_instance = QueryIoFilterIssuesRequestType.from_json(json)
# print the JSON string representation of the object
print QueryIoFilterIssuesRequestType.to_json()

# convert the object into a dict
query_io_filter_issues_request_type_dict = query_io_filter_issues_request_type_instance.to_dict()
# create an instance of QueryIoFilterIssuesRequestType from a dict
query_io_filter_issues_request_type_form_dict = query_io_filter_issues_request_type.from_dict(query_io_filter_issues_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


