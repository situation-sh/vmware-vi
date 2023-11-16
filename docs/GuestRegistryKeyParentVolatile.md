# GuestRegistryKeyParentVolatile

A GuestRegistryKeyParentVolatile exception is thrown when trying to create a non-volatile registry subkey under a volatile registry parent key.  ***Since:*** vSphere API 6.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.guest_registry_key_parent_volatile import GuestRegistryKeyParentVolatile

# TODO update the JSON string below
json = "{}"
# create an instance of GuestRegistryKeyParentVolatile from a JSON string
guest_registry_key_parent_volatile_instance = GuestRegistryKeyParentVolatile.from_json(json)
# print the JSON string representation of the object
print GuestRegistryKeyParentVolatile.to_json()

# convert the object into a dict
guest_registry_key_parent_volatile_dict = guest_registry_key_parent_volatile_instance.to_dict()
# create an instance of GuestRegistryKeyParentVolatile from a dict
guest_registry_key_parent_volatile_form_dict = guest_registry_key_parent_volatile.from_dict(guest_registry_key_parent_volatile_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


