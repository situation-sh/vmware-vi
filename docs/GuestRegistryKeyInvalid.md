# GuestRegistryKeyInvalid

A GuestRegistryKeyInvalid exception is thrown when an operation fails because the guest registry key specified was not valid (most probably due to an invalid HKEY Root in the key path), or does not exist.  ***Since:*** vSphere API 6.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.guest_registry_key_invalid import GuestRegistryKeyInvalid

# TODO update the JSON string below
json = "{}"
# create an instance of GuestRegistryKeyInvalid from a JSON string
guest_registry_key_invalid_instance = GuestRegistryKeyInvalid.from_json(json)
# print the JSON string representation of the object
print GuestRegistryKeyInvalid.to_json()

# convert the object into a dict
guest_registry_key_invalid_dict = guest_registry_key_invalid_instance.to_dict()
# create an instance of GuestRegistryKeyInvalid from a dict
guest_registry_key_invalid_form_dict = guest_registry_key_invalid.from_dict(guest_registry_key_invalid_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


