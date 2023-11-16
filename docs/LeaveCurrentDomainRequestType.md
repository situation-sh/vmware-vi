# LeaveCurrentDomainRequestType

The parameters of *HostActiveDirectoryAuthentication.LeaveCurrentDomain_Task*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**force** | **bool** | If &lt;code&gt;True&lt;/code&gt;, any existing permissions on managed entities for Active Directory users will be deleted. If &lt;code&gt;False&lt;/code&gt; and such permissions exist, the operation will fail.  | 

## Example

```python
from vmware_vi.models.leave_current_domain_request_type import LeaveCurrentDomainRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of LeaveCurrentDomainRequestType from a JSON string
leave_current_domain_request_type_instance = LeaveCurrentDomainRequestType.from_json(json)
# print the JSON string representation of the object
print LeaveCurrentDomainRequestType.to_json()

# convert the object into a dict
leave_current_domain_request_type_dict = leave_current_domain_request_type_instance.to_dict()
# create an instance of LeaveCurrentDomainRequestType from a dict
leave_current_domain_request_type_form_dict = leave_current_domain_request_type.from_dict(leave_current_domain_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


