# GuestAuthentication

GuestAuthentication is an abstract base class for authentication in the guest.  ***Since:*** vSphere API 5.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**interactive_session** | **bool** | This is set to true if the client wants an interactive session in the guest.  Setting this is supported only for *NamePasswordAuthentication*.  ***Since:*** vSphere API 5.0  | 

## Example

```python
from vmware_vi.models.guest_authentication import GuestAuthentication

# TODO update the JSON string below
json = "{}"
# create an instance of GuestAuthentication from a JSON string
guest_authentication_instance = GuestAuthentication.from_json(json)
# print the JSON string representation of the object
print GuestAuthentication.to_json()

# convert the object into a dict
guest_authentication_dict = guest_authentication_instance.to_dict()
# create an instance of GuestAuthentication from a dict
guest_authentication_form_dict = guest_authentication.from_dict(guest_authentication_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


