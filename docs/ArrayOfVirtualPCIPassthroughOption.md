# ArrayOfVirtualPCIPassthroughOption

A boxed array of *VirtualPCIPassthroughOption*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[VirtualPCIPassthroughOption]**](VirtualPCIPassthroughOption.md) |  | 

## Example

```python
from vmware_vi.models.array_of_virtual_pci_passthrough_option import ArrayOfVirtualPCIPassthroughOption

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfVirtualPCIPassthroughOption from a JSON string
array_of_virtual_pci_passthrough_option_instance = ArrayOfVirtualPCIPassthroughOption.from_json(json)
# print the JSON string representation of the object
print ArrayOfVirtualPCIPassthroughOption.to_json()

# convert the object into a dict
array_of_virtual_pci_passthrough_option_dict = array_of_virtual_pci_passthrough_option_instance.to_dict()
# create an instance of ArrayOfVirtualPCIPassthroughOption from a dict
array_of_virtual_pci_passthrough_option_form_dict = array_of_virtual_pci_passthrough_option.from_dict(array_of_virtual_pci_passthrough_option_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


