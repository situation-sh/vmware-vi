# UserLogoutSessionEvent

This event records a user logoff, disconnection, or session timeout. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ip_address** | **str** | The IP address of client  ***Since:*** vSphere API 5.1  | [optional] 
**user_agent** | **str** | The user agent or application  ***Since:*** vSphere API 5.1  | [optional] 
**call_count** | **int** | Number of API invocations made by the session  ***Since:*** vSphere API 5.1  | [optional] 
**session_id** | **str** | The unique identifier for the session.  ***Since:*** vSphere API 5.1  | [optional] 
**login_time** | **datetime** | Timestamp when the user logged on for this session.  ***Since:*** vSphere API 5.1  | [optional] 

## Example

```python
from vmware_vi.models.user_logout_session_event import UserLogoutSessionEvent

# TODO update the JSON string below
json = "{}"
# create an instance of UserLogoutSessionEvent from a JSON string
user_logout_session_event_instance = UserLogoutSessionEvent.from_json(json)
# print the JSON string representation of the object
print UserLogoutSessionEvent.to_json()

# convert the object into a dict
user_logout_session_event_dict = user_logout_session_event_instance.to_dict()
# create an instance of UserLogoutSessionEvent from a dict
user_logout_session_event_form_dict = user_logout_session_event.from_dict(user_logout_session_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


