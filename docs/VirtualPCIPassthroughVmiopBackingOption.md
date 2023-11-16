# VirtualPCIPassthroughVmiopBackingOption

This data object type describes the options for the *VirtualPCIPassthroughVmiopBackingInfo* data object type.  ***Since:*** vSphere API 6.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vgpu** | [**StringOption**](StringOption.md) |  | 
**max_instances** | **int** | Maximum number of instances of this backing type allowed per virtual machine.  This is a parameter of the plugin itself, which may support only a limited number of instances per virtual machine.  ***Since:*** vSphere API 6.0  | 

## Example

```python
from vmware_vi.models.virtual_pci_passthrough_vmiop_backing_option import VirtualPCIPassthroughVmiopBackingOption

# TODO update the JSON string below
json = "{}"
# create an instance of VirtualPCIPassthroughVmiopBackingOption from a JSON string
virtual_pci_passthrough_vmiop_backing_option_instance = VirtualPCIPassthroughVmiopBackingOption.from_json(json)
# print the JSON string representation of the object
print VirtualPCIPassthroughVmiopBackingOption.to_json()

# convert the object into a dict
virtual_pci_passthrough_vmiop_backing_option_dict = virtual_pci_passthrough_vmiop_backing_option_instance.to_dict()
# create an instance of VirtualPCIPassthroughVmiopBackingOption from a dict
virtual_pci_passthrough_vmiop_backing_option_form_dict = virtual_pci_passthrough_vmiop_backing_option.from_dict(virtual_pci_passthrough_vmiop_backing_option_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


