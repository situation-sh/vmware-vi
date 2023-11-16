# NoPermission

Thrown when an operation is denied because of privileges not held on managed object(s). 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | [optional] 
**privilege_id** | **str** | Deprecated as of vSphere 8.0, use the *NoPermission.missingPrivileges* field.  The privilege identifier required  | [optional] 
**missing_privileges** | [**List[NoPermissionEntityPrivileges]**](NoPermissionEntityPrivileges.md) | List of entities and missing privileges for each entity  | [optional] 

## Example

```python
from vmware_vi.models.no_permission import NoPermission

# TODO update the JSON string below
json = "{}"
# create an instance of NoPermission from a JSON string
no_permission_instance = NoPermission.from_json(json)
# print the JSON string representation of the object
print NoPermission.to_json()

# convert the object into a dict
no_permission_dict = no_permission_instance.to_dict()
# create an instance of NoPermission from a dict
no_permission_form_dict = no_permission.from_dict(no_permission_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


