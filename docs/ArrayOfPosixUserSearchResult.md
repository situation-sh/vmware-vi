# ArrayOfPosixUserSearchResult

A boxed array of *PosixUserSearchResult*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[PosixUserSearchResult]**](PosixUserSearchResult.md) |  | 

## Example

```python
from vmware_vi.models.array_of_posix_user_search_result import ArrayOfPosixUserSearchResult

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfPosixUserSearchResult from a JSON string
array_of_posix_user_search_result_instance = ArrayOfPosixUserSearchResult.from_json(json)
# print the JSON string representation of the object
print ArrayOfPosixUserSearchResult.to_json()

# convert the object into a dict
array_of_posix_user_search_result_dict = array_of_posix_user_search_result_instance.to_dict()
# create an instance of ArrayOfPosixUserSearchResult from a dict
array_of_posix_user_search_result_form_dict = array_of_posix_user_search_result.from_dict(array_of_posix_user_search_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


