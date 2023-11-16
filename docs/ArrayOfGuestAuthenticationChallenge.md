# ArrayOfGuestAuthenticationChallenge

A boxed array of *GuestAuthenticationChallenge*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[GuestAuthenticationChallenge]**](GuestAuthenticationChallenge.md) |  | 

## Example

```python
from vmware_vi.models.array_of_guest_authentication_challenge import ArrayOfGuestAuthenticationChallenge

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfGuestAuthenticationChallenge from a JSON string
array_of_guest_authentication_challenge_instance = ArrayOfGuestAuthenticationChallenge.from_json(json)
# print the JSON string representation of the object
print ArrayOfGuestAuthenticationChallenge.to_json()

# convert the object into a dict
array_of_guest_authentication_challenge_dict = array_of_guest_authentication_challenge_instance.to_dict()
# create an instance of ArrayOfGuestAuthenticationChallenge from a dict
array_of_guest_authentication_challenge_form_dict = array_of_guest_authentication_challenge.from_dict(array_of_guest_authentication_challenge_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


