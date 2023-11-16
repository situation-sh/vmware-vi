# VirtualMachineVMCIDeviceOptionFilterSpecOption

Filter specification options.  Indicates options for each filter specification, as defined by *VirtualMachineVMCIDeviceFilterSpec*.  ***Since:*** vSphere API 6.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | [**ChoiceOption**](ChoiceOption.md) |  | 
**protocol** | [**ChoiceOption**](ChoiceOption.md) |  | 
**direction** | [**ChoiceOption**](ChoiceOption.md) |  | 
**lower_dst_port_boundary** | [**LongOption**](LongOption.md) |  | 
**upper_dst_port_boundary** | [**LongOption**](LongOption.md) |  | 

## Example

```python
from vmware_vi.models.virtual_machine_vmci_device_option_filter_spec_option import VirtualMachineVMCIDeviceOptionFilterSpecOption

# TODO update the JSON string below
json = "{}"
# create an instance of VirtualMachineVMCIDeviceOptionFilterSpecOption from a JSON string
virtual_machine_vmci_device_option_filter_spec_option_instance = VirtualMachineVMCIDeviceOptionFilterSpecOption.from_json(json)
# print the JSON string representation of the object
print VirtualMachineVMCIDeviceOptionFilterSpecOption.to_json()

# convert the object into a dict
virtual_machine_vmci_device_option_filter_spec_option_dict = virtual_machine_vmci_device_option_filter_spec_option_instance.to_dict()
# create an instance of VirtualMachineVMCIDeviceOptionFilterSpecOption from a dict
virtual_machine_vmci_device_option_filter_spec_option_form_dict = virtual_machine_vmci_device_option_filter_spec_option.from_dict(virtual_machine_vmci_device_option_filter_spec_option_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


