# ArrayOfUserProfile

A boxed array of *UserProfile*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[UserProfile]**](UserProfile.md) |  | 

## Example

```python
from vmware_vi.models.array_of_user_profile import ArrayOfUserProfile

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfUserProfile from a JSON string
array_of_user_profile_instance = ArrayOfUserProfile.from_json(json)
# print the JSON string representation of the object
print ArrayOfUserProfile.to_json()

# convert the object into a dict
array_of_user_profile_dict = array_of_user_profile_instance.to_dict()
# create an instance of ArrayOfUserProfile from a dict
array_of_user_profile_form_dict = array_of_user_profile.from_dict(array_of_user_profile_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


