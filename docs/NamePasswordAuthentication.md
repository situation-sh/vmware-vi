# NamePasswordAuthentication

NamePasswordAuthentication contains the information necessary to authenticate within a guest using a name and password.  This is the typical method for authentication within a guest and the one currently used by VIX. This method of authentication is stateless.  To use NamePasswordAuthentication, populate username and password with the appropriate login information. You should not use *GuestAuthManager.AcquireCredentialsInGuest* or *GuestAuthManager.ReleaseCredentialsInGuest* for NamePasswordAuthentication.  Once populated, you can use NamePasswordAuthentication in any guest operations function call.  ***Since:*** vSphere API 5.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**username** | **str** | The user name for Name-Password authentication.  ***Since:*** vSphere API 5.0  | 
**password** | **str** | The password for Name-Password authentication.  ***Since:*** vSphere API 5.0  | 

## Example

```python
from vmware_vi.models.name_password_authentication import NamePasswordAuthentication

# TODO update the JSON string below
json = "{}"
# create an instance of NamePasswordAuthentication from a JSON string
name_password_authentication_instance = NamePasswordAuthentication.from_json(json)
# print the JSON string representation of the object
print NamePasswordAuthentication.to_json()

# convert the object into a dict
name_password_authentication_dict = name_password_authentication_instance.to_dict()
# create an instance of NamePasswordAuthentication from a dict
name_password_authentication_form_dict = name_password_authentication.from_dict(name_password_authentication_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


