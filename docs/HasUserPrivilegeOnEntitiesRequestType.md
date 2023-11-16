# HasUserPrivilegeOnEntitiesRequestType

The parameters of *AuthorizationManager.HasUserPrivilegeOnEntities*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entities** | [**List[ManagedObjectReference]**](ManagedObjectReference.md) | are the managed objects to check privileges on. If they refer to managed objects that are not managed entities the privilege check will be done on the root folder.  ***Required privileges:*** System.View  | 
**user_name** | **str** | is the name of the user to check privileges for. Both UPN and PreWindows2000LogonName user name formats are supported.  | 
**priv_id** | **List[str]** | is the set of privileges to check for  | [optional] 

## Example

```python
from vmware_vi.models.has_user_privilege_on_entities_request_type import HasUserPrivilegeOnEntitiesRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of HasUserPrivilegeOnEntitiesRequestType from a JSON string
has_user_privilege_on_entities_request_type_instance = HasUserPrivilegeOnEntitiesRequestType.from_json(json)
# print the JSON string representation of the object
print HasUserPrivilegeOnEntitiesRequestType.to_json()

# convert the object into a dict
has_user_privilege_on_entities_request_type_dict = has_user_privilege_on_entities_request_type_instance.to_dict()
# create an instance of HasUserPrivilegeOnEntitiesRequestType from a dict
has_user_privilege_on_entities_request_type_form_dict = has_user_privilege_on_entities_request_type.from_dict(has_user_privilege_on_entities_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


