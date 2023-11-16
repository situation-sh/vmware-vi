# TicketedSessionAuthentication

TicketedSessionAuthentication contains the information necessary to use previously obtained credentials in the guest.  The ticketed session is not stateless and stores state inside of the guest.  A TicketedSessionAuthentication object will be returned as the result of a successful call to *GuestAuthManager.AcquireCredentialsInGuest*. You can use this object in any guest operations function call.  When you no longer need the TicketedSessionAuthentication object, you should call *GuestAuthManager.ReleaseCredentialsInGuest* to free associated resources and session data.  ***Since:*** vSphere API 5.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ticket** | **str** | This contains a base64 encoded Ticket.  ***Since:*** vSphere API 5.0  | 

## Example

```python
from vmware_vi.models.ticketed_session_authentication import TicketedSessionAuthentication

# TODO update the JSON string below
json = "{}"
# create an instance of TicketedSessionAuthentication from a JSON string
ticketed_session_authentication_instance = TicketedSessionAuthentication.from_json(json)
# print the JSON string representation of the object
print TicketedSessionAuthentication.to_json()

# convert the object into a dict
ticketed_session_authentication_dict = ticketed_session_authentication_instance.to_dict()
# create an instance of TicketedSessionAuthentication from a dict
ticketed_session_authentication_form_dict = ticketed_session_authentication.from_dict(ticketed_session_authentication_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


