# AddGuestAliasRequestType

The parameters of *GuestAliasManager.AddGuestAlias*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vm** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | 
**auth** | [**GuestAuthentication**](GuestAuthentication.md) |  | 
**username** | **str** | Username for the guest account on the virtual machine.  | 
**map_cert** | **bool** | Indicates whether the certificate associated with the alias should be mapped. If an alias certificate is mapped, guest operation requests that use that alias do not have to specify the guest account username in the *SAMLTokenAuthentication* object. If mapCert is false, the request must specify the username.  | 
**base64_cert** | **str** | X.509 certificate from the VMware SSO Server, in base64 encoded DER format. The ESXi Server uses this certificate to authenticate guest operation requests.  | 
**alias_info** | [**GuestAuthAliasInfo**](GuestAuthAliasInfo.md) |  | 

## Example

```python
from vmware_vi.models.add_guest_alias_request_type import AddGuestAliasRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of AddGuestAliasRequestType from a JSON string
add_guest_alias_request_type_instance = AddGuestAliasRequestType.from_json(json)
# print the JSON string representation of the object
print AddGuestAliasRequestType.to_json()

# convert the object into a dict
add_guest_alias_request_type_dict = add_guest_alias_request_type_instance.to_dict()
# create an instance of AddGuestAliasRequestType from a dict
add_guest_alias_request_type_form_dict = add_guest_alias_request_type.from_dict(add_guest_alias_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


