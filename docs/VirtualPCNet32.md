# VirtualPCNet32

This data object type defines the properties of an AMD Lance PCNet32 Ethernet card attached to a virtual machine. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.virtual_pc_net32 import VirtualPCNet32

# TODO update the JSON string below
json = "{}"
# create an instance of VirtualPCNet32 from a JSON string
virtual_pc_net32_instance = VirtualPCNet32.from_json(json)
# print the JSON string representation of the object
print VirtualPCNet32.to_json()

# convert the object into a dict
virtual_pc_net32_dict = virtual_pc_net32_instance.to_dict()
# create an instance of VirtualPCNet32 from a dict
virtual_pc_net32_form_dict = virtual_pc_net32.from_dict(virtual_pc_net32_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


