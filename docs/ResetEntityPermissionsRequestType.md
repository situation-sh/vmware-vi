# ResetEntityPermissionsRequestType

The parameters of *AuthorizationManager.ResetEntityPermissions*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entity** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | 
**permission** | [**List[Permission]**](Permission.md) | The list of Permission objects that define the new rules for access to the entity and potentially entities below it. If the list is empty, all permissions on the entity are removed.  | [optional] 

## Example

```python
from vmware_vi.models.reset_entity_permissions_request_type import ResetEntityPermissionsRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of ResetEntityPermissionsRequestType from a JSON string
reset_entity_permissions_request_type_instance = ResetEntityPermissionsRequestType.from_json(json)
# print the JSON string representation of the object
print ResetEntityPermissionsRequestType.to_json()

# convert the object into a dict
reset_entity_permissions_request_type_dict = reset_entity_permissions_request_type_instance.to_dict()
# create an instance of ResetEntityPermissionsRequestType from a dict
reset_entity_permissions_request_type_form_dict = reset_entity_permissions_request_type.from_dict(reset_entity_permissions_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


