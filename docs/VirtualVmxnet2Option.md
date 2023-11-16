# VirtualVmxnet2Option

The VirtualVmxnet2Option data object type contains the options for the *VirtualVmxnet2* data object type.  ***Since:*** VI API 2.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.virtual_vmxnet2_option import VirtualVmxnet2Option

# TODO update the JSON string below
json = "{}"
# create an instance of VirtualVmxnet2Option from a JSON string
virtual_vmxnet2_option_instance = VirtualVmxnet2Option.from_json(json)
# print the JSON string representation of the object
print VirtualVmxnet2Option.to_json()

# convert the object into a dict
virtual_vmxnet2_option_dict = virtual_vmxnet2_option_instance.to_dict()
# create an instance of VirtualVmxnet2Option from a dict
virtual_vmxnet2_option_form_dict = virtual_vmxnet2_option.from_dict(virtual_vmxnet2_option_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


