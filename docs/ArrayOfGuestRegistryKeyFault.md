# ArrayOfGuestRegistryKeyFault

A boxed array of *GuestRegistryKeyFault*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[GuestRegistryKeyFault]**](GuestRegistryKeyFault.md) |  | 

## Example

```python
from vmware_vi.models.array_of_guest_registry_key_fault import ArrayOfGuestRegistryKeyFault

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfGuestRegistryKeyFault from a JSON string
array_of_guest_registry_key_fault_instance = ArrayOfGuestRegistryKeyFault.from_json(json)
# print the JSON string representation of the object
print ArrayOfGuestRegistryKeyFault.to_json()

# convert the object into a dict
array_of_guest_registry_key_fault_dict = array_of_guest_registry_key_fault_instance.to_dict()
# create an instance of ArrayOfGuestRegistryKeyFault from a dict
array_of_guest_registry_key_fault_form_dict = array_of_guest_registry_key_fault.from_dict(array_of_guest_registry_key_fault_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


