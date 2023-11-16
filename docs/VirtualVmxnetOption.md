# VirtualVmxnetOption

The VirtualVmxnetOption data object type contains the options for the *VirtualVmxnet* data object type. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.virtual_vmxnet_option import VirtualVmxnetOption

# TODO update the JSON string below
json = "{}"
# create an instance of VirtualVmxnetOption from a JSON string
virtual_vmxnet_option_instance = VirtualVmxnetOption.from_json(json)
# print the JSON string representation of the object
print VirtualVmxnetOption.to_json()

# convert the object into a dict
virtual_vmxnet_option_dict = virtual_vmxnet_option_instance.to_dict()
# create an instance of VirtualVmxnetOption from a dict
virtual_vmxnet_option_form_dict = virtual_vmxnet_option.from_dict(virtual_vmxnet_option_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


