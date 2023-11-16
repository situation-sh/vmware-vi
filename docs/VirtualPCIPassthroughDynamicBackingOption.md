# VirtualPCIPassthroughDynamicBackingOption

This data object type describes the options for the *VirtualPCIPassthroughDynamicBackingInfo* data object type.  ***Since:*** vSphere API 7.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.virtual_pci_passthrough_dynamic_backing_option import VirtualPCIPassthroughDynamicBackingOption

# TODO update the JSON string below
json = "{}"
# create an instance of VirtualPCIPassthroughDynamicBackingOption from a JSON string
virtual_pci_passthrough_dynamic_backing_option_instance = VirtualPCIPassthroughDynamicBackingOption.from_json(json)
# print the JSON string representation of the object
print VirtualPCIPassthroughDynamicBackingOption.to_json()

# convert the object into a dict
virtual_pci_passthrough_dynamic_backing_option_dict = virtual_pci_passthrough_dynamic_backing_option_instance.to_dict()
# create an instance of VirtualPCIPassthroughDynamicBackingOption from a dict
virtual_pci_passthrough_dynamic_backing_option_form_dict = virtual_pci_passthrough_dynamic_backing_option.from_dict(virtual_pci_passthrough_dynamic_backing_option_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


