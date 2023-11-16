# HostApplyProfile

The *HostApplyProfile* data object provides access to subprofiles that contain configuration data for different host capabilities.  The Profile Engine will use any configuration data that you supply to overwrite the host configuration. See the *HostProfile.ExecuteHostProfile* and *HostProfileManager.ApplyHostConfig_Task* methods.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**memory** | [**HostMemoryProfile**](HostMemoryProfile.md) |  | [optional] 
**storage** | [**StorageProfile**](StorageProfile.md) |  | [optional] 
**network** | [**NetworkProfile**](NetworkProfile.md) |  | [optional] 
**datetime** | [**DateTimeProfile**](DateTimeProfile.md) |  | [optional] 
**firewall** | [**FirewallProfile**](FirewallProfile.md) |  | [optional] 
**security** | [**SecurityProfile**](SecurityProfile.md) |  | [optional] 
**service** | [**List[ServiceProfile]**](ServiceProfile.md) | Host configuration for services.  Use the *ServiceProfile.key* property to access a subprofile in the list.  ***Since:*** vSphere API 4.0  | [optional] 
**option** | [**List[OptionProfile]**](OptionProfile.md) | List of subprofiles representing advanced configuration options.  Use the *OptionProfile.key* property to access a subprofile in the list.  ***Since:*** vSphere API 4.0  | [optional] 
**user_account** | [**List[UserProfile]**](UserProfile.md) | List of subprofiles for user accounts to be configured on the host.  Use the *UserProfile.key* property to access a subprofile in the list.  ***Since:*** vSphere API 4.0  | [optional] 
**usergroup_account** | [**List[UserGroupProfile]**](UserGroupProfile.md) | List of subprofiles for user groups to be configured on the host.  Use the *UserGroupProfile.key* property to access a subprofile in the list.  ***Since:*** vSphere API 4.0  | [optional] 
**authentication** | [**AuthenticationProfile**](AuthenticationProfile.md) |  | [optional] 

## Example

```python
from vmware_vi.models.host_apply_profile import HostApplyProfile

# TODO update the JSON string below
json = "{}"
# create an instance of HostApplyProfile from a JSON string
host_apply_profile_instance = HostApplyProfile.from_json(json)
# print the JSON string representation of the object
print HostApplyProfile.to_json()

# convert the object into a dict
host_apply_profile_dict = host_apply_profile_instance.to_dict()
# create an instance of HostApplyProfile from a dict
host_apply_profile_form_dict = host_apply_profile.from_dict(host_apply_profile_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


