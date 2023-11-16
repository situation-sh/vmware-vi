# VirtualMachinePciPassthroughInfo

Description of a generic PCI device that can be attached to a virtual machine.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pci_device** | [**HostPciDevice**](HostPciDevice.md) |  | 
**system_id** | **str** | The ID of the system the PCI device is attached to.  ***Since:*** vSphere API 4.0  | 

## Example

```python
from vmware_vi.models.virtual_machine_pci_passthrough_info import VirtualMachinePciPassthroughInfo

# TODO update the JSON string below
json = "{}"
# create an instance of VirtualMachinePciPassthroughInfo from a JSON string
virtual_machine_pci_passthrough_info_instance = VirtualMachinePciPassthroughInfo.from_json(json)
# print the JSON string representation of the object
print VirtualMachinePciPassthroughInfo.to_json()

# convert the object into a dict
virtual_machine_pci_passthrough_info_dict = virtual_machine_pci_passthrough_info_instance.to_dict()
# create an instance of VirtualMachinePciPassthroughInfo from a dict
virtual_machine_pci_passthrough_info_form_dict = virtual_machine_pci_passthrough_info.from_dict(virtual_machine_pci_passthrough_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


