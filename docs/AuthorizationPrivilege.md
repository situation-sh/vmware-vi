# AuthorizationPrivilege

This data object type provides access to some aspect of the system.  Privileges are generally independent. This means a user with a privilege usually can perform an associated set of actions without needing any additional supporting privileges.  Within each product version, privileges do not change. See *AuthorizationDescription* for detailed information on the privileges defined by the system. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**priv_id** | **str** | Unique identifier.  | 
**on_parent** | **bool** | Determines whether or not the privilege is applied on the parent entity.  | 
**name** | **str** | Privilege name.  | 
**priv_group_name** | **str** | Group name.  | 

## Example

```python
from vmware_vi.models.authorization_privilege import AuthorizationPrivilege

# TODO update the JSON string below
json = "{}"
# create an instance of AuthorizationPrivilege from a JSON string
authorization_privilege_instance = AuthorizationPrivilege.from_json(json)
# print the JSON string representation of the object
print AuthorizationPrivilege.to_json()

# convert the object into a dict
authorization_privilege_dict = authorization_privilege_instance.to_dict()
# create an instance of AuthorizationPrivilege from a dict
authorization_privilege_form_dict = authorization_privilege.from_dict(authorization_privilege_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


