# ArrayOfIoFilterQueryIssueResult

A boxed array of *IoFilterQueryIssueResult*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[IoFilterQueryIssueResult]**](IoFilterQueryIssueResult.md) |  | 

## Example

```python
from vmware_vi.models.array_of_io_filter_query_issue_result import ArrayOfIoFilterQueryIssueResult

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfIoFilterQueryIssueResult from a JSON string
array_of_io_filter_query_issue_result_instance = ArrayOfIoFilterQueryIssueResult.from_json(json)
# print the JSON string representation of the object
print ArrayOfIoFilterQueryIssueResult.to_json()

# convert the object into a dict
array_of_io_filter_query_issue_result_dict = array_of_io_filter_query_issue_result_instance.to_dict()
# create an instance of ArrayOfIoFilterQueryIssueResult from a dict
array_of_io_filter_query_issue_result_form_dict = array_of_io_filter_query_issue_result.from_dict(array_of_io_filter_query_issue_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


