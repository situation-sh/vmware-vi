# VirtualPCIPassthroughPluginBackingOption

This data object type describes the options for the *VirtualPCIPassthroughPluginBackingInfo* data object type.  ***Since:*** vSphere API 6.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.virtual_pci_passthrough_plugin_backing_option import VirtualPCIPassthroughPluginBackingOption

# TODO update the JSON string below
json = "{}"
# create an instance of VirtualPCIPassthroughPluginBackingOption from a JSON string
virtual_pci_passthrough_plugin_backing_option_instance = VirtualPCIPassthroughPluginBackingOption.from_json(json)
# print the JSON string representation of the object
print VirtualPCIPassthroughPluginBackingOption.to_json()

# convert the object into a dict
virtual_pci_passthrough_plugin_backing_option_dict = virtual_pci_passthrough_plugin_backing_option_instance.to_dict()
# create an instance of VirtualPCIPassthroughPluginBackingOption from a dict
virtual_pci_passthrough_plugin_backing_option_form_dict = virtual_pci_passthrough_plugin_backing_option.from_dict(virtual_pci_passthrough_plugin_backing_option_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


