# HostConfigInfo

This data object type encapsulates a typical set of host configuration information that is useful for displaying and configuring a host.  VirtualCenter can retrieve this set of information very efficiently even for a large set of hosts. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**host** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | 
**product** | [**AboutInfo**](AboutInfo.md) |  | 
**deployment_info** | [**HostDeploymentInfo**](HostDeploymentInfo.md) |  | [optional] 
**hyper_thread** | [**HostHyperThreadScheduleInfo**](HostHyperThreadScheduleInfo.md) |  | [optional] 
**console_reservation** | [**ServiceConsoleReservationInfo**](ServiceConsoleReservationInfo.md) |  | [optional] 
**virtual_machine_reservation** | [**VirtualMachineMemoryReservationInfo**](VirtualMachineMemoryReservationInfo.md) |  | [optional] 
**storage_device** | [**HostStorageDeviceInfo**](HostStorageDeviceInfo.md) |  | [optional] 
**multipath_state** | [**HostMultipathStateInfo**](HostMultipathStateInfo.md) |  | [optional] 
**file_system_volume** | [**HostFileSystemVolumeInfo**](HostFileSystemVolumeInfo.md) |  | [optional] 
**system_file** | **List[str]** | Datastore paths of files used by the host system on mounted volumes, for instance, the COS vmdk file of the host.  For information on datastore paths, see *Datastore*.  ***Since:*** vSphere API 4.1  | [optional] 
**network** | [**HostNetworkInfo**](HostNetworkInfo.md) |  | [optional] 
**vmotion** | [**HostVMotionInfo**](HostVMotionInfo.md) |  | [optional] 
**virtual_nic_manager_info** | [**HostVirtualNicManagerInfo**](HostVirtualNicManagerInfo.md) |  | [optional] 
**capabilities** | [**HostNetCapabilities**](HostNetCapabilities.md) |  | [optional] 
**datastore_capabilities** | [**HostDatastoreSystemCapabilities**](HostDatastoreSystemCapabilities.md) |  | [optional] 
**offload_capabilities** | [**HostNetOffloadCapabilities**](HostNetOffloadCapabilities.md) |  | [optional] 
**service** | [**HostServiceInfo**](HostServiceInfo.md) |  | [optional] 
**firewall** | [**HostFirewallInfo**](HostFirewallInfo.md) |  | [optional] 
**auto_start** | [**HostAutoStartManagerConfig**](HostAutoStartManagerConfig.md) |  | [optional] 
**active_diagnostic_partition** | [**HostDiagnosticPartition**](HostDiagnosticPartition.md) |  | [optional] 
**option** | [**List[OptionValue]**](OptionValue.md) | Host configuration options as defined by the *OptionValue* data object type.  | [optional] 
**option_def** | [**List[OptionDef]**](OptionDef.md) | A list of supported options.  | [optional] 
**datastore_principal** | **str** | Datastore principal user  | [optional] 
**local_swap_datastore** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | [optional] 
**system_swap_configuration** | [**HostSystemSwapConfiguration**](HostSystemSwapConfiguration.md) |  | [optional] 
**system_resources** | [**HostSystemResourceInfo**](HostSystemResourceInfo.md) |  | [optional] 
**date_time_info** | [**HostDateTimeInfo**](HostDateTimeInfo.md) |  | [optional] 
**flags** | [**HostFlagInfo**](HostFlagInfo.md) |  | [optional] 
**admin_disabled** | **bool** | Deprecated as of vSphere API 6.0, use *HostConfigInfo.lockdownMode*.  If the flag is true, the permissions on the host have been modified such that it is only accessible through local console or an authorized centralized management application.  This flag is affected by the *HostSystem.EnterLockdownMode* and *HostSystem.ExitLockdownMode* operations.  This flag is supported in VirtualCenter only. The value returned from host should be ignored.  See also *HostSystem.EnterLockdownMode*, *HostSystem.ExitLockdownMode*.  ***Since:*** VI API 2.5  | [optional] 
**lockdown_mode** | [**HostLockdownModeEnum**](HostLockdownModeEnum.md) |  | [optional] 
**ipmi** | [**HostIpmiInfo**](HostIpmiInfo.md) |  | [optional] 
**ssl_thumbprint_info** | [**HostSslThumbprintInfo**](HostSslThumbprintInfo.md) |  | [optional] 
**ssl_thumbprint_data** | [**List[HostSslThumbprintInfo]**](HostSslThumbprintInfo.md) | SSL Thumbprints registered on this host.  ***Since:*** vSphere API 5.0  | [optional] 
**certificate** | **List[int]** | Full Host Certificate in PEM format, if known  ***Since:*** vSphere API 5.0  | [optional] 
**pci_passthru_info** | [**List[HostPciPassthruInfo]**](HostPciPassthruInfo.md) | PCI passthrough information.  ***Since:*** vSphere API 4.0  | [optional] 
**authentication_manager_info** | [**HostAuthenticationManagerInfo**](HostAuthenticationManagerInfo.md) |  | [optional] 
**feature_version** | [**List[HostFeatureVersionInfo]**](HostFeatureVersionInfo.md) | List of feature-specific version information.  Each element refers to the version information for a specific feature.  ***Since:*** vSphere API 4.1  | [optional] 
**power_system_capability** | [**PowerSystemCapability**](PowerSystemCapability.md) |  | [optional] 
**power_system_info** | [**PowerSystemInfo**](PowerSystemInfo.md) |  | [optional] 
**cache_configuration_info** | [**List[HostCacheConfigurationInfo]**](HostCacheConfigurationInfo.md) | Host solid stats drive cache configuration information.  ***Since:*** vSphere API 5.0  | [optional] 
**wake_on_lan_capable** | **bool** | Indicates if a host is wake on lan capable.  A host is deemed wake on lan capable if there exists at least one physical network card that is both backing the vmotion interface and is itself wake on lan capable.  ***Since:*** vSphere API 5.0  | [optional] 
**feature_capability** | [**List[HostFeatureCapability]**](HostFeatureCapability.md) | Array of host feature capabilities.  This is expected to change infrequently. It may change while host is in maintenance mode and between reboots if hardware, firmware, or a device driver is changed or upgraded.  ***Since:*** vSphere API 5.1  | [optional] 
**masked_feature_capability** | [**List[HostFeatureCapability]**](HostFeatureCapability.md) | Array of the feature capabilities that the host has after the mask has been applied.  ***Since:*** vSphere API 5.1  | [optional] 
**v_flash_config_info** | [**HostVFlashManagerVFlashConfigInfo**](HostVFlashManagerVFlashConfigInfo.md) |  | [optional] 
**vsan_host_config** | [**VsanHostConfigInfo**](VsanHostConfigInfo.md) |  | [optional] 
**domain_list** | **List[str]** | List of Windows domains available for user searches, if the underlying system supports windows domain membership.  See *UserDirectory.domainList*.  ***Since:*** vSphere API 6.0  | [optional] 
**script_check_sum** | **bytearray** | A checksum of overhead computation script.  (For VMware internal usage only)  ***Since:*** vSphere API 6.0  | [optional] 
**host_config_check_sum** | **bytearray** | A checksum of host configuration option set.  (For VMware internal usage only)  ***Since:*** vSphere API 6.0  | [optional] 
**description_tree_check_sum** | **bytearray** | A checksum of the Assignable Hardware Description Tree.  (For VMware internal usage only)  ***Since:*** vSphere API 7.0  | [optional] 
**graphics_info** | [**List[HostGraphicsInfo]**](HostGraphicsInfo.md) | The list of graphics devices available on this host.  ***Since:*** vSphere API 5.5  | [optional] 
**shared_passthru_gpu_types** | **List[str]** | Array of shared passthru GPU types.  These GPU types may be enabled when specific host hardware is present.  ***Since:*** vSphere API 6.0  | [optional] 
**graphics_config** | [**HostGraphicsConfig**](HostGraphicsConfig.md) |  | [optional] 
**shared_gpu_capabilities** | [**List[HostSharedGpuCapabilities]**](HostSharedGpuCapabilities.md) | Array of shared passthru GPU capablities.  See also *HostSharedGpuCapabilities*.  ***Since:*** vSphere API 6.7  | [optional] 
**io_filter_info** | [**List[HostIoFilterInfo]**](HostIoFilterInfo.md) | Information of the IO Filters installed on the host.  See *HostIoFilterInfo*.  ***Since:*** vSphere API 6.0  | [optional] 
**sriov_device_pool** | [**List[HostSriovDevicePoolInfo]**](HostSriovDevicePoolInfo.md) | Information on SRIOV device pools present on host.  ***Since:*** vSphere API 6.5  | [optional] 
**assignable_hardware_binding** | [**List[HostAssignableHardwareBinding]**](HostAssignableHardwareBinding.md) | Information describing Assignable Hardware device bindings on host.  See *HostAssignableHardwareBinding*.  ***Since:*** vSphere API 7.0  | [optional] 
**assignable_hardware_config** | [**HostAssignableHardwareConfig**](HostAssignableHardwareConfig.md) |  | [optional] 

## Example

```python
from vmware_vi.models.host_config_info import HostConfigInfo

# TODO update the JSON string below
json = "{}"
# create an instance of HostConfigInfo from a JSON string
host_config_info_instance = HostConfigInfo.from_json(json)
# print the JSON string representation of the object
print HostConfigInfo.to_json()

# convert the object into a dict
host_config_info_dict = host_config_info_instance.to_dict()
# create an instance of HostConfigInfo from a dict
host_config_info_form_dict = host_config_info.from_dict(host_config_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


