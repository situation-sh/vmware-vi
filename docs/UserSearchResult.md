# UserSearchResult

When searching for users, the search results in some additional information.  This object describes the additional information. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**principal** | **str** | Login name of a user or the name of a group.  This key is the user within the searched domain.  | 
**full_name** | **str** | Full name of the user found by the search, or the description of a group, if available.  | [optional] 
**group** | **bool** | If this is true, then the result is a group.  If this is false, then the result is a user.  | 

## Example

```python
from vmware_vi.models.user_search_result import UserSearchResult

# TODO update the JSON string below
json = "{}"
# create an instance of UserSearchResult from a JSON string
user_search_result_instance = UserSearchResult.from_json(json)
# print the JSON string representation of the object
print UserSearchResult.to_json()

# convert the object into a dict
user_search_result_dict = user_search_result_instance.to_dict()
# create an instance of UserSearchResult from a dict
user_search_result_form_dict = user_search_result.from_dict(user_search_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


