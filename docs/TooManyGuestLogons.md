# TooManyGuestLogons

A TooManyGuestLogons exception is thrown when there are too many concurrent login sessions active in the guest.  *GuestAuthManager.ReleaseCredentialsInGuest* can be called on ticketed sessions that are no longer needed. This will decrease the number of concurrent sessions active in the guest.  ***Since:*** vSphere API 5.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.too_many_guest_logons import TooManyGuestLogons

# TODO update the JSON string below
json = "{}"
# create an instance of TooManyGuestLogons from a JSON string
too_many_guest_logons_instance = TooManyGuestLogons.from_json(json)
# print the JSON string representation of the object
print TooManyGuestLogons.to_json()

# convert the object into a dict
too_many_guest_logons_dict = too_many_guest_logons_instance.to_dict()
# create an instance of TooManyGuestLogons from a dict
too_many_guest_logons_form_dict = too_many_guest_logons.from_dict(too_many_guest_logons_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


