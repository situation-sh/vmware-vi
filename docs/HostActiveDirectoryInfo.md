# HostActiveDirectoryInfo

The *HostActiveDirectoryInfo* data object describes ESX host membership in an Active Directory domain.  If the *HostAuthenticationStoreInfo*.*HostAuthenticationStoreInfo.enabled* property is <code>True</code>, the host is a member of a domain and the ESX Server will set the domain information properties.  ***Since:*** vSphere API 4.1 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**joined_domain** | **str** | The domain that this host joined.  ***Since:*** vSphere API 4.1  | [optional] 
**trusted_domain** | **List[str]** | List of domains with which the &lt;code&gt;joinedDomain&lt;/code&gt; has a trust.  The &lt;code&gt;joinedDomain&lt;/code&gt; is not included in the &lt;code&gt;trustedDomain&lt;/code&gt; list.  ***Since:*** vSphere API 4.1  | [optional] 
**domain_membership_status** | **str** | Health information about the domain membership.  See *HostActiveDirectoryInfoDomainMembershipStatus_enum*.  ***Since:*** vSphere API 4.1  | [optional] 
**smart_card_authentication_enabled** | **bool** | Whether local smart card authentication is enabled.  ***Since:*** vSphere API 6.0  | [optional] 

## Example

```python
from vmware_vi.models.host_active_directory_info import HostActiveDirectoryInfo

# TODO update the JSON string below
json = "{}"
# create an instance of HostActiveDirectoryInfo from a JSON string
host_active_directory_info_instance = HostActiveDirectoryInfo.from_json(json)
# print the JSON string representation of the object
print HostActiveDirectoryInfo.to_json()

# convert the object into a dict
host_active_directory_info_dict = host_active_directory_info_instance.to_dict()
# create an instance of HostActiveDirectoryInfo from a dict
host_active_directory_info_form_dict = host_active_directory_info.from_dict(host_active_directory_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


