# PosixUserSearchResult

Searching for users and groups on POSIX systems provides User ID and Group ID information, in addition to that defined in UserSearchResult. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | If the search result is for a user, then id refers to User ID.  For a group, the value of Group ID is assigned to id.  | 
**shell_access** | **bool** | If the search result is for a user, shellAccess indicates whether shell access has been granted or not.  | [optional] 

## Example

```python
from vmware_vi.models.posix_user_search_result import PosixUserSearchResult

# TODO update the JSON string below
json = "{}"
# create an instance of PosixUserSearchResult from a JSON string
posix_user_search_result_instance = PosixUserSearchResult.from_json(json)
# print the JSON string representation of the object
print PosixUserSearchResult.to_json()

# convert the object into a dict
posix_user_search_result_dict = posix_user_search_result_instance.to_dict()
# create an instance of PosixUserSearchResult from a dict
posix_user_search_result_form_dict = posix_user_search_result.from_dict(posix_user_search_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


