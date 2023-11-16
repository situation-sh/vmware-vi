# UserNotFound

Thrown when the request refers to a user or group name that could not be resolved. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**principal** | **str** | Principal value that failed lookup.  | 
**unresolved** | **bool** | Flag to indicate whether or not the lookup was unsuccessful.  A false value indicates that the user does not exist in the directory. A true value indicates that the directory could not be contacted, possibly due to a network error.  | 

## Example

```python
from vmware_vi.models.user_not_found import UserNotFound

# TODO update the JSON string below
json = "{}"
# create an instance of UserNotFound from a JSON string
user_not_found_instance = UserNotFound.from_json(json)
# print the JSON string representation of the object
print UserNotFound.to_json()

# convert the object into a dict
user_not_found_dict = user_not_found_instance.to_dict()
# create an instance of UserNotFound from a dict
user_not_found_form_dict = user_not_found.from_dict(user_not_found_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


