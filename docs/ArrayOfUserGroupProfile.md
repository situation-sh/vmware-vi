# ArrayOfUserGroupProfile

A boxed array of *UserGroupProfile*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[UserGroupProfile]**](UserGroupProfile.md) |  | 

## Example

```python
from vmware_vi.models.array_of_user_group_profile import ArrayOfUserGroupProfile

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfUserGroupProfile from a JSON string
array_of_user_group_profile_instance = ArrayOfUserGroupProfile.from_json(json)
# print the JSON string representation of the object
print ArrayOfUserGroupProfile.to_json()

# convert the object into a dict
array_of_user_group_profile_dict = array_of_user_group_profile_instance.to_dict()
# create an instance of ArrayOfUserGroupProfile from a dict
array_of_user_group_profile_form_dict = array_of_user_group_profile.from_dict(array_of_user_group_profile_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


