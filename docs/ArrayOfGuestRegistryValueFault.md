# ArrayOfGuestRegistryValueFault

A boxed array of *GuestRegistryValueFault*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[GuestRegistryValueFault]**](GuestRegistryValueFault.md) |  | 

## Example

```python
from vmware_vi.models.array_of_guest_registry_value_fault import ArrayOfGuestRegistryValueFault

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfGuestRegistryValueFault from a JSON string
array_of_guest_registry_value_fault_instance = ArrayOfGuestRegistryValueFault.from_json(json)
# print the JSON string representation of the object
print ArrayOfGuestRegistryValueFault.to_json()

# convert the object into a dict
array_of_guest_registry_value_fault_dict = array_of_guest_registry_value_fault_instance.to_dict()
# create an instance of ArrayOfGuestRegistryValueFault from a dict
array_of_guest_registry_value_fault_form_dict = array_of_guest_registry_value_fault.from_dict(array_of_guest_registry_value_fault_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


