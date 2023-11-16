# ArrayOfUserLogoutSessionEvent

A boxed array of *UserLogoutSessionEvent*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[UserLogoutSessionEvent]**](UserLogoutSessionEvent.md) |  | 

## Example

```python
from vmware_vi.models.array_of_user_logout_session_event import ArrayOfUserLogoutSessionEvent

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfUserLogoutSessionEvent from a JSON string
array_of_user_logout_session_event_instance = ArrayOfUserLogoutSessionEvent.from_json(json)
# print the JSON string representation of the object
print ArrayOfUserLogoutSessionEvent.to_json()

# convert the object into a dict
array_of_user_logout_session_event_dict = array_of_user_logout_session_event_instance.to_dict()
# create an instance of ArrayOfUserLogoutSessionEvent from a dict
array_of_user_logout_session_event_form_dict = array_of_user_logout_session_event.from_dict(array_of_user_logout_session_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


