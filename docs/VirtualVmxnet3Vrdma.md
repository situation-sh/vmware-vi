# VirtualVmxnet3Vrdma

The VirtualVmxnet3Vrdma data object type represents an instance of the VRDMA virtual Remote Direct Memory Access adapter attached to a virtual machine.  ***Since:*** vSphere API 6.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**device_protocol** | **str** | VRDMA Device protocol.  See *VirtualVmxnet3VrdmaOptionDeviceProtocols_enum* for more information.  ***Since:*** vSphere API 6.7  | [optional] 

## Example

```python
from vmware_vi.models.virtual_vmxnet3_vrdma import VirtualVmxnet3Vrdma

# TODO update the JSON string below
json = "{}"
# create an instance of VirtualVmxnet3Vrdma from a JSON string
virtual_vmxnet3_vrdma_instance = VirtualVmxnet3Vrdma.from_json(json)
# print the JSON string representation of the object
print VirtualVmxnet3Vrdma.to_json()

# convert the object into a dict
virtual_vmxnet3_vrdma_dict = virtual_vmxnet3_vrdma_instance.to_dict()
# create an instance of VirtualVmxnet3Vrdma from a dict
virtual_vmxnet3_vrdma_form_dict = virtual_vmxnet3_vrdma.from_dict(virtual_vmxnet3_vrdma_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


