# VirtualDeviceConfigSpecFileOperation

A boxed *VirtualDeviceConfigSpecFileOperation_enum*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**VirtualDeviceConfigSpecFileOperationEnum**](VirtualDeviceConfigSpecFileOperationEnum.md) |  | 

## Example

```python
from vmware_vi.models.virtual_device_config_spec_file_operation import VirtualDeviceConfigSpecFileOperation

# TODO update the JSON string below
json = "{}"
# create an instance of VirtualDeviceConfigSpecFileOperation from a JSON string
virtual_device_config_spec_file_operation_instance = VirtualDeviceConfigSpecFileOperation.from_json(json)
# print the JSON string representation of the object
print VirtualDeviceConfigSpecFileOperation.to_json()

# convert the object into a dict
virtual_device_config_spec_file_operation_dict = virtual_device_config_spec_file_operation_instance.to_dict()
# create an instance of VirtualDeviceConfigSpecFileOperation from a dict
virtual_device_config_spec_file_operation_form_dict = virtual_device_config_spec_file_operation.from_dict(virtual_device_config_spec_file_operation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


