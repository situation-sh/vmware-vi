# UserPrivilegeResult

This class is used to provide the list of effective privileges set on a given managed entity for a user.  ***Since:*** vSphere API 6.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entity** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | 
**privileges** | **List[str]** | A list of privileges set on the entity.  ***Since:*** vSphere API 6.5  | [optional] 

## Example

```python
from vmware_vi.models.user_privilege_result import UserPrivilegeResult

# TODO update the JSON string below
json = "{}"
# create an instance of UserPrivilegeResult from a JSON string
user_privilege_result_instance = UserPrivilegeResult.from_json(json)
# print the JSON string representation of the object
print UserPrivilegeResult.to_json()

# convert the object into a dict
user_privilege_result_dict = user_privilege_result_instance.to_dict()
# create an instance of UserPrivilegeResult from a dict
user_privilege_result_form_dict = user_privilege_result.from_dict(user_privilege_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


