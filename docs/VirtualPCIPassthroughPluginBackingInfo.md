# VirtualPCIPassthroughPluginBackingInfo

The VirtualPCIPassthrough.PluginBackingInfo is a base data object type for encoding plugin-specific information.  This base type does not define any properties. Specific plugin types are represented by subtypes which define properties for subtype-specific backing information.  ***Since:*** vSphere API 6.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.virtual_pci_passthrough_plugin_backing_info import VirtualPCIPassthroughPluginBackingInfo

# TODO update the JSON string below
json = "{}"
# create an instance of VirtualPCIPassthroughPluginBackingInfo from a JSON string
virtual_pci_passthrough_plugin_backing_info_instance = VirtualPCIPassthroughPluginBackingInfo.from_json(json)
# print the JSON string representation of the object
print VirtualPCIPassthroughPluginBackingInfo.to_json()

# convert the object into a dict
virtual_pci_passthrough_plugin_backing_info_dict = virtual_pci_passthrough_plugin_backing_info_instance.to_dict()
# create an instance of VirtualPCIPassthroughPluginBackingInfo from a dict
virtual_pci_passthrough_plugin_backing_info_form_dict = virtual_pci_passthrough_plugin_backing_info.from_dict(virtual_pci_passthrough_plugin_backing_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


