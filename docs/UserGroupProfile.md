# UserGroupProfile

The *UserGroupProfile* data object represents a user group.  Use the *ApplyProfile.policy* list for access to configuration data for the user group profile. Use the *ApplyProfile.property* list for access to subprofile configuration data, if any.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | Linkable identifier.  ***Since:*** vSphere API 4.0  | 

## Example

```python
from vmware_vi.models.user_group_profile import UserGroupProfile

# TODO update the JSON string below
json = "{}"
# create an instance of UserGroupProfile from a JSON string
user_group_profile_instance = UserGroupProfile.from_json(json)
# print the JSON string representation of the object
print UserGroupProfile.to_json()

# convert the object into a dict
user_group_profile_dict = user_group_profile_instance.to_dict()
# create an instance of UserGroupProfile from a dict
user_group_profile_form_dict = user_group_profile.from_dict(user_group_profile_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


