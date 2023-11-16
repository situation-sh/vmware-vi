# SetEntityPermissionsRequestType

The parameters of *AuthorizationManager.SetEntityPermissions*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entity** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | 
**permission** | [**List[Permission]**](Permission.md) | An array of specifications for permissions on the entity.  | [optional] 

## Example

```python
from vmware_vi.models.set_entity_permissions_request_type import SetEntityPermissionsRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of SetEntityPermissionsRequestType from a JSON string
set_entity_permissions_request_type_instance = SetEntityPermissionsRequestType.from_json(json)
# print the JSON string representation of the object
print SetEntityPermissionsRequestType.to_json()

# convert the object into a dict
set_entity_permissions_request_type_dict = set_entity_permissions_request_type_instance.to_dict()
# create an instance of SetEntityPermissionsRequestType from a dict
set_entity_permissions_request_type_form_dict = set_entity_permissions_request_type.from_dict(set_entity_permissions_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


