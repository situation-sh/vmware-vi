# GuestAuthenticationChallenge

Fault is thrown when a call to *GuestAuthManager.AcquireCredentialsInGuest* requires a challenge response in order to authenticate in the guest.  The authToken string in serverChallenge contains a base64 encoded challenge token.  ***Since:*** vSphere API 5.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**server_challenge** | [**GuestAuthentication**](GuestAuthentication.md) |  | 
**session_id** | **int** | Contains a session ID number that associates the server response with the initial request.  ***Since:*** vSphere API 5.0  | 

## Example

```python
from vmware_vi.models.guest_authentication_challenge import GuestAuthenticationChallenge

# TODO update the JSON string below
json = "{}"
# create an instance of GuestAuthenticationChallenge from a JSON string
guest_authentication_challenge_instance = GuestAuthenticationChallenge.from_json(json)
# print the JSON string representation of the object
print GuestAuthenticationChallenge.to_json()

# convert the object into a dict
guest_authentication_challenge_dict = guest_authentication_challenge_instance.to_dict()
# create an instance of GuestAuthenticationChallenge from a dict
guest_authentication_challenge_form_dict = guest_authentication_challenge.from_dict(guest_authentication_challenge_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


