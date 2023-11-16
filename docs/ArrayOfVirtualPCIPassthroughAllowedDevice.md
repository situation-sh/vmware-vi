# ArrayOfVirtualPCIPassthroughAllowedDevice

A boxed array of *VirtualPCIPassthroughAllowedDevice*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[VirtualPCIPassthroughAllowedDevice]**](VirtualPCIPassthroughAllowedDevice.md) |  | 

## Example

```python
from vmware_vi.models.array_of_virtual_pci_passthrough_allowed_device import ArrayOfVirtualPCIPassthroughAllowedDevice

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfVirtualPCIPassthroughAllowedDevice from a JSON string
array_of_virtual_pci_passthrough_allowed_device_instance = ArrayOfVirtualPCIPassthroughAllowedDevice.from_json(json)
# print the JSON string representation of the object
print ArrayOfVirtualPCIPassthroughAllowedDevice.to_json()

# convert the object into a dict
array_of_virtual_pci_passthrough_allowed_device_dict = array_of_virtual_pci_passthrough_allowed_device_instance.to_dict()
# create an instance of ArrayOfVirtualPCIPassthroughAllowedDevice from a dict
array_of_virtual_pci_passthrough_allowed_device_form_dict = array_of_virtual_pci_passthrough_allowed_device.from_dict(array_of_virtual_pci_passthrough_allowed_device_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


