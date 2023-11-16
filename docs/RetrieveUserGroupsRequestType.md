# RetrieveUserGroupsRequestType

The parameters of *UserDirectory.RetrieveUserGroups*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domain** | **str** | Domain to be searched. If not set, then the method searches the local machine.  | [optional] 
**search_str** | **str** | Case insensitive substring used to filter results; the search string is compared to the login and full name for users, and the name and description for groups. Leave this blank to match all users.  | 
**belongs_to_group** | **str** | If present, the returned list contains only users or groups that directly belong to the specified group. Users or groups that have indirect membership will not be included in the list.  | [optional] 
**belongs_to_user** | **str** | If present, the returned list contains only groups that directly contain the specified user. Groups that indirectly contain the user will not be included in the list.  | [optional] 
**exact_match** | **bool** | Indicates the searchStr passed should match a user or group name exactly.  | 
**find_users** | **bool** | True, if users should be included in the result.  | 
**find_groups** | **bool** | True, if groups should be included in the result.  | 

## Example

```python
from vmware_vi.models.retrieve_user_groups_request_type import RetrieveUserGroupsRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of RetrieveUserGroupsRequestType from a JSON string
retrieve_user_groups_request_type_instance = RetrieveUserGroupsRequestType.from_json(json)
# print the JSON string representation of the object
print RetrieveUserGroupsRequestType.to_json()

# convert the object into a dict
retrieve_user_groups_request_type_dict = retrieve_user_groups_request_type_instance.to_dict()
# create an instance of RetrieveUserGroupsRequestType from a dict
retrieve_user_groups_request_type_form_dict = retrieve_user_groups_request_type.from_dict(retrieve_user_groups_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


