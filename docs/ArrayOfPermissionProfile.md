# ArrayOfPermissionProfile

A boxed array of *PermissionProfile*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[PermissionProfile]**](PermissionProfile.md) |  | 

## Example

```python
from vmware_vi.models.array_of_permission_profile import ArrayOfPermissionProfile

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfPermissionProfile from a JSON string
array_of_permission_profile_instance = ArrayOfPermissionProfile.from_json(json)
# print the JSON string representation of the object
print ArrayOfPermissionProfile.to_json()

# convert the object into a dict
array_of_permission_profile_dict = array_of_permission_profile_instance.to_dict()
# create an instance of ArrayOfPermissionProfile from a dict
array_of_permission_profile_form_dict = array_of_permission_profile.from_dict(array_of_permission_profile_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


