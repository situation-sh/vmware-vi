# VirtualHardwareOption

The VirtualHardwareOption data object contains the options available for all virtual devices. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hw_version** | **int** | The virtual hardware version.  | 
**virtual_device_option** | [**List[VirtualDeviceOption]**](VirtualDeviceOption.md) | Array of virtual device options valid for this virtual machine configuration.  The list is unordered.  | 
**device_list_readonly** | **bool** | Whether the set of virtual devices can be changed, e.g., can devices be added or removed.  This does not preclude changing devices.  | 
**num_cpu** | **List[int]** | List of acceptable values for the number of CPUs supported by this *ConfigOption*.  This is usually superceded by the information available in the guest operating system descriptors. The guest operating system descriptor describes a maximum CPU count, but the acceptable values are still constrained to the set specified here. The default value is stored at index 0 in the list.  | 
**num_cores_per_socket** | [**IntOption**](IntOption.md) |  | 
**auto_cores_per_socket** | [**BoolOption**](BoolOption.md) |  | [optional] 
**num_cpu_readonly** | **bool** | Can the number of virtual CPUs be changed  | 
**memory_mb** | [**LongOption**](LongOption.md) |  | 
**num_pci_controllers** | [**IntOption**](IntOption.md) |  | 
**num_ide_controllers** | [**IntOption**](IntOption.md) |  | 
**num_usb_controllers** | [**IntOption**](IntOption.md) |  | 
**num_usbxhci_controllers** | [**IntOption**](IntOption.md) |  | 
**num_sio_controllers** | [**IntOption**](IntOption.md) |  | 
**num_ps2_controllers** | [**IntOption**](IntOption.md) |  | 
**licensing_limit** | **List[str]** | List of propery names which limits are given be a licensing restriction of the underlying product, e.g., a limit that is not derived based on the product or hardware features.  For example, the property name \&quot;numCPU\&quot;  | [optional] 
**num_supported_wwn_ports** | [**IntOption**](IntOption.md) |  | [optional] 
**num_supported_wwn_nodes** | [**IntOption**](IntOption.md) |  | [optional] 
**resource_config_option** | [**ResourceConfigOption**](ResourceConfigOption.md) |  | 
**num_nvdimm_controllers** | [**IntOption**](IntOption.md) |  | [optional] 
**num_tpm_devices** | [**IntOption**](IntOption.md) |  | [optional] 
**num_wdt_devices** | [**IntOption**](IntOption.md) |  | [optional] 
**num_precision_clock_devices** | [**IntOption**](IntOption.md) |  | [optional] 
**epc_memory_mb** | [**LongOption**](LongOption.md) |  | [optional] 
**acpi_host_bridges_firmware** | **List[str]** | Empty for HWv17 &amp;amp; older, \\[\&quot;efi\&quot;\\] for HWv18.  | [optional] 
**num_cpu_simultaneous_threads** | [**IntOption**](IntOption.md) |  | [optional] 
**num_numa_nodes** | [**IntOption**](IntOption.md) |  | [optional] 
**num_device_groups** | [**IntOption**](IntOption.md) |  | [optional] 
**device_group_types** | **List[str]** | Supported device group types.  | [optional] 

## Example

```python
from vmware_vi.models.virtual_hardware_option import VirtualHardwareOption

# TODO update the JSON string below
json = "{}"
# create an instance of VirtualHardwareOption from a JSON string
virtual_hardware_option_instance = VirtualHardwareOption.from_json(json)
# print the JSON string representation of the object
print VirtualHardwareOption.to_json()

# convert the object into a dict
virtual_hardware_option_dict = virtual_hardware_option_instance.to_dict()
# create an instance of VirtualHardwareOption from a dict
virtual_hardware_option_form_dict = virtual_hardware_option.from_dict(virtual_hardware_option_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


