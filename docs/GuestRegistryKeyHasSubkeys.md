# GuestRegistryKeyHasSubkeys

A GuestRegistryKeyHasSubkeys exception is thrown when an operation fails because the guest registry key has subkeys.  If a delete on the key is desired, please use the recursive delete option.  ***Since:*** vSphere API 6.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.guest_registry_key_has_subkeys import GuestRegistryKeyHasSubkeys

# TODO update the JSON string below
json = "{}"
# create an instance of GuestRegistryKeyHasSubkeys from a JSON string
guest_registry_key_has_subkeys_instance = GuestRegistryKeyHasSubkeys.from_json(json)
# print the JSON string representation of the object
print GuestRegistryKeyHasSubkeys.to_json()

# convert the object into a dict
guest_registry_key_has_subkeys_dict = guest_registry_key_has_subkeys_instance.to_dict()
# create an instance of GuestRegistryKeyHasSubkeys from a dict
guest_registry_key_has_subkeys_form_dict = guest_registry_key_has_subkeys.from_dict(guest_registry_key_has_subkeys_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


