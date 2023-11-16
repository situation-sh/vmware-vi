# DeleteRegistryKeyInGuestRequestType

The parameters of *GuestWindowsRegistryManager.DeleteRegistryKeyInGuest*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vm** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | 
**auth** | [**GuestAuthentication**](GuestAuthentication.md) |  | 
**key_name** | [**GuestRegKeyNameSpec**](GuestRegKeyNameSpec.md) |  | 
**recursive** | **bool** | If true, the key is deleted along with any subkeys (if present). Otherwise, it shall only delete the key if it has no subkeys.  | 

## Example

```python
from vmware_vi.models.delete_registry_key_in_guest_request_type import DeleteRegistryKeyInGuestRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteRegistryKeyInGuestRequestType from a JSON string
delete_registry_key_in_guest_request_type_instance = DeleteRegistryKeyInGuestRequestType.from_json(json)
# print the JSON string representation of the object
print DeleteRegistryKeyInGuestRequestType.to_json()

# convert the object into a dict
delete_registry_key_in_guest_request_type_dict = delete_registry_key_in_guest_request_type_instance.to_dict()
# create an instance of DeleteRegistryKeyInGuestRequestType from a dict
delete_registry_key_in_guest_request_type_form_dict = delete_registry_key_in_guest_request_type.from_dict(delete_registry_key_in_guest_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


