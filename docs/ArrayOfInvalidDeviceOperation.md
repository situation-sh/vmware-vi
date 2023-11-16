# ArrayOfInvalidDeviceOperation

A boxed array of *InvalidDeviceOperation*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[InvalidDeviceOperation]**](InvalidDeviceOperation.md) |  | 

## Example

```python
from vmware_vi.models.array_of_invalid_device_operation import ArrayOfInvalidDeviceOperation

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfInvalidDeviceOperation from a JSON string
array_of_invalid_device_operation_instance = ArrayOfInvalidDeviceOperation.from_json(json)
# print the JSON string representation of the object
print ArrayOfInvalidDeviceOperation.to_json()

# convert the object into a dict
array_of_invalid_device_operation_dict = array_of_invalid_device_operation_instance.to_dict()
# create an instance of ArrayOfInvalidDeviceOperation from a dict
array_of_invalid_device_operation_form_dict = array_of_invalid_device_operation.from_dict(array_of_invalid_device_operation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


