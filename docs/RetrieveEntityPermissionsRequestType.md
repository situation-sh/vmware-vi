# RetrieveEntityPermissionsRequestType

The parameters of *AuthorizationManager.RetrieveEntityPermissions*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entity** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | 
**inherited** | **bool** | Whether or not to include propagating permissions defined by parent entities.  | 

## Example

```python
from vmware_vi.models.retrieve_entity_permissions_request_type import RetrieveEntityPermissionsRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of RetrieveEntityPermissionsRequestType from a JSON string
retrieve_entity_permissions_request_type_instance = RetrieveEntityPermissionsRequestType.from_json(json)
# print the JSON string representation of the object
print RetrieveEntityPermissionsRequestType.to_json()

# convert the object into a dict
retrieve_entity_permissions_request_type_dict = retrieve_entity_permissions_request_type_instance.to_dict()
# create an instance of RetrieveEntityPermissionsRequestType from a dict
retrieve_entity_permissions_request_type_form_dict = retrieve_entity_permissions_request_type.from_dict(retrieve_entity_permissions_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


