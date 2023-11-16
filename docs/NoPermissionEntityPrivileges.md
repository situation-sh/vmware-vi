# NoPermissionEntityPrivileges

Entity and privileges for the entity 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entity** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | 
**privilege_ids** | **List[str]** |  | [optional] 

## Example

```python
from vmware_vi.models.no_permission_entity_privileges import NoPermissionEntityPrivileges

# TODO update the JSON string below
json = "{}"
# create an instance of NoPermissionEntityPrivileges from a JSON string
no_permission_entity_privileges_instance = NoPermissionEntityPrivileges.from_json(json)
# print the JSON string representation of the object
print NoPermissionEntityPrivileges.to_json()

# convert the object into a dict
no_permission_entity_privileges_dict = no_permission_entity_privileges_instance.to_dict()
# create an instance of NoPermissionEntityPrivileges from a dict
no_permission_entity_privileges_form_dict = no_permission_entity_privileges.from_dict(no_permission_entity_privileges_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


