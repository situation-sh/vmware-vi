# VirtualMachineVirtualDeviceSwapDeviceSwapInfo

Information for the device swap operation. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** | Is the swap operation enabled for this virtual machine.  | [optional] 
**applicable** | **bool** | Is the swap operation applicable to this virtual machine? Operation is applicable if it is enabled for the virtual machine, for the host or cluster in which virtual machine resides, operating system supports device swap, and virtual machine has controllers that need to be replaced.  This field is read-only and cannot be modified.  | [optional] 
**status** | **str** | Status of the operation.  One of *VirtualMachineVirtualDeviceSwapDeviceSwapStatus_enum* This field is read-only and cannot be modified.  | [optional] 

## Example

```python
from vmware_vi.models.virtual_machine_virtual_device_swap_device_swap_info import VirtualMachineVirtualDeviceSwapDeviceSwapInfo

# TODO update the JSON string below
json = "{}"
# create an instance of VirtualMachineVirtualDeviceSwapDeviceSwapInfo from a JSON string
virtual_machine_virtual_device_swap_device_swap_info_instance = VirtualMachineVirtualDeviceSwapDeviceSwapInfo.from_json(json)
# print the JSON string representation of the object
print VirtualMachineVirtualDeviceSwapDeviceSwapInfo.to_json()

# convert the object into a dict
virtual_machine_virtual_device_swap_device_swap_info_dict = virtual_machine_virtual_device_swap_device_swap_info_instance.to_dict()
# create an instance of VirtualMachineVirtualDeviceSwapDeviceSwapInfo from a dict
virtual_machine_virtual_device_swap_device_swap_info_form_dict = virtual_machine_virtual_device_swap_device_swap_info.from_dict(virtual_machine_virtual_device_swap_device_swap_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


