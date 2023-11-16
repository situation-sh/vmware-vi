# HostAuthenticationManagerInfo

The *HostAuthenticationManagerInfo* data object provides access to authentication information for the ESX host.  ***Since:*** vSphere API 4.1 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auth_config** | [**List[HostAuthenticationStoreInfo]**](HostAuthenticationStoreInfo.md) | An array containing entries for local authentication and host Active Directory authentication. - *HostLocalAuthenticationInfo* - Local authentication is always enabled. - *HostActiveDirectoryInfo* - Host Active Directory authentication information   includes the name of the domain, membership status,   and a list of other domains trusted by the membership domain.    ***Since:*** vSphere API 4.1  | 

## Example

```python
from vmware_vi.models.host_authentication_manager_info import HostAuthenticationManagerInfo

# TODO update the JSON string below
json = "{}"
# create an instance of HostAuthenticationManagerInfo from a JSON string
host_authentication_manager_info_instance = HostAuthenticationManagerInfo.from_json(json)
# print the JSON string representation of the object
print HostAuthenticationManagerInfo.to_json()

# convert the object into a dict
host_authentication_manager_info_dict = host_authentication_manager_info_instance.to_dict()
# create an instance of HostAuthenticationManagerInfo from a dict
host_authentication_manager_info_form_dict = host_authentication_manager_info.from_dict(host_authentication_manager_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


