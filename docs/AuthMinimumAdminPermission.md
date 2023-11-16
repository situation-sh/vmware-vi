# AuthMinimumAdminPermission

This fault is thrown when the requested change would result in a loss of full administrative privileges for at least one user or group. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.auth_minimum_admin_permission import AuthMinimumAdminPermission

# TODO update the JSON string below
json = "{}"
# create an instance of AuthMinimumAdminPermission from a JSON string
auth_minimum_admin_permission_instance = AuthMinimumAdminPermission.from_json(json)
# print the JSON string representation of the object
print AuthMinimumAdminPermission.to_json()

# convert the object into a dict
auth_minimum_admin_permission_dict = auth_minimum_admin_permission_instance.to_dict()
# create an instance of AuthMinimumAdminPermission from a dict
auth_minimum_admin_permission_form_dict = auth_minimum_admin_permission.from_dict(auth_minimum_admin_permission_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


