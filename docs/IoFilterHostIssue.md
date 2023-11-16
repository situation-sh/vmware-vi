# IoFilterHostIssue

The issues on a host.  ***Since:*** vSphere API 6.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**host** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | 
**issue** | [**List[MethodFault]**](MethodFault.md) | The issues.  ***Since:*** vSphere API 6.0  | 

## Example

```python
from vmware_vi.models.io_filter_host_issue import IoFilterHostIssue

# TODO update the JSON string below
json = "{}"
# create an instance of IoFilterHostIssue from a JSON string
io_filter_host_issue_instance = IoFilterHostIssue.from_json(json)
# print the JSON string representation of the object
print IoFilterHostIssue.to_json()

# convert the object into a dict
io_filter_host_issue_dict = io_filter_host_issue_instance.to_dict()
# create an instance of IoFilterHostIssue from a dict
io_filter_host_issue_form_dict = io_filter_host_issue.from_dict(io_filter_host_issue_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


