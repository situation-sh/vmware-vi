# VirtualVmxnet2

The VirtualVmxnet2 data object type represents an instance of the Vmxnet2 virtual Ethernet adapter attached to a virtual machine.  ***Since:*** VI API 2.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.virtual_vmxnet2 import VirtualVmxnet2

# TODO update the JSON string below
json = "{}"
# create an instance of VirtualVmxnet2 from a JSON string
virtual_vmxnet2_instance = VirtualVmxnet2.from_json(json)
# print the JSON string representation of the object
print VirtualVmxnet2.to_json()

# convert the object into a dict
virtual_vmxnet2_dict = virtual_vmxnet2_instance.to_dict()
# create an instance of VirtualVmxnet2 from a dict
virtual_vmxnet2_form_dict = virtual_vmxnet2.from_dict(virtual_vmxnet2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


