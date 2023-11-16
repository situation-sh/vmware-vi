# UserProfile

The *UserProfile* data object represents a user.  Use the *ApplyProfile.policy* list for access to configuration data for the user profile. Use the *ApplyProfile.property* list for access to subprofile configuration data, if any.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | Linkable identifier.  ***Since:*** vSphere API 4.0  | 

## Example

```python
from vmware_vi.models.user_profile import UserProfile

# TODO update the JSON string below
json = "{}"
# create an instance of UserProfile from a JSON string
user_profile_instance = UserProfile.from_json(json)
# print the JSON string representation of the object
print UserProfile.to_json()

# convert the object into a dict
user_profile_dict = user_profile_instance.to_dict()
# create an instance of UserProfile from a dict
user_profile_form_dict = user_profile.from_dict(user_profile_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


