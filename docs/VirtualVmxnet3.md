# VirtualVmxnet3

The VirtualVmxnet3 data object type represents an instance of the Vmxnet3 virtual Ethernet adapter attached to a virtual machine.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uptv2_enabled** | **bool** | Indicates whether UPTv2(Uniform Pass-through version 2) compatibility is enabled on this network adapter.  UPTv2 is only available on Vmxnet3 adapter. Clients can set this property enabled or disabled if ethernet virtual device is Vmxnet3. It requires the VM hardware version is compatible with ESXi version which has enabled smartnic feature.  | [optional] 

## Example

```python
from vmware_vi.models.virtual_vmxnet3 import VirtualVmxnet3

# TODO update the JSON string below
json = "{}"
# create an instance of VirtualVmxnet3 from a JSON string
virtual_vmxnet3_instance = VirtualVmxnet3.from_json(json)
# print the JSON string representation of the object
print VirtualVmxnet3.to_json()

# convert the object into a dict
virtual_vmxnet3_dict = virtual_vmxnet3_instance.to_dict()
# create an instance of VirtualVmxnet3 from a dict
virtual_vmxnet3_form_dict = virtual_vmxnet3.from_dict(virtual_vmxnet3_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


