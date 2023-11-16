# ArrayOfGuestOperationsFault

A boxed array of *GuestOperationsFault*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[GuestOperationsFault]**](GuestOperationsFault.md) |  | 

## Example

```python
from vmware_vi.models.array_of_guest_operations_fault import ArrayOfGuestOperationsFault

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfGuestOperationsFault from a JSON string
array_of_guest_operations_fault_instance = ArrayOfGuestOperationsFault.from_json(json)
# print the JSON string representation of the object
print ArrayOfGuestOperationsFault.to_json()

# convert the object into a dict
array_of_guest_operations_fault_dict = array_of_guest_operations_fault_instance.to_dict()
# create an instance of ArrayOfGuestOperationsFault from a dict
array_of_guest_operations_fault_form_dict = array_of_guest_operations_fault.from_dict(array_of_guest_operations_fault_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


