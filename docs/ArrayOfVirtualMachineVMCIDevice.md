# ArrayOfVirtualMachineVMCIDevice

A boxed array of *VirtualMachineVMCIDevice*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[VirtualMachineVMCIDevice]**](VirtualMachineVMCIDevice.md) |  | 

## Example

```python
from vmware_vi.models.array_of_virtual_machine_vmci_device import ArrayOfVirtualMachineVMCIDevice

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfVirtualMachineVMCIDevice from a JSON string
array_of_virtual_machine_vmci_device_instance = ArrayOfVirtualMachineVMCIDevice.from_json(json)
# print the JSON string representation of the object
print ArrayOfVirtualMachineVMCIDevice.to_json()

# convert the object into a dict
array_of_virtual_machine_vmci_device_dict = array_of_virtual_machine_vmci_device_instance.to_dict()
# create an instance of ArrayOfVirtualMachineVMCIDevice from a dict
array_of_virtual_machine_vmci_device_form_dict = array_of_virtual_machine_vmci_device.from_dict(array_of_virtual_machine_vmci_device_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


