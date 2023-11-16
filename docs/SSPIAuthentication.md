# SSPIAuthentication

SSPIAuthentication contains the information necessary to initiate a ticketed authentication session in the guest using SSPI credentials.  The ticketed session is not stateless and stores state inside of the guest.  To use SSPIAuthentication, populate sspiToken with a base64 encoded SSPI token. Then call *GuestAuthManager.AcquireCredentialsInGuest* with the SSPIAuthentication object and no sessionID. After issuing the *GuestAuthManager.AcquireCredentialsInGuest* call, a *GuestAuthenticationChallenge* will be thrown. Use the serverChallenge sspiToken in *GuestAuthenticationChallenge* to generate the proper SSPI response token. Populate an SSPIAuthentication object with the base64 encoded SSPI response token, and call *GuestAuthManager.AcquireCredentialsInGuest* with the SSPIAuthentication object and the sessionID found in *GuestAuthenticationChallenge*.  Successful authentication will result in a *TicketedSessionAuthentication* object being returned. You can use the *TicketedSessionAuthentication* in any guest operations function call. You should NOT attempt to use SSPIAuthentication in any guest operations function call.  When you no longer need the *TicketedSessionAuthentication* object, you should call *GuestAuthManager.ReleaseCredentialsInGuest* to free associated resources and session data.  Usage notes: SSPI authentication has the same limitations as a duplicated primary token obtained from the Windows API function LogonUser with the LOGON32\\_LOGON\\_NETWORK logon type. This will affect programs started with *GuestProcessManager.StartProgramInGuest*. For example, launched programs will be unable to use WMI functions unless the \"Remote Enable\" privilege is enabled for the user. Similarly, access to network resources may fail due to the limitations of the token.  ***Since:*** vSphere API 5.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sspi_token** | **str** | This contains a base64 encoded SSPI Token.  ***Since:*** vSphere API 5.0  | 

## Example

```python
from vmware_vi.models.sspi_authentication import SSPIAuthentication

# TODO update the JSON string below
json = "{}"
# create an instance of SSPIAuthentication from a JSON string
sspi_authentication_instance = SSPIAuthentication.from_json(json)
# print the JSON string representation of the object
print SSPIAuthentication.to_json()

# convert the object into a dict
sspi_authentication_dict = sspi_authentication_instance.to_dict()
# create an instance of SSPIAuthentication from a dict
sspi_authentication_form_dict = sspi_authentication.from_dict(sspi_authentication_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


