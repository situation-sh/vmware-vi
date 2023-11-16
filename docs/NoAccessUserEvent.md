# NoAccessUserEvent

This event records a failed user logon due to insufficient access permission. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ip_address** | **str** | The IP address of the peer that initiated the connection.  This may be the client that originated the session, or it may be an intervening proxy if the binding uses a protocol that supports proxies, such as HTTP.  | 

## Example

```python
from vmware_vi.models.no_access_user_event import NoAccessUserEvent

# TODO update the JSON string below
json = "{}"
# create an instance of NoAccessUserEvent from a JSON string
no_access_user_event_instance = NoAccessUserEvent.from_json(json)
# print the JSON string representation of the object
print NoAccessUserEvent.to_json()

# convert the object into a dict
no_access_user_event_dict = no_access_user_event_instance.to_dict()
# create an instance of NoAccessUserEvent from a dict
no_access_user_event_form_dict = no_access_user_event.from_dict(no_access_user_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


