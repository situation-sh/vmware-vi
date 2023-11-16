# RemoveEntityPermissionRequestType

The parameters of *AuthorizationManager.RemoveEntityPermission*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entity** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | 
**user** | **str** | User or group for which the permission is defined.  | 
**is_group** | **bool** | True, if user refers to a group name; false, for a user name.  | 

## Example

```python
from vmware_vi.models.remove_entity_permission_request_type import RemoveEntityPermissionRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of RemoveEntityPermissionRequestType from a JSON string
remove_entity_permission_request_type_instance = RemoveEntityPermissionRequestType.from_json(json)
# print the JSON string representation of the object
print RemoveEntityPermissionRequestType.to_json()

# convert the object into a dict
remove_entity_permission_request_type_dict = remove_entity_permission_request_type_instance.to_dict()
# create an instance of RemoveEntityPermissionRequestType from a dict
remove_entity_permission_request_type_form_dict = remove_entity_permission_request_type.from_dict(remove_entity_permission_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


