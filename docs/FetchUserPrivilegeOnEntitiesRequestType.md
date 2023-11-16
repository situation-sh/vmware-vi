# FetchUserPrivilegeOnEntitiesRequestType

The parameters of *AuthorizationManager.FetchUserPrivilegeOnEntities*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entities** | [**List[ManagedObjectReference]**](ManagedObjectReference.md) | are the entities to retrieve privileges on  ***Required privileges:*** System.View  Refers instances of *ManagedEntity*.  | 
**user_name** | **str** | is the user to retrieve privileges for  | 

## Example

```python
from vmware_vi.models.fetch_user_privilege_on_entities_request_type import FetchUserPrivilegeOnEntitiesRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of FetchUserPrivilegeOnEntitiesRequestType from a JSON string
fetch_user_privilege_on_entities_request_type_instance = FetchUserPrivilegeOnEntitiesRequestType.from_json(json)
# print the JSON string representation of the object
print FetchUserPrivilegeOnEntitiesRequestType.to_json()

# convert the object into a dict
fetch_user_privilege_on_entities_request_type_dict = fetch_user_privilege_on_entities_request_type_instance.to_dict()
# create an instance of FetchUserPrivilegeOnEntitiesRequestType from a dict
fetch_user_privilege_on_entities_request_type_form_dict = fetch_user_privilege_on_entities_request_type.from_dict(fetch_user_privilege_on_entities_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


