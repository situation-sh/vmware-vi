# RemoveGuestAliasByCertRequestType

The parameters of *GuestAliasManager.RemoveGuestAliasByCert*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vm** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | 
**auth** | [**GuestAuthentication**](GuestAuthentication.md) |  | 
**username** | **str** | Username for the guest account on the virtual machine.  | 
**base64_cert** | **str** | The X.509 certificate to be removed, in base64 encoded DER format.  | 

## Example

```python
from vmware_vi.models.remove_guest_alias_by_cert_request_type import RemoveGuestAliasByCertRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of RemoveGuestAliasByCertRequestType from a JSON string
remove_guest_alias_by_cert_request_type_instance = RemoveGuestAliasByCertRequestType.from_json(json)
# print the JSON string representation of the object
print RemoveGuestAliasByCertRequestType.to_json()

# convert the object into a dict
remove_guest_alias_by_cert_request_type_dict = remove_guest_alias_by_cert_request_type_instance.to_dict()
# create an instance of RemoveGuestAliasByCertRequestType from a dict
remove_guest_alias_by_cert_request_type_form_dict = remove_guest_alias_by_cert_request_type.from_dict(remove_guest_alias_by_cert_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


