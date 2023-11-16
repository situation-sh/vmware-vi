# ArrayOfVirtualPCIPassthroughDynamicBackingOption

A boxed array of *VirtualPCIPassthroughDynamicBackingOption*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[VirtualPCIPassthroughDynamicBackingOption]**](VirtualPCIPassthroughDynamicBackingOption.md) |  | 

## Example

```python
from vmware_vi.models.array_of_virtual_pci_passthrough_dynamic_backing_option import ArrayOfVirtualPCIPassthroughDynamicBackingOption

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfVirtualPCIPassthroughDynamicBackingOption from a JSON string
array_of_virtual_pci_passthrough_dynamic_backing_option_instance = ArrayOfVirtualPCIPassthroughDynamicBackingOption.from_json(json)
# print the JSON string representation of the object
print ArrayOfVirtualPCIPassthroughDynamicBackingOption.to_json()

# convert the object into a dict
array_of_virtual_pci_passthrough_dynamic_backing_option_dict = array_of_virtual_pci_passthrough_dynamic_backing_option_instance.to_dict()
# create an instance of ArrayOfVirtualPCIPassthroughDynamicBackingOption from a dict
array_of_virtual_pci_passthrough_dynamic_backing_option_form_dict = array_of_virtual_pci_passthrough_dynamic_backing_option.from_dict(array_of_virtual_pci_passthrough_dynamic_backing_option_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


