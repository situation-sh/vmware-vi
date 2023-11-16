# DeleteRegistryValueInGuestRequestType

The parameters of *GuestWindowsRegistryManager.DeleteRegistryValueInGuest*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vm** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | 
**auth** | [**GuestAuthentication**](GuestAuthentication.md) |  | 
**value_name** | [**GuestRegValueNameSpec**](GuestRegValueNameSpec.md) |  | 

## Example

```python
from vmware_vi.models.delete_registry_value_in_guest_request_type import DeleteRegistryValueInGuestRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteRegistryValueInGuestRequestType from a JSON string
delete_registry_value_in_guest_request_type_instance = DeleteRegistryValueInGuestRequestType.from_json(json)
# print the JSON string representation of the object
print DeleteRegistryValueInGuestRequestType.to_json()

# convert the object into a dict
delete_registry_value_in_guest_request_type_dict = delete_registry_value_in_guest_request_type_instance.to_dict()
# create an instance of DeleteRegistryValueInGuestRequestType from a dict
delete_registry_value_in_guest_request_type_form_dict = delete_registry_value_in_guest_request_type.from_dict(delete_registry_value_in_guest_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


