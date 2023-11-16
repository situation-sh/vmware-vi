# GuestRegistryValueNotFound

A GuestRegistryValueNotFound exception is thrown when an operation fails because the guest registry Value specified was not found.  ***Since:*** vSphere API 6.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.guest_registry_value_not_found import GuestRegistryValueNotFound

# TODO update the JSON string below
json = "{}"
# create an instance of GuestRegistryValueNotFound from a JSON string
guest_registry_value_not_found_instance = GuestRegistryValueNotFound.from_json(json)
# print the JSON string representation of the object
print GuestRegistryValueNotFound.to_json()

# convert the object into a dict
guest_registry_value_not_found_dict = guest_registry_value_not_found_instance.to_dict()
# create an instance of GuestRegistryValueNotFound from a dict
guest_registry_value_not_found_form_dict = guest_registry_value_not_found.from_dict(guest_registry_value_not_found_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


