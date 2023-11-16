# HasPrivilegeOnEntitiesRequestType

The parameters of *AuthorizationManager.HasPrivilegeOnEntities*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entity** | [**List[ManagedObjectReference]**](ManagedObjectReference.md) | The set of entities on which the privileges are checked.  ***Required privileges:*** System.Read  Refers instances of *ManagedEntity*.  | 
**session_id** | **str** | The session ID to check privileges for. A sesssion ID can be obtained from *UserSession.key*.  | 
**priv_id** | **List[str]** | The array of privilege IDs to check.  | [optional] 

## Example

```python
from vmware_vi.models.has_privilege_on_entities_request_type import HasPrivilegeOnEntitiesRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of HasPrivilegeOnEntitiesRequestType from a JSON string
has_privilege_on_entities_request_type_instance = HasPrivilegeOnEntitiesRequestType.from_json(json)
# print the JSON string representation of the object
print HasPrivilegeOnEntitiesRequestType.to_json()

# convert the object into a dict
has_privilege_on_entities_request_type_dict = has_privilege_on_entities_request_type_instance.to_dict()
# create an instance of HasPrivilegeOnEntitiesRequestType from a dict
has_privilege_on_entities_request_type_form_dict = has_privilege_on_entities_request_type.from_dict(has_privilege_on_entities_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


