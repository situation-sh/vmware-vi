# ArrayOfUserLoginSessionEvent

A boxed array of *UserLoginSessionEvent*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[UserLoginSessionEvent]**](UserLoginSessionEvent.md) |  | 

## Example

```python
from vmware_vi.models.array_of_user_login_session_event import ArrayOfUserLoginSessionEvent

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfUserLoginSessionEvent from a JSON string
array_of_user_login_session_event_instance = ArrayOfUserLoginSessionEvent.from_json(json)
# print the JSON string representation of the object
print ArrayOfUserLoginSessionEvent.to_json()

# convert the object into a dict
array_of_user_login_session_event_dict = array_of_user_login_session_event_instance.to_dict()
# create an instance of ArrayOfUserLoginSessionEvent from a dict
array_of_user_login_session_event_form_dict = array_of_user_login_session_event.from_dict(array_of_user_login_session_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


