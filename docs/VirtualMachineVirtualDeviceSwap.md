# VirtualMachineVirtualDeviceSwap

Device Swap: Report current status of device swap feature. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**lsi_to_pvscsi** | [**VirtualMachineVirtualDeviceSwapDeviceSwapInfo**](VirtualMachineVirtualDeviceSwapDeviceSwapInfo.md) |  | [optional] 

## Example

```python
from vmware_vi.models.virtual_machine_virtual_device_swap import VirtualMachineVirtualDeviceSwap

# TODO update the JSON string below
json = "{}"
# create an instance of VirtualMachineVirtualDeviceSwap from a JSON string
virtual_machine_virtual_device_swap_instance = VirtualMachineVirtualDeviceSwap.from_json(json)
# print the JSON string representation of the object
print VirtualMachineVirtualDeviceSwap.to_json()

# convert the object into a dict
virtual_machine_virtual_device_swap_dict = virtual_machine_virtual_device_swap_instance.to_dict()
# create an instance of VirtualMachineVirtualDeviceSwap from a dict
virtual_machine_virtual_device_swap_form_dict = virtual_machine_virtual_device_swap.from_dict(virtual_machine_virtual_device_swap_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


