# ArrayOfVirtualDeviceConfigSpecOperation

A boxed array of *VirtualDeviceConfigSpecOperation_enum*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[VirtualDeviceConfigSpecOperationEnum]**](VirtualDeviceConfigSpecOperationEnum.md) |  | 

## Example

```python
from vmware_vi.models.array_of_virtual_device_config_spec_operation import ArrayOfVirtualDeviceConfigSpecOperation

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfVirtualDeviceConfigSpecOperation from a JSON string
array_of_virtual_device_config_spec_operation_instance = ArrayOfVirtualDeviceConfigSpecOperation.from_json(json)
# print the JSON string representation of the object
print ArrayOfVirtualDeviceConfigSpecOperation.to_json()

# convert the object into a dict
array_of_virtual_device_config_spec_operation_dict = array_of_virtual_device_config_spec_operation_instance.to_dict()
# create an instance of ArrayOfVirtualDeviceConfigSpecOperation from a dict
array_of_virtual_device_config_spec_operation_form_dict = array_of_virtual_device_config_spec_operation.from_dict(array_of_virtual_device_config_spec_operation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


