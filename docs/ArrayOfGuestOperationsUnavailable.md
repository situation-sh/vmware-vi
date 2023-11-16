# ArrayOfGuestOperationsUnavailable

A boxed array of *GuestOperationsUnavailable*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[GuestOperationsUnavailable]**](GuestOperationsUnavailable.md) |  | 

## Example

```python
from vmware_vi.models.array_of_guest_operations_unavailable import ArrayOfGuestOperationsUnavailable

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfGuestOperationsUnavailable from a JSON string
array_of_guest_operations_unavailable_instance = ArrayOfGuestOperationsUnavailable.from_json(json)
# print the JSON string representation of the object
print ArrayOfGuestOperationsUnavailable.to_json()

# convert the object into a dict
array_of_guest_operations_unavailable_dict = array_of_guest_operations_unavailable_instance.to_dict()
# create an instance of ArrayOfGuestOperationsUnavailable from a dict
array_of_guest_operations_unavailable_form_dict = array_of_guest_operations_unavailable.from_dict(array_of_guest_operations_unavailable_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


