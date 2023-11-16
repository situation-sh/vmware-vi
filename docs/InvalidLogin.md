# InvalidLogin

Thrown when a server logon fails due to a bad user name or password. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.invalid_login import InvalidLogin

# TODO update the JSON string below
json = "{}"
# create an instance of InvalidLogin from a JSON string
invalid_login_instance = InvalidLogin.from_json(json)
# print the JSON string representation of the object
print InvalidLogin.to_json()

# convert the object into a dict
invalid_login_dict = invalid_login_instance.to_dict()
# create an instance of InvalidLogin from a dict
invalid_login_form_dict = invalid_login.from_dict(invalid_login_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


