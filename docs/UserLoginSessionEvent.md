# UserLoginSessionEvent

This event records a user logon. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ip_address** | **str** | The IP address of the peer that initiated the connection.  This may be the client that originated the session, or it may be an intervening proxy if the binding uses a protocol that supports proxies, such as HTTP.  | 
**user_agent** | **str** | The user agent or application  ***Since:*** vSphere API 5.1  | [optional] 
**locale** | **str** | The locale of the session.  | 
**session_id** | **str** | The unique identifier for the session.  | 

## Example

```python
from vmware_vi.models.user_login_session_event import UserLoginSessionEvent

# TODO update the JSON string below
json = "{}"
# create an instance of UserLoginSessionEvent from a JSON string
user_login_session_event_instance = UserLoginSessionEvent.from_json(json)
# print the JSON string representation of the object
print UserLoginSessionEvent.to_json()

# convert the object into a dict
user_login_session_event_dict = user_login_session_event_instance.to_dict()
# create an instance of UserLoginSessionEvent from a dict
user_login_session_event_form_dict = user_login_session_event.from_dict(user_login_session_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


