# VirtualMachineVMCIDeviceOption

The *VirtualMachineVMCIDeviceOption* data object contains the options for the virtual VMCI device (*VirtualMachineVMCIDevice*).  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allow_unrestricted_communication** | [**BoolOption**](BoolOption.md) |  | 
**filter_spec_option** | [**VirtualMachineVMCIDeviceOptionFilterSpecOption**](VirtualMachineVMCIDeviceOptionFilterSpecOption.md) |  | [optional] 
**filter_supported** | [**BoolOption**](BoolOption.md) |  | [optional] 

## Example

```python
from vmware_vi.models.virtual_machine_vmci_device_option import VirtualMachineVMCIDeviceOption

# TODO update the JSON string below
json = "{}"
# create an instance of VirtualMachineVMCIDeviceOption from a JSON string
virtual_machine_vmci_device_option_instance = VirtualMachineVMCIDeviceOption.from_json(json)
# print the JSON string representation of the object
print VirtualMachineVMCIDeviceOption.to_json()

# convert the object into a dict
virtual_machine_vmci_device_option_dict = virtual_machine_vmci_device_option_instance.to_dict()
# create an instance of VirtualMachineVMCIDeviceOption from a dict
virtual_machine_vmci_device_option_form_dict = virtual_machine_vmci_device_option.from_dict(virtual_machine_vmci_device_option_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


