# GuestRegistryKeyAlreadyExists

A GuestRegistryKeyAlreadyExists exception is thrown when an operation fails because the guest registry key specified already exists.  ***Since:*** vSphere API 6.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.guest_registry_key_already_exists import GuestRegistryKeyAlreadyExists

# TODO update the JSON string below
json = "{}"
# create an instance of GuestRegistryKeyAlreadyExists from a JSON string
guest_registry_key_already_exists_instance = GuestRegistryKeyAlreadyExists.from_json(json)
# print the JSON string representation of the object
print GuestRegistryKeyAlreadyExists.to_json()

# convert the object into a dict
guest_registry_key_already_exists_dict = guest_registry_key_already_exists_instance.to_dict()
# create an instance of GuestRegistryKeyAlreadyExists from a dict
guest_registry_key_already_exists_form_dict = guest_registry_key_already_exists.from_dict(guest_registry_key_already_exists_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


