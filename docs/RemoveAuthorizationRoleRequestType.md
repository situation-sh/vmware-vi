# RemoveAuthorizationRoleRequestType

The parameters of *AuthorizationManager.RemoveAuthorizationRole*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**role_id** | **int** |  | 
**fail_if_used** | **bool** | If true, prevents the role from being removed if any permissions are using it.  | 

## Example

```python
from vmware_vi.models.remove_authorization_role_request_type import RemoveAuthorizationRoleRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of RemoveAuthorizationRoleRequestType from a JSON string
remove_authorization_role_request_type_instance = RemoveAuthorizationRoleRequestType.from_json(json)
# print the JSON string representation of the object
print RemoveAuthorizationRoleRequestType.to_json()

# convert the object into a dict
remove_authorization_role_request_type_dict = remove_authorization_role_request_type_instance.to_dict()
# create an instance of RemoveAuthorizationRoleRequestType from a dict
remove_authorization_role_request_type_form_dict = remove_authorization_role_request_type.from_dict(remove_authorization_role_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


