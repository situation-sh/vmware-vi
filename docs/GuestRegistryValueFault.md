# GuestRegistryValueFault

A GuestRegistryValueFault exception is thrown when an operation fails because of some errors in accessing/modifying a guest registry value.  ***Since:*** vSphere API 6.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key_name** | **str** | The full path to the windows registry key containing the value.  ***Since:*** vSphere API 6.0  | 
**value_name** | **str** | The name of the value.  ***Since:*** vSphere API 6.0  | 

## Example

```python
from vmware_vi.models.guest_registry_value_fault import GuestRegistryValueFault

# TODO update the JSON string below
json = "{}"
# create an instance of GuestRegistryValueFault from a JSON string
guest_registry_value_fault_instance = GuestRegistryValueFault.from_json(json)
# print the JSON string representation of the object
print GuestRegistryValueFault.to_json()

# convert the object into a dict
guest_registry_value_fault_dict = guest_registry_value_fault_instance.to_dict()
# create an instance of GuestRegistryValueFault from a dict
guest_registry_value_fault_form_dict = guest_registry_value_fault.from_dict(guest_registry_value_fault_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


