# ArrayOfFtIssuesOnHost

A boxed array of *FtIssuesOnHost*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[FtIssuesOnHost]**](FtIssuesOnHost.md) |  | 

## Example

```python
from vmware_vi.models.array_of_ft_issues_on_host import ArrayOfFtIssuesOnHost

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfFtIssuesOnHost from a JSON string
array_of_ft_issues_on_host_instance = ArrayOfFtIssuesOnHost.from_json(json)
# print the JSON string representation of the object
print ArrayOfFtIssuesOnHost.to_json()

# convert the object into a dict
array_of_ft_issues_on_host_dict = array_of_ft_issues_on_host_instance.to_dict()
# create an instance of ArrayOfFtIssuesOnHost from a dict
array_of_ft_issues_on_host_form_dict = array_of_ft_issues_on_host.from_dict(array_of_ft_issues_on_host_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


