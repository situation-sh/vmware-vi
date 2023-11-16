# UpdateAuthorizationRoleRequestType

The parameters of *AuthorizationManager.UpdateAuthorizationRole*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**role_id** | **int** | The ID of the role that is updated.  | 
**new_name** | **str** | The new name for the role.  | 
**priv_ids** | **List[str]** | The new set of privileges to assign to the role.  | [optional] 

## Example

```python
from vmware_vi.models.update_authorization_role_request_type import UpdateAuthorizationRoleRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateAuthorizationRoleRequestType from a JSON string
update_authorization_role_request_type_instance = UpdateAuthorizationRoleRequestType.from_json(json)
# print the JSON string representation of the object
print UpdateAuthorizationRoleRequestType.to_json()

# convert the object into a dict
update_authorization_role_request_type_dict = update_authorization_role_request_type_instance.to_dict()
# create an instance of UpdateAuthorizationRoleRequestType from a dict
update_authorization_role_request_type_form_dict = update_authorization_role_request_type.from_dict(update_authorization_role_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


