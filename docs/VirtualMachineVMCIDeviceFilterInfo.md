# VirtualMachineVMCIDeviceFilterInfo

The *VirtualMachineVMCIDeviceFilterInfo* data object contains an array of filters.  To clear all existing filters, leave filters unset or specify an empty array.  ***Since:*** vSphere API 6.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filters** | [**List[VirtualMachineVMCIDeviceFilterSpec]**](VirtualMachineVMCIDeviceFilterSpec.md) |  | [optional] 

## Example

```python
from vmware_vi.models.virtual_machine_vmci_device_filter_info import VirtualMachineVMCIDeviceFilterInfo

# TODO update the JSON string below
json = "{}"
# create an instance of VirtualMachineVMCIDeviceFilterInfo from a JSON string
virtual_machine_vmci_device_filter_info_instance = VirtualMachineVMCIDeviceFilterInfo.from_json(json)
# print the JSON string representation of the object
print VirtualMachineVMCIDeviceFilterInfo.to_json()

# convert the object into a dict
virtual_machine_vmci_device_filter_info_dict = virtual_machine_vmci_device_filter_info_instance.to_dict()
# create an instance of VirtualMachineVMCIDeviceFilterInfo from a dict
virtual_machine_vmci_device_filter_info_form_dict = virtual_machine_vmci_device_filter_info.from_dict(virtual_machine_vmci_device_filter_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


