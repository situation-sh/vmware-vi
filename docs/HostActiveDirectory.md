# HostActiveDirectory

The *HostActiveDirectory* data object contains Active Directory configuration information for an ESX host.  The vSphere API supports Microsoft Active Directory management of authentication for ESX hosts. To integrate an ESX host into an Active Directory environment, you use an Active Directory account that has the authority to add a computer to a domain. The ESX Server locates the Active Directory domain controller. When you use the host profile to configure authentication for an ESX host, you specify the configuration operation (add or remove). To add the host to a domain, specify the domain, and the authorized Active Directory account user name and password. You do not need to specify these parameters to remove the host from a domain because the host has the information it needs to perform the operation. When you call *HostProfileManager.ApplyHostConfig_Task* to apply the configuration, the ESX Server will call the appropriate method (*HostActiveDirectoryAuthentication.JoinDomain_Task* or *HostActiveDirectoryAuthentication.LeaveCurrentDomain_Task*) on your behalf.  Before you call the method to apply the host profile, check to see that the *HostAuthenticationManager*.*HostAuthenticationManager.supportedStore* array contains a *HostActiveDirectoryAuthentication* object. The presence of the Active Directory authentication object indicates that a host is capable of joining a domain. However, if you try to add a host to a domain when the *HostAuthenticationStoreInfo*.*HostAuthenticationStoreInfo.enabled* property is <code>True</code>, the join method will throw a fault.  As an alternative to using the host profile to configure Active Directory authentication for an ESX host, your vSphere client application can call the *HostActiveDirectoryAuthentication* join and leave methods directly to add the host to or remove the host from a domain.  To take advantage of ESX host membership in an Active Directory domain, grant permissions on the ESX host to users and groups in Active Directory who should have direct access to management of the ESX host. Use the *UserDirectory*.*UserDirectory.RetrieveUserGroups* method to obtain information about Active Directory users and groups. After retrieving the Active Directory data, you can use the *AuthorizationManager*.*AuthorizationManager.SetEntityPermissions* method to set the *Permission.principal* property to the appropriate user or group.  By default, the ESX host assigns the Administrator role to the \"ESX Admins\" group. If the group does not exist when the host joins the domain, the host will not assign the role. In this case, you must create the \"ESX Admins\" group in the Active Directory. The host will periodically check the domain controller for the group and will assign the role when the group exists.  ***Since:*** vSphere API 4.1 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**change_operation** | **str** | Configuration change operation to apply to the host.  You can specify the following values: - *add*:   Add the host to the domain. The ESX Server will use the   *HostActiveDirectorySpec* information   (domain, account user name and password) to call   *HostActiveDirectoryAuthentication.JoinDomain_Task* and optionally   configure smart card authentication by calling   *HostActiveDirectoryAuthentication.DisableSmartCardAuthentication*   and replacing the trust anchors with those provided. - *remove*:   Remove the host from its current domain.   The ESX Server will call   *HostActiveDirectoryAuthentication.LeaveCurrentDomain_Task*, specifying   &lt;code&gt;True&lt;/code&gt; for the &lt;code&gt;force&lt;/code&gt; parameter to delete   existing permissions.   *HostActiveDirectoryAuthentication.DisableSmartCardAuthentication*   is also called if smart card authentication is enabled and trust   anchors are removed.    See also *HostConfigChangeOperation_enum*.  ***Since:*** vSphere API 4.1  | 
**spec** | [**HostActiveDirectorySpec**](HostActiveDirectorySpec.md) |  | [optional] 

## Example

```python
from vmware_vi.models.host_active_directory import HostActiveDirectory

# TODO update the JSON string below
json = "{}"
# create an instance of HostActiveDirectory from a JSON string
host_active_directory_instance = HostActiveDirectory.from_json(json)
# print the JSON string representation of the object
print HostActiveDirectory.to_json()

# convert the object into a dict
host_active_directory_dict = host_active_directory_instance.to_dict()
# create an instance of HostActiveDirectory from a dict
host_active_directory_form_dict = host_active_directory.from_dict(host_active_directory_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


