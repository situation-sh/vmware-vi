# VirtualMachineConfigInfo

The ConfigInfo data object type encapsulates the configuration settings and virtual hardware for a virtual machine.  This type holds all the information that is present in the .vmx configuration file for the virtual machine. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**change_version** | **str** | The changeVersion is a unique identifier for a given version of the configuration.  Each change to the configuration updates this value. This is typically implemented as an ever increasing count or a time-stamp. However, a client should always treat this as an opaque string.  | 
**modified** | **datetime** | Last time a virtual machine&#39;s configuration was modified.  | 
**name** | **str** | Display name of the virtual machine.  Any / (slash), \\\\ (backslash), character used in this name element is escaped. Similarly, any % (percent) character used in this name element is escaped, unless it is used to start an escape sequence. A slash is escaped as %2F or %2f. A backslash is escaped as %5C or %5c, and a percent is escaped as %25.  | 
**guest_full_name** | **str** | This is the full name of the guest operating system for the virtual machine.  For example: Windows 2000 Professional.  See also *VirtualMachineConfigInfo.alternateGuestName*.  | 
**version** | **str** | The version string for this virtual machine.  | 
**uuid** | **str** | 128-bit SMBIOS UUID of a virtual machine represented as a hexadecimal string in \&quot;12345678-abcd-1234-cdef-123456789abc\&quot; format.  | 
**create_date** | **datetime** | Time the virtual machine&#39;s configuration was created.  ***Since:*** vSphere API 6.7  | [optional] 
**instance_uuid** | **str** | VirtualCenter-specific 128-bit UUID of a virtual machine, represented as a hexademical string.  This identifier is used by VirtualCenter to uniquely identify all virtual machine instances, including those that may share the same SMBIOS UUID.  ***Since:*** vSphere API 4.0  | [optional] 
**npiv_node_world_wide_name** | **List[int]** | A 64-bit node WWN (World Wide Name).  These WWNs are paired with the *VirtualMachineConfigInfo.npivPortWorldWideName* to be used by the NPIV VPORTs instantiated for the virtual machine on the physical HBAs of the host. A pair of node and port WWNs serves as a unique identifier in accessing a LUN, so that it can be monitored or controlled by the storage administrator.  If this property contains a single node WWN, the same node WWN is used to pair with all port WWNs listed in *VirtualMachineConfigInfo.npivPortWorldWideName*. If this property or *VirtualMachineConfigInfo.npivPortWorldWideName* is empty or unset, NPIV WWN is disabled for the virtual machine.  ***Since:*** VI API 2.5  | [optional] 
**npiv_port_world_wide_name** | **List[int]** | A 64-bit port WWN (World Wide Name).  For detail description on WWN, see *VirtualMachineConfigInfo.npivNodeWorldWideName*.  ***Since:*** VI API 2.5  | [optional] 
**npiv_world_wide_name_type** | **str** | The source that provides/generates the assigned WWNs.  See also *VirtualMachineConfigInfoNpivWwnType_enum*.  ***Since:*** VI API 2.5  | [optional] 
**npiv_desired_node_wwns** | **int** | The NPIV node WWNs to be extended from the original list of WWN nummbers.  This property should be set to desired number which is an aggregate of existing plus new numbers. Desired Node WWNs should always be greater than the existing number of node WWNs  ***Since:*** vSphere API 4.0  | [optional] 
**npiv_desired_port_wwns** | **int** | The NPIV port WWNs to be extended from the original list of WWN nummbers.  This property should be set to desired number which is an aggregate of existing plus new numbers. Desired Node WWNs should always be greater than the existing number of port WWNs  ***Since:*** vSphere API 4.0  | [optional] 
**npiv_temporary_disabled** | **bool** | This property is used to enable or disable the NPIV capability on a desired virtual machine on a temporary basis.  When this property is set NPIV Vport will not be instantiated by the VMX process of the Virtual Machine. When this property is set port WWNs and node WWNs in the VM configuration are preserved.  ***Since:*** vSphere API 4.0  | [optional] 
**npiv_on_non_rdm_disks** | **bool** | This property is used to check whether the NPIV can be enabled on the Virtual machine with non-rdm disks in the configuration, so this is potentially not enabling npiv on vmfs disks.  Also this property is used to check whether RDM is required to generate WWNs for a virtual machine.  ***Since:*** vSphere API 4.0  | [optional] 
**location_id** | **str** | Hash incorporating the virtual machine&#39;s config file location and the UUID of the host assigned to run the virtual machine.  | [optional] 
**template** | **bool** | Flag indicating whether or not a virtual machine is a template.  | 
**guest_id** | **str** | Guest operating system configured on a virtual machine.  This is a guest identifier that can be used to access the *GuestOsDescriptor* list for information about default configuration. For more information on possible values, see *VirtualMachineGuestOsIdentifier*.  | 
**alternate_guest_name** | **str** | Used as display name for the operating system if guestId is &#x60;other&#x60; or &#x60;other-64&#x60;.  See also *VirtualMachineConfigInfo.guestFullName*.  ***Since:*** VI API 2.5  | 
**annotation** | **str** | Description for the virtual machine.  | [optional] 
**files** | [**VirtualMachineFileInfo**](VirtualMachineFileInfo.md) |  | 
**tools** | [**ToolsConfigInfo**](ToolsConfigInfo.md) |  | [optional] 
**flags** | [**VirtualMachineFlagInfo**](VirtualMachineFlagInfo.md) |  | 
**console_preferences** | [**VirtualMachineConsolePreferences**](VirtualMachineConsolePreferences.md) |  | [optional] 
**default_power_ops** | [**VirtualMachineDefaultPowerOpInfo**](VirtualMachineDefaultPowerOpInfo.md) |  | 
**reboot_power_off** | **bool** | Whether the next reboot will result in a power off.  | [optional] 
**hardware** | [**VirtualHardware**](VirtualHardware.md) |  | 
**vcpu_config** | [**List[VirtualMachineVcpuConfig]**](VirtualMachineVcpuConfig.md) | Vcpu configuration.  The &lt;code&gt;vcpuConfig&lt;/code&gt; array is indexed by vcpu number.  ***Since:*** vSphere API 7.0  | [optional] 
**cpu_allocation** | [**ResourceAllocationInfo**](ResourceAllocationInfo.md) |  | [optional] 
**memory_allocation** | [**ResourceAllocationInfo**](ResourceAllocationInfo.md) |  | [optional] 
**latency_sensitivity** | [**LatencySensitivity**](LatencySensitivity.md) |  | [optional] 
**memory_hot_add_enabled** | **bool** | Whether memory can be added while this virtual machine is running.  ***Since:*** vSphere API 4.0  | [optional] 
**cpu_hot_add_enabled** | **bool** | Whether virtual processors can be added while this virtual machine is running.  ***Since:*** vSphere API 4.0  | [optional] 
**cpu_hot_remove_enabled** | **bool** | Whether virtual processors can be removed while this virtual machine is running.  ***Since:*** vSphere API 4.0  | [optional] 
**hot_plug_memory_limit** | **int** | The maximum amount of memory, in MB, than can be added to a running virtual machine.  This value is determined by the virtual machine and is specified only if *VirtualMachineConfigInfo.memoryHotAddEnabled* is set to true.  ***Since:*** vSphere API 4.0  | [optional] 
**hot_plug_memory_increment_size** | **int** | Memory, in MB that can be added to a running virtual machine must be in increments of this value and needs be a multiple of this value.  This value is determined by the virtual machine and is specified only if *VirtualMachineConfigSpec.memoryHotAddEnabled* has been set to true.  ***Since:*** vSphere API 4.0  | [optional] 
**cpu_affinity** | [**VirtualMachineAffinityInfo**](VirtualMachineAffinityInfo.md) |  | [optional] 
**memory_affinity** | [**VirtualMachineAffinityInfo**](VirtualMachineAffinityInfo.md) |  | [optional] 
**network_shaper** | [**VirtualMachineNetworkShaperInfo**](VirtualMachineNetworkShaperInfo.md) |  | [optional] 
**extra_config** | [**List[OptionValue]**](OptionValue.md) | Additional configuration information for the virtual machine.  | [optional] 
**cpu_feature_mask** | [**List[HostCpuIdInfo]**](HostCpuIdInfo.md) | Specifies CPU feature compatibility masks that override the defaults from the *GuestOsDescriptor* of the virtual machine&#39;s guest OS.  As of vSphere API 6.5 *FeatureMask* is the recommended method for masking virtual machines with hardware version 9 and above (newer). They can be viewed via *featureMask*.  | [optional] 
**datastore_url** | [**List[VirtualMachineConfigInfoDatastoreUrlPair]**](VirtualMachineConfigInfoDatastoreUrlPair.md) | Enumerates the set of datastores that this virtual machine is stored on, as well as the URL identification for each of these.  Changes to datastores do not generate property updates on this property. However, when this property is retrieved it returns the current datastore information.  | [optional] 
**swap_placement** | **str** | Virtual machine swapfile placement policy.  This will be unset if the virtual machine&#39;s *swapPlacementSupported* capability is false. If swapPlacementSupported is true, the default policy is \&quot;inherit\&quot;.  See also *VirtualMachineConfigInfoSwapPlacementType_enum*.  ***Since:*** VI API 2.5  | [optional] 
**boot_options** | [**VirtualMachineBootOptions**](VirtualMachineBootOptions.md) |  | [optional] 
**ft_info** | [**FaultToleranceConfigInfo**](FaultToleranceConfigInfo.md) |  | [optional] 
**rep_config** | [**ReplicationConfigSpec**](ReplicationConfigSpec.md) |  | [optional] 
**v_app_config** | [**VmConfigInfo**](VmConfigInfo.md) |  | [optional] 
**v_asserts_enabled** | **bool** | Indicates whether user-configured virtual asserts will be triggered during virtual machine replay.  ***Since:*** vSphere API 4.0  | [optional] 
**change_tracking_enabled** | **bool** | Indicates whether changed block tracking for this VM&#39;s disks is active.  ***Since:*** vSphere API 4.0  | [optional] 
**firmware** | **str** | Information about firmware type for this Virtual Machine.  Possible values are described in *GuestOsDescriptorFirmwareType_enum* When creating a new VM: \\- If vim.vm.FlagInfo.vbsEnabled is set to &lt;code&gt;true&lt;/code&gt; and this property is set to &lt;code&gt;bios&lt;/code&gt;, error is returned. \\- If this property is unset and vim.vm.FlagInfo.vbsEnabled is set to &lt;code&gt;true&lt;/code&gt;, this property is set to &lt;code&gt;efi&lt;/code&gt;.  ***Since:*** vSphere API 5.0  | [optional] 
**max_mks_connections** | **int** | Indicates the maximum number of active remote display connections that the virtual machine will support.  ***Since:*** vSphere API 5.0  | [optional] 
**guest_auto_lock_enabled** | **bool** | Indicates whether the guest operating system will logout any active sessions whenever there are no remote display connections open to the virtual machine.  ***Since:*** vSphere API 5.0  | [optional] 
**managed_by** | [**ManagedByInfo**](ManagedByInfo.md) |  | [optional] 
**memory_reservation_locked_to_max** | **bool** | If set true, memory resource reservation for this virtual machine will always be equal to the virtual machine&#39;s memory size; increases in memory size will be rejected when a corresponding reservation increase is not possible.  ***Since:*** vSphere API 5.0  | [optional] 
**initial_overhead** | [**VirtualMachineConfigInfoOverheadInfo**](VirtualMachineConfigInfoOverheadInfo.md) |  | [optional] 
**nested_hv_enabled** | **bool** | Indicates whether this VM is configured to use nested hardware-assisted virtualization.  ***Since:*** vSphere API 5.1  | [optional] 
**v_pmc_enabled** | **bool** | Indicates whether this VM have vurtual CPU performance counters enabled.  ***Since:*** vSphere API 5.1  | [optional] 
**scheduled_hardware_upgrade_info** | [**ScheduledHardwareUpgradeInfo**](ScheduledHardwareUpgradeInfo.md) |  | [optional] 
**fork_config_info** | [**VirtualMachineForkConfigInfo**](VirtualMachineForkConfigInfo.md) |  | [optional] 
**v_flash_cache_reservation** | **int** | Deprecated since vSphere 7.0 because vFlash Read Cache end of availability.  Specifies the total vFlash resource reservation for the vFlash caches associated with this VM&#39;s virtual disks, in bytes.  This reservation must be allocated to power on the VM. See *VirtualMachineRuntimeInfo.vFlashCacheAllocation* for allocated reservation when VM is powered on.  ***Since:*** vSphere API 5.5  | [optional] 
**vmx_config_checksum** | **bytearray** | A checksum of vmx config file.  ***Since:*** vSphere API 6.0  | [optional] 
**message_bus_tunnel_enabled** | **bool** | Whether to allow tunneling of clients from the guest VM into the common message bus on the host network.  ***Since:*** vSphere API 6.0  | [optional] 
**vm_storage_object_id** | **str** | Virtual Machine Object Identifier.  With Object-based Storage systems, Virtual Machine home directory is backed by an object. This identifier will be set only if VM directory resided on object-based storage systems.  ***Since:*** vSphere API 6.0  | [optional] 
**swap_storage_object_id** | **str** | Virtual Machine Swap Object Identifier.  With Object-based Storage systems, VM&#39;s Swap is backed by an object. This identifier will be set only if VM swap resided on object-based storage systems.  ***Since:*** vSphere API 6.0  | [optional] 
**key_id** | [**CryptoKeyId**](CryptoKeyId.md) |  | [optional] 
**guest_integrity_info** | [**VirtualMachineGuestIntegrityInfo**](VirtualMachineGuestIntegrityInfo.md) |  | [optional] 
**migrate_encryption** | **str** | An enum describing whether encrypted vMotion is required for this VM.  See *VirtualMachineConfigSpecEncryptedVMotionModes_enum* for allowed values. This defaults to opportunistic for a regular VM, and will be set to required for an encrypted VM.  ***Since:*** vSphere API 6.5  | [optional] 
**sgx_info** | [**VirtualMachineSgxInfo**](VirtualMachineSgxInfo.md) |  | [optional] 
**content_lib_item_info** | [**VirtualMachineContentLibraryItemInfo**](VirtualMachineContentLibraryItemInfo.md) |  | [optional] 
**ft_encryption_mode** | **str** | An enum describing whether encrypted Fault Tolerance is required for this VM.  See *VirtualMachineConfigSpecEncryptedFtModes_enum* for allowed values. \\- This defaults to opportunistic for a regular VM, and will be set to required for an encrypted VM. \\- If this property is unset, the mode of encrypted Fault Tolerance will be set to opportunistic.  ***Since:*** vSphere API 7.0.2.0  | [optional] 
**guest_monitoring_mode_info** | [**VirtualMachineGuestMonitoringModeInfo**](VirtualMachineGuestMonitoringModeInfo.md) |  | [optional] 
**sev_enabled** | **bool** | SEV (Secure Encrypted Virtualization) enabled or not.  SEV is enabled when set to true, and disabled otherwise.  ***Since:*** vSphere API 7.0.1.0  | [optional] 
**numa_info** | [**VirtualMachineVirtualNumaInfo**](VirtualMachineVirtualNumaInfo.md) |  | [optional] 
**pmem_failover_enabled** | **bool** | Property to indicate PMem HA failover configuration.  \\- When set to TRUE, VMs configured to use PMem will be failed over to other hosts by HA, but the data in NVDIMM is not persistent. \\- When set to FALSE, VMs configured to use PMem will not be failed over to other hosts by HA. Property is currently only applicable to VMs with NVDimms and will fail to set True if vPMem disks are present.  ***Since:*** vSphere API 7.0.2.0  | [optional] 
**vmx_stats_collection_enabled** | **bool** | Indicates whether VMXStats Collection is enabled/disabled.  \\- If TRUE, VMXStats is enabled for the VM and a scoreboard file is created to store stats for various VMX components. \\- If FALSE, VMXStats is disabled for the VM and there is no scoreboard file created.  | [optional] 
**vm_op_notification_to_app_enabled** | **bool** | Indicates whether operation notification to applications is enabled/disabled.  \\- When set to TRUE, application running inside the VM will be notified of operations for which they have registered. \\- If unset or FALSE, new applications are not allowed to register for notifications and RPCs will no longer be supported from already registered applications.  ***Since:*** vSphere API 7.0.3.0  | [optional] 
**vm_op_notification_timeout** | **int** | Operation notification timeout in seconds.  \\- Specifies the maximum time the application can take to prepare for the operation after its been notified. This value is used only if *VirtualMachineConfigInfo.vmOpNotificationToAppEnabled* is set to TRUE. \\- If *VirtualMachineConfigInfo.vmOpNotificationTimeout* is unset, then it defaults to cluster/host timeout.  | [optional] 
**device_swap** | [**VirtualMachineVirtualDeviceSwap**](VirtualMachineVirtualDeviceSwap.md) |  | [optional] 
**pmem** | [**VirtualMachineVirtualPMem**](VirtualMachineVirtualPMem.md) |  | [optional] 
**device_groups** | [**VirtualMachineVirtualDeviceGroups**](VirtualMachineVirtualDeviceGroups.md) |  | [optional] 
**fixed_passthru_hot_plug_enabled** | **bool** | Indicates whether support to add and remove fixed passthrough devices when the VM is running is enabled.  When the virtual machine is powered on, this indicates if support for hot adding and removing fixed passthrough devices was enabled prior to power on. Otherwise, it indicates whether it will be enabled when the VM is powered on. NOTE: When setting this to true, the memory reservation should be equal to the guest memory size or the option to reserve all guest memory should be selected. If unset, the current value is left unchanged.  | [optional] 

## Example

```python
from vmware_vi.models.virtual_machine_config_info import VirtualMachineConfigInfo

# TODO update the JSON string below
json = "{}"
# create an instance of VirtualMachineConfigInfo from a JSON string
virtual_machine_config_info_instance = VirtualMachineConfigInfo.from_json(json)
# print the JSON string representation of the object
print VirtualMachineConfigInfo.to_json()

# convert the object into a dict
virtual_machine_config_info_dict = virtual_machine_config_info_instance.to_dict()
# create an instance of VirtualMachineConfigInfo from a dict
virtual_machine_config_info_form_dict = virtual_machine_config_info.from_dict(virtual_machine_config_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


