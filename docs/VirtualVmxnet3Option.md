# VirtualVmxnet3Option

The VirtualVmxnet3Option data object type contains the options for the *VirtualVmxnet3* data object type.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uptv2_enabled** | [**BoolOption**](BoolOption.md) |  | [optional] 

## Example

```python
from vmware_vi.models.virtual_vmxnet3_option import VirtualVmxnet3Option

# TODO update the JSON string below
json = "{}"
# create an instance of VirtualVmxnet3Option from a JSON string
virtual_vmxnet3_option_instance = VirtualVmxnet3Option.from_json(json)
# print the JSON string representation of the object
print VirtualVmxnet3Option.to_json()

# convert the object into a dict
virtual_vmxnet3_option_dict = virtual_vmxnet3_option_instance.to_dict()
# create an instance of VirtualVmxnet3Option from a dict
virtual_vmxnet3_option_form_dict = virtual_vmxnet3_option.from_dict(virtual_vmxnet3_option_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


