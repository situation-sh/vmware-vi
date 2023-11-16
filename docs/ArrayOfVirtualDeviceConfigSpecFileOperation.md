# ArrayOfVirtualDeviceConfigSpecFileOperation

A boxed array of *VirtualDeviceConfigSpecFileOperation_enum*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[VirtualDeviceConfigSpecFileOperationEnum]**](VirtualDeviceConfigSpecFileOperationEnum.md) |  | 

## Example

```python
from vmware_vi.models.array_of_virtual_device_config_spec_file_operation import ArrayOfVirtualDeviceConfigSpecFileOperation

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfVirtualDeviceConfigSpecFileOperation from a JSON string
array_of_virtual_device_config_spec_file_operation_instance = ArrayOfVirtualDeviceConfigSpecFileOperation.from_json(json)
# print the JSON string representation of the object
print ArrayOfVirtualDeviceConfigSpecFileOperation.to_json()

# convert the object into a dict
array_of_virtual_device_config_spec_file_operation_dict = array_of_virtual_device_config_spec_file_operation_instance.to_dict()
# create an instance of ArrayOfVirtualDeviceConfigSpecFileOperation from a dict
array_of_virtual_device_config_spec_file_operation_form_dict = array_of_virtual_device_config_spec_file_operation.from_dict(array_of_virtual_device_config_spec_file_operation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


