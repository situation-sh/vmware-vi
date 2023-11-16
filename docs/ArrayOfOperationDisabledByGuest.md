# ArrayOfOperationDisabledByGuest

A boxed array of *OperationDisabledByGuest*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[OperationDisabledByGuest]**](OperationDisabledByGuest.md) |  | 

## Example

```python
from vmware_vi.models.array_of_operation_disabled_by_guest import ArrayOfOperationDisabledByGuest

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfOperationDisabledByGuest from a JSON string
array_of_operation_disabled_by_guest_instance = ArrayOfOperationDisabledByGuest.from_json(json)
# print the JSON string representation of the object
print ArrayOfOperationDisabledByGuest.to_json()

# convert the object into a dict
array_of_operation_disabled_by_guest_dict = array_of_operation_disabled_by_guest_instance.to_dict()
# create an instance of ArrayOfOperationDisabledByGuest from a dict
array_of_operation_disabled_by_guest_form_dict = array_of_operation_disabled_by_guest.from_dict(array_of_operation_disabled_by_guest_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


