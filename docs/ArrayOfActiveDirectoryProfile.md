# ArrayOfActiveDirectoryProfile

A boxed array of *ActiveDirectoryProfile*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[ActiveDirectoryProfile]**](ActiveDirectoryProfile.md) |  | 

## Example

```python
from vmware_vi.models.array_of_active_directory_profile import ArrayOfActiveDirectoryProfile

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfActiveDirectoryProfile from a JSON string
array_of_active_directory_profile_instance = ArrayOfActiveDirectoryProfile.from_json(json)
# print the JSON string representation of the object
print ArrayOfActiveDirectoryProfile.to_json()

# convert the object into a dict
array_of_active_directory_profile_dict = array_of_active_directory_profile_instance.to_dict()
# create an instance of ArrayOfActiveDirectoryProfile from a dict
array_of_active_directory_profile_form_dict = array_of_active_directory_profile.from_dict(array_of_active_directory_profile_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


