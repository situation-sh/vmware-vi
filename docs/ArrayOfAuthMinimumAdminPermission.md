# ArrayOfAuthMinimumAdminPermission

A boxed array of *AuthMinimumAdminPermission*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[AuthMinimumAdminPermission]**](AuthMinimumAdminPermission.md) |  | 

## Example

```python
from vmware_vi.models.array_of_auth_minimum_admin_permission import ArrayOfAuthMinimumAdminPermission

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfAuthMinimumAdminPermission from a JSON string
array_of_auth_minimum_admin_permission_instance = ArrayOfAuthMinimumAdminPermission.from_json(json)
# print the JSON string representation of the object
print ArrayOfAuthMinimumAdminPermission.to_json()

# convert the object into a dict
array_of_auth_minimum_admin_permission_dict = array_of_auth_minimum_admin_permission_instance.to_dict()
# create an instance of ArrayOfAuthMinimumAdminPermission from a dict
array_of_auth_minimum_admin_permission_form_dict = array_of_auth_minimum_admin_permission.from_dict(array_of_auth_minimum_admin_permission_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


