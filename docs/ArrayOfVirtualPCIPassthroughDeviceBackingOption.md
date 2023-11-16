# ArrayOfVirtualPCIPassthroughDeviceBackingOption

A boxed array of *VirtualPCIPassthroughDeviceBackingOption*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[VirtualPCIPassthroughDeviceBackingOption]**](VirtualPCIPassthroughDeviceBackingOption.md) |  | 

## Example

```python
from vmware_vi.models.array_of_virtual_pci_passthrough_device_backing_option import ArrayOfVirtualPCIPassthroughDeviceBackingOption

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfVirtualPCIPassthroughDeviceBackingOption from a JSON string
array_of_virtual_pci_passthrough_device_backing_option_instance = ArrayOfVirtualPCIPassthroughDeviceBackingOption.from_json(json)
# print the JSON string representation of the object
print ArrayOfVirtualPCIPassthroughDeviceBackingOption.to_json()

# convert the object into a dict
array_of_virtual_pci_passthrough_device_backing_option_dict = array_of_virtual_pci_passthrough_device_backing_option_instance.to_dict()
# create an instance of ArrayOfVirtualPCIPassthroughDeviceBackingOption from a dict
array_of_virtual_pci_passthrough_device_backing_option_form_dict = array_of_virtual_pci_passthrough_device_backing_option.from_dict(array_of_virtual_pci_passthrough_device_backing_option_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

