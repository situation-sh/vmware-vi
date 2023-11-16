# UserSession

Information about a current user session. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | A unique identifier for this session, also known as the session ID.  | 
**user_name** | **str** | The user name represented by this session.  | 
**full_name** | **str** | The full name of the user, if available.  | 
**login_time** | **datetime** | Timestamp when the user last logged on to the server.  | 
**last_active_time** | **datetime** | Timestamp when the user last executed a command.  | 
**locale** | **str** | The locale for the session used for data formatting and preferred for messages.  | 
**message_locale** | **str** | The locale used for messages for the session.  If there are no localized messages for the user-specified locale, then the server determines this locale.  | 
**extension_session** | **bool** | Whether or not this session belongs to a VC Extension.  ***Since:*** vSphere API 5.0  | 
**ip_address** | **str** | The client identity.  It could be IP address, or pipe name depended on client binding  ***Since:*** vSphere API 5.1  | 
**user_agent** | **str** | The name of user agent or application  ***Since:*** vSphere API 5.1  | 
**call_count** | **int** | Number of API invocations since the session started  ***Since:*** vSphere API 5.1  | 

## Example

```python
from vmware_vi.models.user_session import UserSession

# TODO update the JSON string below
json = "{}"
# create an instance of UserSession from a JSON string
user_session_instance = UserSession.from_json(json)
# print the JSON string representation of the object
print UserSession.to_json()

# convert the object into a dict
user_session_dict = user_session_instance.to_dict()
# create an instance of UserSession from a dict
user_session_form_dict = user_session.from_dict(user_session_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


