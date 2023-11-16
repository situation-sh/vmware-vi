# GuestOsDescriptor

This data object type contains information to describe a particular guest operating system. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Identifier (short name) for the guest operating system.  | 
**family** | **str** | Family to which this guest operating system belongs.  | 
**full_name** | **str** | Full name of the guest operating system.  For example, if the value of \&quot;id\&quot; is \&quot;win2000Pro\&quot;, then the value of \&quot;fullName\&quot; is \&quot;Windows 2000 Professional\&quot;.  | 
**supported_max_cpus** | **int** | Maximum number of processors supported for this guest.  | 
**num_supported_physical_sockets** | **int** | Maximum number of sockets supported for this guest.  ***Since:*** vSphere API 5.0  | 
**num_supported_cores_per_socket** | **int** | Maximum number of cores per socket for this guest.  ***Since:*** vSphere API 5.0  | 
**supported_min_mem_mb** | **int** | Minimum memory requirements supported for this guest, in MB.  | 
**supported_max_mem_mb** | **int** | Maximum memory requirements supported for this guest, in MB.  | 
**recommended_mem_mb** | **int** | Recommended default memory size for this guest, in MB.  | 
**recommended_color_depth** | **int** | Recommended default color depth for this guest.  | 
**supported_disk_controller_list** | **List[str]** | List of supported disk controller types for this guest.  | 
**recommended_scsi_controller** | **str** | Recommended default SCSI controller type for this guest.  | [optional] 
**recommended_disk_controller** | **str** | Recommended default disk controller type for this guest.  | 
**supported_num_disks** | **int** | Number of disks supported for this guest.  | 
**recommended_disk_size_mb** | **int** | Recommended default disk size for this guest, in MB.  | 
**recommended_cdrom_controller** | **str** | Recommended default CD-ROM type for this guest.  ***Since:*** vSphere API 5.5  | 
**supported_ethernet_card** | **List[str]** | List of supported ethernet cards for this guest.  | 
**recommended_ethernet_card** | **str** | Recommended default ethernet controller type for this guest.  | [optional] 
**supports_slave_disk** | **bool** | Flag to indicate whether or not this guest can support a disk configured as a slave.  | [optional] 
**cpu_feature_mask** | [**List[HostCpuIdInfo]**](HostCpuIdInfo.md) | Specifies the CPU feature compatibility masks.  | [optional] 
**smc_required** | **bool** | Flag that indicates wether the guest requires an SMC (Apple hardware).  This is logically equivalent to GuestOS &#x3D; Mac OS  ***Since:*** vSphere API 5.0  | 
**supports_wake_on_lan** | **bool** | Flag to indicate whether or not this guest can support Wake-on-LAN.  | 
**supports_vmi** | **bool** | Flag indicating whether or not this guest supports the virtual machine interface.  ***Since:*** vSphere API 4.0  | 
**supports_memory_hot_add** | **bool** | Whether the memory size for this guest can be changed while the virtual machine is running.  ***Since:*** vSphere API 4.0  | 
**supports_cpu_hot_add** | **bool** | Whether virtual CPUs can be added to this guest while the virtual machine is running.  ***Since:*** vSphere API 4.0  | 
**supports_cpu_hot_remove** | **bool** | Whether virtual CPUs can be removed from this guest while the virtual machine is running.  ***Since:*** vSphere API 4.0  | 
**supported_firmware** | **List[str]** | Supported firmware types for this guest.  Possible values are described in *GuestOsDescriptorFirmwareType_enum*  ***Since:*** vSphere API 5.0  | 
**recommended_firmware** | **str** | Recommended firmware type for this guest.  Possible values are described in *GuestOsDescriptorFirmwareType_enum*  ***Since:*** vSphere API 5.0  | 
**supported_usb_controller_list** | **List[str]** | List of supported USB controllers for this guest.  ***Since:*** vSphere API 5.0  | [optional] 
**recommended_usb_controller** | **str** | Recommended default USB controller type for this guest.  ***Since:*** vSphere API 5.0  | [optional] 
**supports3_d** | **bool** | Whether this guest supports 3D graphics.  ***Since:*** vSphere API 5.0  | 
**recommended3_d** | **bool** | Recommended 3D graphics for this guest.  ***Since:*** vSphere API 5.1  | 
**smc_recommended** | **bool** | Whether SMC (Apple hardware) is recommended for this guest.  ***Since:*** vSphere API 5.0  | 
**ich7m_recommended** | **bool** | Whether I/O Controller Hub is recommended for this guest.  ***Since:*** vSphere API 5.0  | 
**usb_recommended** | **bool** | Whether USB controller is recommended for this guest.  ***Since:*** vSphere API 5.0  | 
**support_level** | **str** | Support level of this Guest Possible values are described in *GuestOsDescriptorSupportLevel_enum*  ***Since:*** vSphere API 5.0  | 
**supported_for_create** | **bool** | Whether or not this guest should be allowed for selection during virtual machine creation.  ***Since:*** vSphere API 5.0  | 
**v_ram_size_in_kb** | [**IntOption**](IntOption.md) |  | 
**num_supported_floppy_devices** | **int** | Maximum number of floppies supported by this guest.  ***Since:*** vSphere API 6.0  | 
**wake_on_lan_ethernet_card** | **List[str]** | List of NICs supported by this guest that support Wake-On-Lan.  ***Since:*** vSphere API 6.0  | [optional] 
**supports_pvscsi_controller_for_boot** | **bool** | Whether or not this guest can use pvscsi as boot adapter.  ***Since:*** vSphere API 6.0  | 
**disk_uuid_enabled** | **bool** | Whether or not this guest should have disk uuid enabled by default.  ***Since:*** vSphere API 6.0  | 
**supports_hot_plug_pci** | **bool** | Whether or not this guest supports hot plug of PCI devices.  ***Since:*** vSphere API 6.0  | 
**supports_secure_boot** | **bool** | Whether or not this guest supports Secure Boot.  If some of the OS releases that fall under this guest OS descriptor support Secure Boot, it is reasonable to offer the ability to enable Secure Boot. Only meaningful when virtual EFI firmware is in use.  ***Since:*** vSphere API 6.5  | [optional] 
**default_secure_boot** | **bool** | Whether or not Secure Boot should be enabled by default for this guest OS.  If all OS releases that fall under this guest OS descriptor support Secure Boot and are known to operate correctly with Secure Boot enabled, it is reasonable to enable it by default. Only meaningful when virtual EFI firmware is in use.  ***Since:*** vSphere API 6.5  | [optional] 
**persistent_memory_supported** | **bool** | Support of persistent memory (virtual NVDIMM device).  See also *VirtualNVDIMM*.  ***Since:*** vSphere API 6.7  | [optional] 
**supported_min_persistent_memory_mb** | **int** | Minimum persistent memory supported for this guest, in MB.  ***Since:*** vSphere API 6.7  | [optional] 
**supported_max_persistent_memory_mb** | **int** | Maximum persistent memory supported for this guest, in MB.  Total size of all the virtual NVDIMM devices should be less than this value.  ***Since:*** vSphere API 6.7  | [optional] 
**recommended_persistent_memory_mb** | **int** | Recommended default persistent memory size for this guest, in MB.  ***Since:*** vSphere API 6.7  | [optional] 
**persistent_memory_hot_add_supported** | **bool** | Support of persistent memory hot-add operation.  ***Since:*** vSphere API 6.7  | [optional] 
**persistent_memory_hot_remove_supported** | **bool** | Support of persistent memory hot-remove operation.  ***Since:*** vSphere API 6.7  | [optional] 
**persistent_memory_cold_growth_supported** | **bool** | Support of virtual NVDIMM cold-growth operation.  ***Since:*** vSphere API 6.7  | [optional] 
**persistent_memory_cold_growth_granularity_mb** | **int** | Virtual NVDIMM cold-growth granularity in MB.  ***Since:*** vSphere API 6.7  | [optional] 
**persistent_memory_hot_growth_supported** | **bool** | Support of virtual NVDIMM hot-growth operation.  ***Since:*** vSphere API 6.7  | [optional] 
**persistent_memory_hot_growth_granularity_mb** | **int** | Virtual NVDIMM hot-growth granularity in MB.  ***Since:*** vSphere API 6.7  | [optional] 
**num_recommended_physical_sockets** | **int** | Recommended number of sockets for this guest.  ***Since:*** vSphere API 6.7  | [optional] 
**num_recommended_cores_per_socket** | **int** | Recommended number of cores per socket for this guest.  ***Since:*** vSphere API 6.7  | [optional] 
**vvtd_supported** | [**BoolOption**](BoolOption.md) |  | [optional] 
**vbs_supported** | [**BoolOption**](BoolOption.md) |  | [optional] 
**vsgx_supported** | [**BoolOption**](BoolOption.md) |  | [optional] 
**vsgx_remote_attestation_supported** | **bool** | Support for Intel Software Guard Extensions remote attestation.  | [optional] 
**supports_tpm20** | **bool** | Support for TPM 2.0.  ***Since:*** vSphere API 6.7  | [optional] 
**recommended_tpm20** | **bool** | Support for default vTPM  | [optional] 
**vwdt_supported** | **bool** | Support for Virtual Watchdog Timer.  ***Since:*** vSphere API 7.0  | [optional] 

## Example

```python
from vmware_vi.models.guest_os_descriptor import GuestOsDescriptor

# TODO update the JSON string below
json = "{}"
# create an instance of GuestOsDescriptor from a JSON string
guest_os_descriptor_instance = GuestOsDescriptor.from_json(json)
# print the JSON string representation of the object
print GuestOsDescriptor.to_json()

# convert the object into a dict
guest_os_descriptor_dict = guest_os_descriptor_instance.to_dict()
# create an instance of GuestOsDescriptor from a dict
guest_os_descriptor_form_dict = guest_os_descriptor.from_dict(guest_os_descriptor_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


