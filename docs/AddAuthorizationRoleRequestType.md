# AddAuthorizationRoleRequestType

The parameters of *AuthorizationManager.AddAuthorizationRole*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the new role.  | 
**priv_ids** | **List[str]** | List of privileges to assign to the role.  | [optional] 

## Example

```python
from vmware_vi.models.add_authorization_role_request_type import AddAuthorizationRoleRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of AddAuthorizationRoleRequestType from a JSON string
add_authorization_role_request_type_instance = AddAuthorizationRoleRequestType.from_json(json)
# print the JSON string representation of the object
print AddAuthorizationRoleRequestType.to_json()

# convert the object into a dict
add_authorization_role_request_type_dict = add_authorization_role_request_type_instance.to_dict()
# create an instance of AddAuthorizationRoleRequestType from a dict
add_authorization_role_request_type_form_dict = add_authorization_role_request_type.from_dict(add_authorization_role_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


