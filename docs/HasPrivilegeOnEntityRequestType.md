# HasPrivilegeOnEntityRequestType

The parameters of *AuthorizationManager.HasPrivilegeOnEntity*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entity** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | 
**session_id** | **str** | The session ID to check privileges for. A sesssion ID can be obtained from *UserSession.key*.  | 
**priv_id** | **List[str]** | The array of privilege IDs to check.  | [optional] 

## Example

```python
from vmware_vi.models.has_privilege_on_entity_request_type import HasPrivilegeOnEntityRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of HasPrivilegeOnEntityRequestType from a JSON string
has_privilege_on_entity_request_type_instance = HasPrivilegeOnEntityRequestType.from_json(json)
# print the JSON string representation of the object
print HasPrivilegeOnEntityRequestType.to_json()

# convert the object into a dict
has_privilege_on_entity_request_type_dict = has_privilege_on_entity_request_type_instance.to_dict()
# create an instance of HasPrivilegeOnEntityRequestType from a dict
has_privilege_on_entity_request_type_form_dict = has_privilege_on_entity_request_type.from_dict(has_privilege_on_entity_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


