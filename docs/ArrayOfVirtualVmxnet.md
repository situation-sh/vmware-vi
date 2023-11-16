# ArrayOfVirtualVmxnet

A boxed array of *VirtualVmxnet*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[VirtualVmxnet]**](VirtualVmxnet.md) |  | 

## Example

```python
from vmware_vi.models.array_of_virtual_vmxnet import ArrayOfVirtualVmxnet

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfVirtualVmxnet from a JSON string
array_of_virtual_vmxnet_instance = ArrayOfVirtualVmxnet.from_json(json)
# print the JSON string representation of the object
print ArrayOfVirtualVmxnet.to_json()

# convert the object into a dict
array_of_virtual_vmxnet_dict = array_of_virtual_vmxnet_instance.to_dict()
# create an instance of ArrayOfVirtualVmxnet from a dict
array_of_virtual_vmxnet_form_dict = array_of_virtual_vmxnet.from_dict(array_of_virtual_vmxnet_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


