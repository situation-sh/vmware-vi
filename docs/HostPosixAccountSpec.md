# HostPosixAccountSpec

This data object type contains a POSIX-specific parameter for local account creation. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**posix_id** | **int** | Deprecated as of vSphere API 5.1, this property is deprecated and is ignored.  The user ID or group ID of a specified account.  | [optional] 
**shell_access** | **bool** | Grants shell access.  As of vSphere API 5.1, this property is deprecated and is ignored. *HostLocalAccountManager.CreateUser* will always set this to true, and *HostLocalAccountManager.UpdateUser* will set it to true if it is already false. Also shell access is granted only to users with Administrator role on the root folder and no other non-Admin role on any other inventory object.  As of vSphere API 7.0.3.2, this property is no longer ignored and it must be true if a user with administrator permissions needs shell access. It can be set to true for other users only by administrators who themselves have this shell access. Administrators without shell access cannot change the passwords of users with shell access. Setting this property to false for user &#39;root&#39; has no effect.  If this property is not specified when creating a new user account then the default value depends on the following factors: if the calling user does not have shell access then it defaults to false; if the calling user has shell access then it defaults to true, unless overridden by host configuration settings.  | [optional] 

## Example

```python
from vmware_vi.models.host_posix_account_spec import HostPosixAccountSpec

# TODO update the JSON string below
json = "{}"
# create an instance of HostPosixAccountSpec from a JSON string
host_posix_account_spec_instance = HostPosixAccountSpec.from_json(json)
# print the JSON string representation of the object
print HostPosixAccountSpec.to_json()

# convert the object into a dict
host_posix_account_spec_dict = host_posix_account_spec_instance.to_dict()
# create an instance of HostPosixAccountSpec from a dict
host_posix_account_spec_form_dict = host_posix_account_spec.from_dict(host_posix_account_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


