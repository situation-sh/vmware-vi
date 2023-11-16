# InvalidGuestLogin

An InvalidGuestLogin exception is thrown when an operation fails because authentication information used to authenticate with the guest was not accepted.  ***Since:*** vSphere API 5.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.invalid_guest_login import InvalidGuestLogin

# TODO update the JSON string below
json = "{}"
# create an instance of InvalidGuestLogin from a JSON string
invalid_guest_login_instance = InvalidGuestLogin.from_json(json)
# print the JSON string representation of the object
print InvalidGuestLogin.to_json()

# convert the object into a dict
invalid_guest_login_dict = invalid_guest_login_instance.to_dict()
# create an instance of InvalidGuestLogin from a dict
invalid_guest_login_form_dict = invalid_guest_login.from_dict(invalid_guest_login_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


