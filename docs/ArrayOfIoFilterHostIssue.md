# ArrayOfIoFilterHostIssue

A boxed array of *IoFilterHostIssue*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[IoFilterHostIssue]**](IoFilterHostIssue.md) |  | 

## Example

```python
from vmware_vi.models.array_of_io_filter_host_issue import ArrayOfIoFilterHostIssue

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfIoFilterHostIssue from a JSON string
array_of_io_filter_host_issue_instance = ArrayOfIoFilterHostIssue.from_json(json)
# print the JSON string representation of the object
print ArrayOfIoFilterHostIssue.to_json()

# convert the object into a dict
array_of_io_filter_host_issue_dict = array_of_io_filter_host_issue_instance.to_dict()
# create an instance of ArrayOfIoFilterHostIssue from a dict
array_of_io_filter_host_issue_form_dict = array_of_io_filter_host_issue.from_dict(array_of_io_filter_host_issue_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


