# IoFilterQueryIssueResult

Result for *IoFilterManager.QueryIoFilterIssues*.  ***Since:*** vSphere API 6.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**op_type** | **str** | The type of the operation performed on the IO Filter.  The set of possible values are defined in *IoFilterOperation_enum*.  ***Since:*** vSphere API 6.0  | 
**host_issue** | [**List[IoFilterHostIssue]**](IoFilterHostIssue.md) | The issues on hosts.  ***Since:*** vSphere API 6.0  | [optional] 

## Example

```python
from vmware_vi.models.io_filter_query_issue_result import IoFilterQueryIssueResult

# TODO update the JSON string below
json = "{}"
# create an instance of IoFilterQueryIssueResult from a JSON string
io_filter_query_issue_result_instance = IoFilterQueryIssueResult.from_json(json)
# print the JSON string representation of the object
print IoFilterQueryIssueResult.to_json()

# convert the object into a dict
io_filter_query_issue_result_dict = io_filter_query_issue_result_instance.to_dict()
# create an instance of IoFilterQueryIssueResult from a dict
io_filter_query_issue_result_form_dict = io_filter_query_issue_result.from_dict(io_filter_query_issue_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


