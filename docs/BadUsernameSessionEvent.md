# BadUsernameSessionEvent

This event records a failed user logon.  Failed logons are due to no match existing between the provided user name and password combination and the combinations stored for authentication. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ip_address** | **str** | The IP address of the peer that initiated the connection.  This may be the client that originated the session, or it may be an intervening proxy if the binding uses a protocol that supports proxies, such as HTTP.  | 

## Example

```python
from vmware_vi.models.bad_username_session_event import BadUsernameSessionEvent

# TODO update the JSON string below
json = "{}"
# create an instance of BadUsernameSessionEvent from a JSON string
bad_username_session_event_instance = BadUsernameSessionEvent.from_json(json)
# print the JSON string representation of the object
print BadUsernameSessionEvent.to_json()

# convert the object into a dict
bad_username_session_event_dict = bad_username_session_event_instance.to_dict()
# create an instance of BadUsernameSessionEvent from a dict
bad_username_session_event_form_dict = bad_username_session_event.from_dict(bad_username_session_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


