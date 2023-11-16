# GuestRegistryFault

A GuestRegistryFault exception is thrown when an operation fails because of some errors in accessing/modifying the guest registry.  ***Since:*** vSphere API 6.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**windows_system_error_code** | **int** | The windows system error number from GetLastError().  ***Since:*** vSphere API 6.0  | 

## Example

```python
from vmware_vi.models.guest_registry_fault import GuestRegistryFault

# TODO update the JSON string below
json = "{}"
# create an instance of GuestRegistryFault from a JSON string
guest_registry_fault_instance = GuestRegistryFault.from_json(json)
# print the JSON string representation of the object
print GuestRegistryFault.to_json()

# convert the object into a dict
guest_registry_fault_dict = guest_registry_fault_instance.to_dict()
# create an instance of GuestRegistryFault from a dict
guest_registry_fault_form_dict = guest_registry_fault.from_dict(guest_registry_fault_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


