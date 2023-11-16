# UpdateSystemUsersRequestType

The parameters of *HostAccessManager.UpdateSystemUsers*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**users** | **List[str]** | the new list of local system users.  | [optional] 

## Example

```python
from vmware_vi.models.update_system_users_request_type import UpdateSystemUsersRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateSystemUsersRequestType from a JSON string
update_system_users_request_type_instance = UpdateSystemUsersRequestType.from_json(json)
# print the JSON string representation of the object
print UpdateSystemUsersRequestType.to_json()

# convert the object into a dict
update_system_users_request_type_dict = update_system_users_request_type_instance.to_dict()
# create an instance of UpdateSystemUsersRequestType from a dict
update_system_users_request_type_form_dict = update_system_users_request_type.from_dict(update_system_users_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


