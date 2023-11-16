# ArrayOfAuthenticationProfile

A boxed array of *AuthenticationProfile*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[AuthenticationProfile]**](AuthenticationProfile.md) |  | 

## Example

```python
from vmware_vi.models.array_of_authentication_profile import ArrayOfAuthenticationProfile

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfAuthenticationProfile from a JSON string
array_of_authentication_profile_instance = ArrayOfAuthenticationProfile.from_json(json)
# print the JSON string representation of the object
print ArrayOfAuthenticationProfile.to_json()

# convert the object into a dict
array_of_authentication_profile_dict = array_of_authentication_profile_instance.to_dict()
# create an instance of ArrayOfAuthenticationProfile from a dict
array_of_authentication_profile_form_dict = array_of_authentication_profile.from_dict(array_of_authentication_profile_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


