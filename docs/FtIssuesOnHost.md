# FtIssuesOnHost

The FtIssuesOnHost fault reports issues that prevent a particular host from being used as the register or power on host for a Fault Tolerance secondary virtual machine  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**host** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | 
**host_name** | **str** | Name for the host which has Fault Tolerance issues.  ***Since:*** vSphere API 4.0  | 
**errors** | [**List[MethodFault]**](MethodFault.md) | Information on the details of the Fault Tolerance issues  ***Since:*** vSphere API 4.0  | [optional] 

## Example

```python
from vmware_vi.models.ft_issues_on_host import FtIssuesOnHost

# TODO update the JSON string below
json = "{}"
# create an instance of FtIssuesOnHost from a JSON string
ft_issues_on_host_instance = FtIssuesOnHost.from_json(json)
# print the JSON string representation of the object
print FtIssuesOnHost.to_json()

# convert the object into a dict
ft_issues_on_host_dict = ft_issues_on_host_instance.to_dict()
# create an instance of FtIssuesOnHost from a dict
ft_issues_on_host_form_dict = ft_issues_on_host.from_dict(ft_issues_on_host_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


