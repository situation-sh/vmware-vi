# ArrayOfVirtualMachineVMCIDeviceFilterInfo

A boxed array of *VirtualMachineVMCIDeviceFilterInfo*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[VirtualMachineVMCIDeviceFilterInfo]**](VirtualMachineVMCIDeviceFilterInfo.md) |  | 

## Example

```python
from vmware_vi.models.array_of_virtual_machine_vmci_device_filter_info import ArrayOfVirtualMachineVMCIDeviceFilterInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfVirtualMachineVMCIDeviceFilterInfo from a JSON string
array_of_virtual_machine_vmci_device_filter_info_instance = ArrayOfVirtualMachineVMCIDeviceFilterInfo.from_json(json)
# print the JSON string representation of the object
print ArrayOfVirtualMachineVMCIDeviceFilterInfo.to_json()

# convert the object into a dict
array_of_virtual_machine_vmci_device_filter_info_dict = array_of_virtual_machine_vmci_device_filter_info_instance.to_dict()
# create an instance of ArrayOfVirtualMachineVMCIDeviceFilterInfo from a dict
array_of_virtual_machine_vmci_device_filter_info_form_dict = array_of_virtual_machine_vmci_device_filter_info.from_dict(array_of_virtual_machine_vmci_device_filter_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


