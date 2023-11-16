# InvalidDeviceOperation

An InvalidDeviceOperation exception is thrown if virtual machine creation or configuration fails because an invalid operation is attempted on the given device. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bad_op** | [**VirtualDeviceConfigSpecOperationEnum**](VirtualDeviceConfigSpecOperationEnum.md) |  | [optional] 
**bad_file_op** | [**VirtualDeviceConfigSpecFileOperationEnum**](VirtualDeviceConfigSpecFileOperationEnum.md) |  | [optional] 

## Example

```python
from vmware_vi.models.invalid_device_operation import InvalidDeviceOperation

# TODO update the JSON string below
json = "{}"
# create an instance of InvalidDeviceOperation from a JSON string
invalid_device_operation_instance = InvalidDeviceOperation.from_json(json)
# print the JSON string representation of the object
print InvalidDeviceOperation.to_json()

# convert the object into a dict
invalid_device_operation_dict = invalid_device_operation_instance.to_dict()
# create an instance of InvalidDeviceOperation from a dict
invalid_device_operation_form_dict = invalid_device_operation.from_dict(invalid_device_operation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


