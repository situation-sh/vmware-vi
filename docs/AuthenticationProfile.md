# AuthenticationProfile

The *AuthenticationProfile* data object represents the host configuration for authentication.  If a profile plug-in defines policies or subprofiles, use the *ApplyProfile.policy* or *ApplyProfile.property* list to access the additional configuration data.  ***Since:*** vSphere API 4.1 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active_directory** | [**ActiveDirectoryProfile**](ActiveDirectoryProfile.md) |  | [optional] 

## Example

```python
from vmware_vi.models.authentication_profile import AuthenticationProfile

# TODO update the JSON string below
json = "{}"
# create an instance of AuthenticationProfile from a JSON string
authentication_profile_instance = AuthenticationProfile.from_json(json)
# print the JSON string representation of the object
print AuthenticationProfile.to_json()

# convert the object into a dict
authentication_profile_dict = authentication_profile_instance.to_dict()
# create an instance of AuthenticationProfile from a dict
authentication_profile_form_dict = authentication_profile.from_dict(authentication_profile_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


