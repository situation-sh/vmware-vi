# VirtualVmxnet3VrdmaOption

The VirtualVmxnet3VrdmaOption data object type contains the options for the *VirtualVmxnet3Vrdma* data object type.  ***Since:*** vSphere API 6.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**device_protocol** | [**ChoiceOption**](ChoiceOption.md) |  | [optional] 

## Example

```python
from vmware_vi.models.virtual_vmxnet3_vrdma_option import VirtualVmxnet3VrdmaOption

# TODO update the JSON string below
json = "{}"
# create an instance of VirtualVmxnet3VrdmaOption from a JSON string
virtual_vmxnet3_vrdma_option_instance = VirtualVmxnet3VrdmaOption.from_json(json)
# print the JSON string representation of the object
print VirtualVmxnet3VrdmaOption.to_json()

# convert the object into a dict
virtual_vmxnet3_vrdma_option_dict = virtual_vmxnet3_vrdma_option_instance.to_dict()
# create an instance of VirtualVmxnet3VrdmaOption from a dict
virtual_vmxnet3_vrdma_option_form_dict = virtual_vmxnet3_vrdma_option.from_dict(virtual_vmxnet3_vrdma_option_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


