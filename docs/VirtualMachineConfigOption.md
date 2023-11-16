# VirtualMachineConfigOption

This configuration data object type contains information about the execution environment for a virtual machine.  This includes information about which features are supported, such as: - Which guest operating systems are supported. - How devices are emulated. For example, that a CD-ROM drive can be emulated   with a file or that a serial port can be emulated with a pipe.    VirtualCenter can provide a broader environment than any single physical host. This is a departure from traditional virtualization approaches, which rely on the host system to define the environment for virtual machines. This data object describes environment capabilities and is used by VirtualCenter to choose hosts on which to run virtual machines. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**version** | **str** | The version corresponding to this configOption.  | 
**description** | **str** | A description string for this configOption.  | 
**guest_os_descriptor** | [**List[GuestOsDescriptor]**](GuestOsDescriptor.md) | List of supported guest operating systems.  The choice of guest operating system may limit the set of valid devices. For example, you cannot select Vmxnet with all guest operating systems.  | 
**guest_os_default_index** | **int** | Index into guestOsDescriptor array denoting the default guest operating system.  | 
**hardware_options** | [**VirtualHardwareOption**](VirtualHardwareOption.md) |  | 
**capabilities** | [**VirtualMachineCapability**](VirtualMachineCapability.md) |  | 
**datastore** | [**DatastoreOption**](DatastoreOption.md) |  | 
**default_device** | [**List[VirtualDevice]**](VirtualDevice.md) | The list of virtual devices that are created on a virtual machine by default.  Clients should not create these devices.  | [optional] 
**supported_monitor_type** | **List[str]** | The monitor types supported by a host.  The acceptable monitor types are enumerated by *VirtualMachineFlagInfoMonitorType_enum*.  ***Since:*** VI API 2.5  | 
**supported_ovf_environment_transport** | **List[str]** | Specifies the supported property transports that are available for the OVF environment  ***Since:*** vSphere API 4.0  | [optional] 
**supported_ovf_install_transport** | **List[str]** | Specifies the supported transports for the OVF installation phase.  ***Since:*** vSphere API 4.0  | [optional] 
**property_relations** | [**List[VirtualMachinePropertyRelation]**](VirtualMachinePropertyRelation.md) | The relations between the properties of the virtual machine config spec.  ***Since:*** vSphere API 6.7  | [optional] 

## Example

```python
from vmware_vi.models.virtual_machine_config_option import VirtualMachineConfigOption

# TODO update the JSON string below
json = "{}"
# create an instance of VirtualMachineConfigOption from a JSON string
virtual_machine_config_option_instance = VirtualMachineConfigOption.from_json(json)
# print the JSON string representation of the object
print VirtualMachineConfigOption.to_json()

# convert the object into a dict
virtual_machine_config_option_dict = virtual_machine_config_option_instance.to_dict()
# create an instance of VirtualMachineConfigOption from a dict
virtual_machine_config_option_form_dict = virtual_machine_config_option.from_dict(virtual_machine_config_option_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


