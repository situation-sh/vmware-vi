# AcquireCredentialsInGuestRequestType

The parameters of *GuestAuthManager.AcquireCredentialsInGuest*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vm** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | 
**requested_auth** | [**GuestAuthentication**](GuestAuthentication.md) |  | 
**session_id** | **int** | The sessionID number should be provided only when responding to a server challenge. The sessionID number to be used with the challenge is found in the *GuestAuthenticationChallenge* object.  | [optional] 

## Example

```python
from vmware_vi.models.acquire_credentials_in_guest_request_type import AcquireCredentialsInGuestRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of AcquireCredentialsInGuestRequestType from a JSON string
acquire_credentials_in_guest_request_type_instance = AcquireCredentialsInGuestRequestType.from_json(json)
# print the JSON string representation of the object
print AcquireCredentialsInGuestRequestType.to_json()

# convert the object into a dict
acquire_credentials_in_guest_request_type_dict = acquire_credentials_in_guest_request_type_instance.to_dict()
# create an instance of AcquireCredentialsInGuestRequestType from a dict
acquire_credentials_in_guest_request_type_form_dict = acquire_credentials_in_guest_request_type.from_dict(acquire_credentials_in_guest_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


