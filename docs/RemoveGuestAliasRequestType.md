# RemoveGuestAliasRequestType

The parameters of *GuestAliasManager.RemoveGuestAlias*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vm** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | 
**auth** | [**GuestAuthentication**](GuestAuthentication.md) |  | 
**username** | **str** | Username for the guest account on the virtual machine.  | 
**base64_cert** | **str** | The X.509 certificate associated with the alias to be removed, in base64 encoded DER format.  | 
**subject** | [**GuestAuthSubject**](GuestAuthSubject.md) |  | 

## Example

```python
from vmware_vi.models.remove_guest_alias_request_type import RemoveGuestAliasRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of RemoveGuestAliasRequestType from a JSON string
remove_guest_alias_request_type_instance = RemoveGuestAliasRequestType.from_json(json)
# print the JSON string representation of the object
print RemoveGuestAliasRequestType.to_json()

# convert the object into a dict
remove_guest_alias_request_type_dict = remove_guest_alias_request_type_instance.to_dict()
# create an instance of RemoveGuestAliasRequestType from a dict
remove_guest_alias_request_type_form_dict = remove_guest_alias_request_type.from_dict(remove_guest_alias_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


