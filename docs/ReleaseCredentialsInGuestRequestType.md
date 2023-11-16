# ReleaseCredentialsInGuestRequestType

The parameters of *GuestAuthManager.ReleaseCredentialsInGuest*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vm** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | 
**auth** | [**GuestAuthentication**](GuestAuthentication.md) |  | 

## Example

```python
from vmware_vi.models.release_credentials_in_guest_request_type import ReleaseCredentialsInGuestRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of ReleaseCredentialsInGuestRequestType from a JSON string
release_credentials_in_guest_request_type_instance = ReleaseCredentialsInGuestRequestType.from_json(json)
# print the JSON string representation of the object
print ReleaseCredentialsInGuestRequestType.to_json()

# convert the object into a dict
release_credentials_in_guest_request_type_dict = release_credentials_in_guest_request_type_instance.to_dict()
# create an instance of ReleaseCredentialsInGuestRequestType from a dict
release_credentials_in_guest_request_type_form_dict = release_credentials_in_guest_request_type.from_dict(release_credentials_in_guest_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


