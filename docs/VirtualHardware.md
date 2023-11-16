# VirtualHardware

The VirtualHardware data object type contains the complete configuration of the hardware in a virtual machine. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**num_cpu** | **int** | Number of virtual CPUs present in this virtual machine.  | 
**num_cores_per_socket** | **int** | Number of cores used to distribute virtual CPUs among sockets in this virtual machine.  This field should be ignored for powered off VM with autoCoresPerSocket equals TRUE, because the virtual socket size will be assigned during power-on. This field could be unset for releases prior to 7.0 U3, and it implies numCoresPerSocket is 1. In other cases, this field represents the actual virtual socket size seen by the virtual machine.  ***Since:*** vSphere API 5.0  | [optional] 
**auto_cores_per_socket** | **bool** | Cores per socket is automatically determined.  | [optional] 
**memory_mb** | **int** | Memory size, in MB.  | 
**virtual_ich7_m_present** | **bool** | Does this virtual machine have Virtual Intel I/O Controller Hub 7  ***Since:*** vSphere API 5.0  | [optional] 
**virtual_smc_present** | **bool** | Does this virtual machine have System Management Controller  ***Since:*** vSphere API 5.0  | [optional] 
**device** | [**List[VirtualDevice]**](VirtualDevice.md) | The set of virtual devices belonging to the virtual machine.  This list is unordered.  | [optional] 
**motherboard_layout** | **str** | One of motherboardLayout choices.  Default is i440bxHostBridge. See *VirtualHardware.motherboardLayout*  | [optional] 
**simultaneous_threads** | **int** | Number of SMT (Simultaneous multithreading) threads.  If unset, then system defaults are in use.  | [optional] 

## Example

```python
from vmware_vi.models.virtual_hardware import VirtualHardware

# TODO update the JSON string below
json = "{}"
# create an instance of VirtualHardware from a JSON string
virtual_hardware_instance = VirtualHardware.from_json(json)
# print the JSON string representation of the object
print VirtualHardware.to_json()

# convert the object into a dict
virtual_hardware_dict = virtual_hardware_instance.to_dict()
# create an instance of VirtualHardware from a dict
virtual_hardware_form_dict = virtual_hardware.from_dict(virtual_hardware_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


