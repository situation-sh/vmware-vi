# ArrayOfInvalidGuestLogin

A boxed array of *InvalidGuestLogin*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[InvalidGuestLogin]**](InvalidGuestLogin.md) |  | 

## Example

```python
from vmware_vi.models.array_of_invalid_guest_login import ArrayOfInvalidGuestLogin

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfInvalidGuestLogin from a JSON string
array_of_invalid_guest_login_instance = ArrayOfInvalidGuestLogin.from_json(json)
# print the JSON string representation of the object
print ArrayOfInvalidGuestLogin.to_json()

# convert the object into a dict
array_of_invalid_guest_login_dict = array_of_invalid_guest_login_instance.to_dict()
# create an instance of ArrayOfInvalidGuestLogin from a dict
array_of_invalid_guest_login_form_dict = array_of_invalid_guest_login.from_dict(array_of_invalid_guest_login_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


