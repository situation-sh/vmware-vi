# AuthorizationRole

This data object type specifies a collection of privileges used to grant access to users on managed entities. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**role_id** | **int** | Unique role identifier.  | 
**system** | **bool** | Whether or not the role is system-defined.  System-defined roles cannot be changed.  | 
**name** | **str** | System-defined or user-defined role name.  | 
**info** | [**Description**](Description.md) |  | 
**privilege** | **List[str]** | Privileges provided by this role, by privilege identifier.  | [optional] 

## Example

```python
from vmware_vi.models.authorization_role import AuthorizationRole

# TODO update the JSON string below
json = "{}"
# create an instance of AuthorizationRole from a JSON string
authorization_role_instance = AuthorizationRole.from_json(json)
# print the JSON string representation of the object
print AuthorizationRole.to_json()

# convert the object into a dict
authorization_role_dict = authorization_role_instance.to_dict()
# create an instance of AuthorizationRole from a dict
authorization_role_form_dict = authorization_role.from_dict(authorization_role_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


