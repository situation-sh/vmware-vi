# PasswordExpired

Thrown when a server login fails due to expired user password.  ***Since:*** vSphere API 6.7.2 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.password_expired import PasswordExpired

# TODO update the JSON string below
json = "{}"
# create an instance of PasswordExpired from a JSON string
password_expired_instance = PasswordExpired.from_json(json)
# print the JSON string representation of the object
print PasswordExpired.to_json()

# convert the object into a dict
password_expired_dict = password_expired_instance.to_dict()
# create an instance of PasswordExpired from a dict
password_expired_form_dict = password_expired.from_dict(password_expired_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


