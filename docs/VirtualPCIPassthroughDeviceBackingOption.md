# VirtualPCIPassthroughDeviceBackingOption

This data object type describes the options for the *VirtualPCIPassthroughDeviceBackingInfo* data object type.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.virtual_pci_passthrough_device_backing_option import VirtualPCIPassthroughDeviceBackingOption

# TODO update the JSON string below
json = "{}"
# create an instance of VirtualPCIPassthroughDeviceBackingOption from a JSON string
virtual_pci_passthrough_device_backing_option_instance = VirtualPCIPassthroughDeviceBackingOption.from_json(json)
# print the JSON string representation of the object
print VirtualPCIPassthroughDeviceBackingOption.to_json()

# convert the object into a dict
virtual_pci_passthrough_device_backing_option_dict = virtual_pci_passthrough_device_backing_option_instance.to_dict()
# create an instance of VirtualPCIPassthroughDeviceBackingOption from a dict
virtual_pci_passthrough_device_backing_option_form_dict = virtual_pci_passthrough_device_backing_option.from_dict(virtual_pci_passthrough_device_backing_option_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


