# ArrayOfVirtualPCIPassthroughPluginBackingOption

A boxed array of *VirtualPCIPassthroughPluginBackingOption*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[VirtualPCIPassthroughPluginBackingOption]**](VirtualPCIPassthroughPluginBackingOption.md) |  | 

## Example

```python
from vmware_vi.models.array_of_virtual_pci_passthrough_plugin_backing_option import ArrayOfVirtualPCIPassthroughPluginBackingOption

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfVirtualPCIPassthroughPluginBackingOption from a JSON string
array_of_virtual_pci_passthrough_plugin_backing_option_instance = ArrayOfVirtualPCIPassthroughPluginBackingOption.from_json(json)
# print the JSON string representation of the object
print ArrayOfVirtualPCIPassthroughPluginBackingOption.to_json()

# convert the object into a dict
array_of_virtual_pci_passthrough_plugin_backing_option_dict = array_of_virtual_pci_passthrough_plugin_backing_option_instance.to_dict()
# create an instance of ArrayOfVirtualPCIPassthroughPluginBackingOption from a dict
array_of_virtual_pci_passthrough_plugin_backing_option_form_dict = array_of_virtual_pci_passthrough_plugin_backing_option.from_dict(array_of_virtual_pci_passthrough_plugin_backing_option_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


