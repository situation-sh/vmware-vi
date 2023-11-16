# PermissionProfile

The *PermissionProfile* data object represents the profile for a permission rule.  Use the *ApplyProfile.policy* list for access to configuration data for the permission profile. Use the *ApplyProfile.property* list for access to subprofiles, if any.  ***Since:*** vSphere API 4.1 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** |  | 

## Example

```python
from vmware_vi.models.permission_profile import PermissionProfile

# TODO update the JSON string below
json = "{}"
# create an instance of PermissionProfile from a JSON string
permission_profile_instance = PermissionProfile.from_json(json)
# print the JSON string representation of the object
print PermissionProfile.to_json()

# convert the object into a dict
permission_profile_dict = permission_profile_instance.to_dict()
# create an instance of PermissionProfile from a dict
permission_profile_form_dict = permission_profile.from_dict(permission_profile_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


