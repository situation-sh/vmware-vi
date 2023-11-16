# VirtualVmxnet

The VirtualVmxnet data object type represents an instance of the Vmxnet virtual Ethernet adapter attached to a virtual machine. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.virtual_vmxnet import VirtualVmxnet

# TODO update the JSON string below
json = "{}"
# create an instance of VirtualVmxnet from a JSON string
virtual_vmxnet_instance = VirtualVmxnet.from_json(json)
# print the JSON string representation of the object
print VirtualVmxnet.to_json()

# convert the object into a dict
virtual_vmxnet_dict = virtual_vmxnet_instance.to_dict()
# create an instance of VirtualVmxnet from a dict
virtual_vmxnet_form_dict = virtual_vmxnet.from_dict(virtual_vmxnet_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


