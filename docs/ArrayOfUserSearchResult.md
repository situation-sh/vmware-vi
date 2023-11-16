# ArrayOfUserSearchResult

A boxed array of *UserSearchResult*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[UserSearchResult]**](UserSearchResult.md) |  | 

## Example

```python
from vmware_vi.models.array_of_user_search_result import ArrayOfUserSearchResult

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfUserSearchResult from a JSON string
array_of_user_search_result_instance = ArrayOfUserSearchResult.from_json(json)
# print the JSON string representation of the object
print ArrayOfUserSearchResult.to_json()

# convert the object into a dict
array_of_user_search_result_dict = array_of_user_search_result_instance.to_dict()
# create an instance of ArrayOfUserSearchResult from a dict
array_of_user_search_result_form_dict = array_of_user_search_result.from_dict(array_of_user_search_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


