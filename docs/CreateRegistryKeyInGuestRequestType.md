# CreateRegistryKeyInGuestRequestType

The parameters of *GuestWindowsRegistryManager.CreateRegistryKeyInGuest*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vm** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | 
**auth** | [**GuestAuthentication**](GuestAuthentication.md) |  | 
**key_name** | [**GuestRegKeyNameSpec**](GuestRegKeyNameSpec.md) |  | 
**is_volatile** | **bool** | If true, the key is created in memory and is not preserved across system reboot. Otherwise, it shall persist in the file system.  | 
**class_type** | **str** | User defined class type for this key. May be omitted.  | [optional] 

## Example

```python
from vmware_vi.models.create_registry_key_in_guest_request_type import CreateRegistryKeyInGuestRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of CreateRegistryKeyInGuestRequestType from a JSON string
create_registry_key_in_guest_request_type_instance = CreateRegistryKeyInGuestRequestType.from_json(json)
# print the JSON string representation of the object
print CreateRegistryKeyInGuestRequestType.to_json()

# convert the object into a dict
create_registry_key_in_guest_request_type_dict = create_registry_key_in_guest_request_type_instance.to_dict()
# create an instance of CreateRegistryKeyInGuestRequestType from a dict
create_registry_key_in_guest_request_type_form_dict = create_registry_key_in_guest_request_type.from_dict(create_registry_key_in_guest_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


