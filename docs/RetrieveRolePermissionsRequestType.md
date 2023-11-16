# RetrieveRolePermissionsRequestType

The parameters of *AuthorizationManager.RetrieveRolePermissions*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**role_id** | **int** |  | 

## Example

```python
from vmware_vi.models.retrieve_role_permissions_request_type import RetrieveRolePermissionsRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of RetrieveRolePermissionsRequestType from a JSON string
retrieve_role_permissions_request_type_instance = RetrieveRolePermissionsRequestType.from_json(json)
# print the JSON string representation of the object
print RetrieveRolePermissionsRequestType.to_json()

# convert the object into a dict
retrieve_role_permissions_request_type_dict = retrieve_role_permissions_request_type_instance.to_dict()
# create an instance of RetrieveRolePermissionsRequestType from a dict
retrieve_role_permissions_request_type_form_dict = retrieve_role_permissions_request_type.from_dict(retrieve_role_permissions_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


