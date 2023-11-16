# SetRegistryValueInGuestRequestType

The parameters of *GuestWindowsRegistryManager.SetRegistryValueInGuest*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vm** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | 
**auth** | [**GuestAuthentication**](GuestAuthentication.md) |  | 
**value** | [**GuestRegValueSpec**](GuestRegValueSpec.md) |  | 

## Example

```python
from vmware_vi.models.set_registry_value_in_guest_request_type import SetRegistryValueInGuestRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of SetRegistryValueInGuestRequestType from a JSON string
set_registry_value_in_guest_request_type_instance = SetRegistryValueInGuestRequestType.from_json(json)
# print the JSON string representation of the object
print SetRegistryValueInGuestRequestType.to_json()

# convert the object into a dict
set_registry_value_in_guest_request_type_dict = set_registry_value_in_guest_request_type_instance.to_dict()
# create an instance of SetRegistryValueInGuestRequestType from a dict
set_registry_value_in_guest_request_type_form_dict = set_registry_value_in_guest_request_type.from_dict(set_registry_value_in_guest_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


