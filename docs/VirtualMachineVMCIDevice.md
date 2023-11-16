# VirtualMachineVMCIDevice

The *VirtualMachineVMCIDevice* data object represents a virtual communication device that supports the VMCI (Virtual Machine Communication Interface).  Each virtual machine has a VMCI device that handles interprocess socket-based communication. VMCI device information is available in the virtual machine hardware device list (*VirtualMachine*.*VirtualMachine.config*.*VirtualMachineConfigInfo.hardware*.*VirtualHardware.device*\\[\\]).  An application running on a virtual machine uses the VMCI Sockets API for communication with other virtual machines on the same host (communication between virtual machines is not supported on vSphere 5.1 and later platforms as described for VirtualVMCIDevice.*VirtualMachineVMCIDevice.allowUnrestrictedCommunication*), or for communication with the host. For information about using the vSphere VMCI Sockets API, see the _VMCI Sockets Programming Guide_.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Unique identifier for VMCI socket access to this virtual machine.  Use this value to identify this virtual machine in calls to the VMCI Sockets API. Applications running on other virtual machines on this host will use this value to connect to this virtual machine. You can cast this value to a 32-bit unsigned integer.  The vSphere Server sets this value when a virtual machine powers on. The Server may change this value after power operations such as vMotion or restoring a virtual machine from a snapshot. If you have saved a VMCI device identifier, check to see if the value is still valid after power operations.  ***Since:*** vSphere API 4.0  | [optional] 
**allow_unrestricted_communication** | **bool** | Deprecated as of vSphere API 5.1. On vSphere 5.1 and later platforms, the VMCI device does not support communication with other virtual machines. Therefore, this property has no effect on these platforms.  Determines the extent of VMCI communication with this virtual machine.  Set this property to true to allow VMCI communication with all virtual machines on the host and with trusted services. Set this property to false to allow VMCI communication only with trusted services such as the hypervisor on the host.  If unset, communication is restricted to trusted services only.  ***Since:*** vSphere API 4.0  | [optional] 
**filter_enable** | **bool** | Determines if filtering of VMCI communication is enabled for this virtual machine.  Set this property to enable or disable filter rules as specified in *VirtualMachineVMCIDevice.filterInfo*.  ***Since:*** vSphere API 6.0  | [optional] 
**filter_info** | [**VirtualMachineVMCIDeviceFilterInfo**](VirtualMachineVMCIDeviceFilterInfo.md) |  | [optional] 

## Example

```python
from vmware_vi.models.virtual_machine_vmci_device import VirtualMachineVMCIDevice

# TODO update the JSON string below
json = "{}"
# create an instance of VirtualMachineVMCIDevice from a JSON string
virtual_machine_vmci_device_instance = VirtualMachineVMCIDevice.from_json(json)
# print the JSON string representation of the object
print VirtualMachineVMCIDevice.to_json()

# convert the object into a dict
virtual_machine_vmci_device_dict = virtual_machine_vmci_device_instance.to_dict()
# create an instance of VirtualMachineVMCIDevice from a dict
virtual_machine_vmci_device_form_dict = virtual_machine_vmci_device.from_dict(virtual_machine_vmci_device_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


