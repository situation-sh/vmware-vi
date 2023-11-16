# ActiveDirectoryProfile

The *ActiveDirectoryProfile* data object represents Active Directory configuration.  Use the *ApplyProfile.policy* list for access to configuration data for the Active Directory profile. Use the *ApplyProfile.property* list for access to subprofiles, if any.  ***Since:*** vSphere API 4.1 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.active_directory_profile import ActiveDirectoryProfile

# TODO update the JSON string below
json = "{}"
# create an instance of ActiveDirectoryProfile from a JSON string
active_directory_profile_instance = ActiveDirectoryProfile.from_json(json)
# print the JSON string representation of the object
print ActiveDirectoryProfile.to_json()

# convert the object into a dict
active_directory_profile_dict = active_directory_profile_instance.to_dict()
# create an instance of ActiveDirectoryProfile from a dict
active_directory_profile_form_dict = active_directory_profile.from_dict(active_directory_profile_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


