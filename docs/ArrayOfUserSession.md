# ArrayOfUserSession

A boxed array of *UserSession*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[UserSession]**](UserSession.md) |  | 

## Example

```python
from vmware_vi.models.array_of_user_session import ArrayOfUserSession

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfUserSession from a JSON string
array_of_user_session_instance = ArrayOfUserSession.from_json(json)
# print the JSON string representation of the object
print ArrayOfUserSession.to_json()

# convert the object into a dict
array_of_user_session_dict = array_of_user_session_instance.to_dict()
# create an instance of ArrayOfUserSession from a dict
array_of_user_session_form_dict = array_of_user_session.from_dict(array_of_user_session_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


