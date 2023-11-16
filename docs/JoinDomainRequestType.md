# JoinDomainRequestType

The parameters of *HostActiveDirectoryAuthentication.JoinDomain_Task*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domain_name** | **str** | Name of the domain to be joined.  | 
**user_name** | **str** | Name for an Active Directory account that has the authority to add hosts to the domain.  | 
**password** | **str** | Password for the &lt;code&gt;userName&lt;/code&gt; account.  | 

## Example

```python
from vmware_vi.models.join_domain_request_type import JoinDomainRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of JoinDomainRequestType from a JSON string
join_domain_request_type_instance = JoinDomainRequestType.from_json(json)
# print the JSON string representation of the object
print JoinDomainRequestType.to_json()

# convert the object into a dict
join_domain_request_type_dict = join_domain_request_type_instance.to_dict()
# create an instance of JoinDomainRequestType from a dict
join_domain_request_type_form_dict = join_domain_request_type.from_dict(join_domain_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


