# ValidateCredentialsInGuestRequestType

The parameters of *GuestAuthManager.ValidateCredentialsInGuest*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vm** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | 
**auth** | [**GuestAuthentication**](GuestAuthentication.md) |  | 

## Example

```python
from vmware_vi.models.validate_credentials_in_guest_request_type import ValidateCredentialsInGuestRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of ValidateCredentialsInGuestRequestType from a JSON string
validate_credentials_in_guest_request_type_instance = ValidateCredentialsInGuestRequestType.from_json(json)
# print the JSON string representation of the object
print ValidateCredentialsInGuestRequestType.to_json()

# convert the object into a dict
validate_credentials_in_guest_request_type_dict = validate_credentials_in_guest_request_type_instance.to_dict()
# create an instance of ValidateCredentialsInGuestRequestType from a dict
validate_credentials_in_guest_request_type_form_dict = validate_credentials_in_guest_request_type.from_dict(validate_credentials_in_guest_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


