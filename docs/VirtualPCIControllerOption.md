# VirtualPCIControllerOption

This data object type contains the options for a virtual PCI Controller. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**num_scsi_controllers** | [**IntOption**](IntOption.md) |  | 
**num_ethernet_cards** | [**IntOption**](IntOption.md) |  | 
**num_video_cards** | [**IntOption**](IntOption.md) |  | 
**num_sound_cards** | [**IntOption**](IntOption.md) |  | 
**num_vmi_roms** | [**IntOption**](IntOption.md) |  | 
**num_vmci_devices** | [**IntOption**](IntOption.md) |  | 
**num_pci_passthrough_devices** | [**IntOption**](IntOption.md) |  | 
**num_sas_scsi_controllers** | [**IntOption**](IntOption.md) |  | 
**num_vmxnet3_ethernet_cards** | [**IntOption**](IntOption.md) |  | 
**num_para_virtual_scsi_controllers** | [**IntOption**](IntOption.md) |  | 
**num_sata_controllers** | [**IntOption**](IntOption.md) |  | 
**num_nvme_controllers** | [**IntOption**](IntOption.md) |  | [optional] 
**num_vmxnet3_vrdma_ethernet_cards** | [**IntOption**](IntOption.md) |  | [optional] 

## Example

```python
from vmware_vi.models.virtual_pci_controller_option import VirtualPCIControllerOption

# TODO update the JSON string below
json = "{}"
# create an instance of VirtualPCIControllerOption from a JSON string
virtual_pci_controller_option_instance = VirtualPCIControllerOption.from_json(json)
# print the JSON string representation of the object
print VirtualPCIControllerOption.to_json()

# convert the object into a dict
virtual_pci_controller_option_dict = virtual_pci_controller_option_instance.to_dict()
# create an instance of VirtualPCIControllerOption from a dict
virtual_pci_controller_option_form_dict = virtual_pci_controller_option.from_dict(virtual_pci_controller_option_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


