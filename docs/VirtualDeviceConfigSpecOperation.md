# VirtualDeviceConfigSpecOperation

A boxed *VirtualDeviceConfigSpecOperation_enum*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**VirtualDeviceConfigSpecOperationEnum**](VirtualDeviceConfigSpecOperationEnum.md) |  | 

## Example

```python
from vmware_vi.models.virtual_device_config_spec_operation import VirtualDeviceConfigSpecOperation

# TODO update the JSON string below
json = "{}"
# create an instance of VirtualDeviceConfigSpecOperation from a JSON string
virtual_device_config_spec_operation_instance = VirtualDeviceConfigSpecOperation.from_json(json)
# print the JSON string representation of the object
print VirtualDeviceConfigSpecOperation.to_json()

# convert the object into a dict
virtual_device_config_spec_operation_dict = virtual_device_config_spec_operation_instance.to_dict()
# create an instance of VirtualDeviceConfigSpecOperation from a dict
virtual_device_config_spec_operation_form_dict = virtual_device_config_spec_operation.from_dict(virtual_device_config_spec_operation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


