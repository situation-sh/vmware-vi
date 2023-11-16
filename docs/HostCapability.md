# HostCapability

Specifies the capabilities of the particular host.  This set of capabilities is referenced in other parts of the API specification to indicate under what circumstances an API will throw a *NotSupported* fault. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**recursive_resource_pools_supported** | **bool** |  | 
**cpu_memory_resource_configuration_supported** | **bool** | Flag indicating whether cpu and memory resource configuration is supported.  If this is set to false, *ResourcePool.UpdateConfig*, *ResourcePool.UpdateChildResourceConfiguration* cannot be used for changing the cpu/memory resource configurations.  ***Since:*** VI API 2.5  | 
**reboot_supported** | **bool** | Flag indicating whether rebooting the host is supported.  | 
**shutdown_supported** | **bool** | Flag indicating whether the host can be powered off  | 
**vmotion_supported** | **bool** | Flag indicating whether you can perform VMotion.  | 
**standby_supported** | **bool** | Flag indicating whether you can put the host in a power down state, from which it can be powered up automatically.  ***Since:*** VI API 2.5  | 
**ipmi_supported** | **bool** | Flag indicating whether the host supports IPMI (Intelligent Platform Management Interface).  XXX - Make ipmiSupported optional until there is a compatible hostagent.  ***Since:*** vSphere API 4.0  | [optional] 
**max_supported_vms** | **int** | The maximum number of virtual machines that can exist on this host.  If this capability is not set, the number of virtual machines is unlimited.  | [optional] 
**max_running_vms** | **int** | The maximum number of virtual machines that can be running simultaneously on this host.  If this capability is not set, the number of virtual machines running simultaneously is unlimited.  | [optional] 
**max_supported_vcpus** | **int** | The maximum number of virtual CPUs supported per virtual machine.  If this capability is not set, the number is unlimited.  | [optional] 
**max_registered_vms** | **int** | The maximum number of registered virtual machines supported by the host.  If this limit is exceeded, the management agent will be at risk of running out of system resources. *configIssue* will be posted on *HostSystem* in this case.  If this capability is not set, the number is unknown.  ***Since:*** vSphere API 5.1  | [optional] 
**datastore_principal_supported** | **bool** | Flag indicating whether datastore principal user is supported on the host.  | 
**san_supported** | **bool** | Flag indicating whether access to SAN devices is supported.  | 
**nfs_supported** | **bool** | Is access to NFS devices supported.  | 
**iscsi_supported** | **bool** | Is access to iSCSI devices supported.  | 
**vlan_tagging_supported** | **bool** | Is VLAN Tagging supported.  | 
**nic_teaming_supported** | **bool** | Is NIC teaming supported.  | 
**high_guest_mem_supported** | **bool** | Is high guest memory supported.  | 
**maintenance_mode_supported** | **bool** | Is maintenance mode supported  | 
**suspended_relocate_supported** | **bool** | Indicates whether this host supports relocation of suspended virtual machines.  Must be true on the source and destination hosts for the relocation to work.  | 
**restricted_snapshot_relocate_supported** | **bool** | Indicates whether this host supports relocation of virtual machines with snapshots.  Must be true on the source and destination hosts for the relocation to work. Even if this is true, the following conditions must hold: 1\\) All the the vm&#39;s files are in one directory prior to the relocate. 2\\) All of the vm&#39;s files will be in one directory after the relocate. 3\\) The source and destination hosts are the same product version.  ***Since:*** VI API 2.5  | 
**per_vm_swap_files** | **bool** | Flag indicating whether virtual machine execution on this host involves a swapfile for each virtual machine.  If true, the swapfile placement for a powered-on virtual machine is advertised in its FileLayout by the *swapFile* property.  ***Since:*** VI API 2.5  | 
**local_swap_datastore_supported** | **bool** | Flag indicating whether the host supports selecting a datastore that that may be used to store virtual machine swapfiles.  ***Since:*** VI API 2.5  | 
**unshared_swap_v_motion_supported** | **bool** | Flag indicating whether the host supports participating in a VMotion where the virtual machine swapfile is not visible to the destination.  ***Since:*** VI API 2.5  | 
**background_snapshots_supported** | **bool** | Flag indicating whether background snapshots are supported on this host.  ***Since:*** VI API 2.5  | 
**pre_assigned_pci_unit_numbers_supported** | **bool** | Flag to indicate whether the server returns unit numbers in a pre-assigned range for devices on the PCI bus.  When the server supports this flag, the device unit number namespace is partitioned by device type. Different types of devices will sit in a specific range of unit numbers that may not correspond to physical slots in the pci bus but present a relative ordering of the devices with respect to other devices of the same type. Note that this does not mean that the user can set the relative ordering between device types, but only allows stable orderings between devices of the same type. The unit number will now clearly represent an ordering between devices of the same type. *VirtualDevice.unitNumber* This property is only available for devices on the pci controller.  ***Since:*** VI API 2.5  | 
**screenshot_supported** | **bool** | Indicates whether the screenshot retrival over https is supported for this host&#39;s virtual machines.  If true, a screenshot can be retrieved at the HTTPS relative path _/screen?id&#x3D;&amp;lt;managed object ID of virtual machine or snapshot&amp;gt;_. If any of the optional parameters &#39;top&#39;, &#39;left&#39;, &#39;bottom&#39;, and &#39;right&#39; is specified, the returned image will be cropped from the rectangle with upper left corner (left, top) and bottom right corner (right - 1, bottom - 1). These values default to the top, left, bottom and right edges of the image. The client must use an authenticated session with privilege VirtualMachine.Interact.ConsoleInteract on the requested virtual machine or, in the case of a snapshot, the virtual machine associated with that snapshot.  ***Since:*** VI API 2.5  | 
**scaled_screenshot_supported** | **bool** | Indicates whether scaling is supported for screenshots retrieved over https.  If true, screenshot retrieval supports the additional optional parameters &#39;width&#39; and &#39;height&#39;. After cropping, the returned image will be scaled to these dimensions. If only one of these parameters is specified, default behavior is to return an image roughly proportional to the source image.  ***Since:*** VI API 2.5  | 
**storage_v_motion_supported** | **bool** | Indicates whether the storage of a powered-on virtual machine may be relocated.  ***Since:*** vSphere API 4.0  | 
**vmotion_with_storage_v_motion_supported** | **bool** | Indicates whether the storage of a powered-on virtual machine may be relocated while simultaneously changing the execution host of the virtual machine.  ***Since:*** vSphere API 4.0  | 
**vmotion_across_network_supported** | **bool** | Indicates whether the network of a powered-on virtual machine can be changed while simultaneously changing the execution host of the virtual machine.  ***Since:*** vSphere API 5.5  | [optional] 
**max_num_disks_sv_motion** | **int** | Maximum number of migrating disks allowed of a migrating VM during SVMotion.  If this capability is not set, then the maximum is considered to be 64.  ***Since:*** vSphere API 6.0  | [optional] 
**max_virtual_disk_desc_version_supported** | **int** | Maximum version of vDiskVersion supported by this host.  If this capability is not set, then the maximum is considered to be 6.  | [optional] 
**hbr_nic_selection_supported** | **bool** | Indicates whether a dedicated nic can be selected for vSphere Replication LWD traffic, i.e., from the primary host to the VR server.  ***Since:*** vSphere API 5.1  | 
**vr_nfc_nic_selection_supported** | **bool** | Indicates whether a dedicated nic can be selected for vSphere Replication NFC traffic, i.e., from the VR server to the secondary host.  ***Since:*** vSphere API 6.0  | 
**record_replay_supported** | **bool** | Deprecated as of vSphere API 6.0.  Indicates whether this host supports record and replay  ***Since:*** vSphere API 4.0  | 
**ft_supported** | **bool** | Deprecated as of vSphere API 6.0.  Indicates whether this host supports Fault Tolerance There can be many reasons why a host does not support Fault Tolerance, which includes CPU compatibility, product compatibility as well as other host configuration settings.  For specific reasons, look into *HostCapability.replayCompatibilityIssues* and *HostCapability.ftCompatibilityIssues* In releases after vSphere API 5.0, vSphere Servers might not generate property collector update notifications for this property. To obtain the latest value of the property, you can use PropertyCollector methods RetrievePropertiesEx or WaitForUpdatesEx. If you use the PropertyCollector.WaitForUpdatesEx method, specify an empty string for the version parameter. Since this property is on a DataObject, an update returned by WaitForUpdatesEx may contain values for this property when some other property on the DataObject changes. If this update is a result of a call to WaitForUpdatesEx with a non-empty version parameter, the value for this property may not be current.  ***Since:*** vSphere API 4.0  | 
**replay_unsupported_reason** | **str** | Deprecated as of vSphere API 4.1, use *HostCapability.replayCompatibilityIssues*.  For a host whose CPU doesn&#39;t support replay, indicates the reason for the incompatibility.  *HostReplayUnsupportedReason_enum* represents the set of possible values.  ***Since:*** vSphere API 4.0  | [optional] 
**replay_compatibility_issues** | **List[str]** | Deprecated as of vSphere API 6.0.  For a host which doesn&#39;t support replay, indicates all the reasons for the incompatibility.  *HostReplayUnsupportedReason_enum* lists the set of possible values.  ***Since:*** vSphere API 4.1  | [optional] 
**smp_ft_supported** | **bool** | Indicates whether this host supports smp fault tolerance  ***Since:*** vSphere API 6.0  | 
**ft_compatibility_issues** | **List[str]** | Deprecated as of vSphere API 6.0.  For a host which doesn&#39;t support Fault Tolerance, indicates all the reasons for the incompatibility.  *HostCapabilityFtUnsupportedReason_enum* lists the set of possible values.  ***Since:*** vSphere API 4.1  | [optional] 
**smp_ft_compatibility_issues** | **List[str]** | For a host which doesn&#39;t support smp fault tolerance, indicates all the reasons for the incompatibility.  *HostCapabilityFtUnsupportedReason_enum* lists the set of possible values.  ***Since:*** vSphere API 6.0  | [optional] 
**max_vcpus_per_ft_vm** | **int** | The maximum number of vCPUs allowed for a fault-tolerant virtual machine.  ***Since:*** vSphere API 6.0  | [optional] 
**login_by_ssl_thumbprint_supported** | **bool** | Flag indicating whether this host supports SSL thumbprint authentication  ***Since:*** vSphere API 4.0  | [optional] 
**clone_from_snapshot_supported** | **bool** | Indicates whether or not cloning a virtual machine from a snapshot point is allowed.  This property must be true on the host where the virtual machine is currently residing. This property need not be true on the destination host for the clone.  See also *VirtualMachineCloneSpec.snapshot*.  ***Since:*** vSphere API 4.0  | 
**delta_disk_backings_supported** | **bool** | Flag indicating whether explicitly creating arbirary configurations of delta disk backings is supported.  A delta disk backing is a way to preserve a virtual disk backing at some point in time. A delta disk backing is a file backing which in turn points to the original virtual disk backing (the parent). After a delta disk backing is added, all writes go to the delta disk backing. All reads first try the delta disk backing and then try the parent backing if needed.  If this property is false, then delta disk backings can only be implicitly created through using snapshot operations and two virtual machines cannot safely share a parent disk backing.  If this property is true, then delta disk backings can be explicitly created and managed, and two virtual machines may safely share a parent disk backing.  In the context above, \&quot;safely\&quot; means that performing operations on one of the virtual machines will not affect the operation of the other virtual machine.  See also *VirtualDiskSparseVer1BackingInfo.parent*, *VirtualDiskSparseVer2BackingInfo.parent*, *VirtualDiskFlatVer1BackingInfo.parent*, *VirtualDiskFlatVer2BackingInfo.parent*, *VirtualDiskRawDiskMappingVer1BackingInfo.parent*, *VirtualMachine.PromoteDisks_Task*, *VirtualMachineRelocateSpec.diskMoveType*, *VirtualMachineRelocateSpecDiskLocator.diskMoveType*.  ***Since:*** vSphere API 4.0  | 
**per_vm_network_traffic_shaping_supported** | **bool** | Indicates whether network traffic shaping on a per virtual machine basis is supported.  ***Since:*** vSphere API 4.0  | 
**tpm_supported** | **bool** | Flag indicating whether this host supports the integrity measurement using a TPM device.  ***Since:*** vSphere API 4.0  | 
**tpm_version** | **str** | TPM version if supported by this host.  ***Since:*** vSphere API 6.7  | [optional] 
**txt_enabled** | **bool** | Flag indicating whether Intel TXT is enabled on this host.  ***Since:*** vSphere API 6.7  | [optional] 
**supported_cpu_feature** | [**List[HostCpuIdInfo]**](HostCpuIdInfo.md) | Deprecated as of vSphere API 6.5 use *featureCapability*.  CPU feature set that is supported by the virtualization platform.  This feature set may reflect characteristics of the product capabilities and licensing. For any feature marked &#39;-&#39;, reference the *cpuFeature* array of the host&#39;s HardwareInfo to determine the correct value.  ***Since:*** vSphere API 4.0  | [optional] 
**virtual_exec_usage_supported** | **bool** | Indicates whether the host supports configuring hardware virtualization (HV) support for virtual machines.  ***Since:*** vSphere API 4.0  | 
**storage_iorm_supported** | **bool** | Indicates whether the host supports storage I/O resource management.  ***Since:*** vSphere API 4.1  | 
**vm_direct_path_gen2_supported** | **bool** | Deprecated as of vSphere API 8.0. VMDirectPath Gen 2 is no longer supported and there is no replacement.  Indicates whether the host supports network passthrough using VMDirectPath Gen 2.  Note that this is a general capability for the host and is independent of support by a given physical NIC. If false, the reason(s) for lack of support will be provided in *HostCapability.vmDirectPathGen2UnsupportedReason* and/or in *HostCapability.vmDirectPathGen2UnsupportedReasonExtended*.  See also *PhysicalNic.vmDirectPathGen2Supported*.  ***Since:*** vSphere API 4.1  | [optional] 
**vm_direct_path_gen2_unsupported_reason** | **List[str]** | Deprecated as of vSphere API 8.0. VMDirectPath Gen 2 is no longer supported and there is no replacement.  If *HostCapability.vmDirectPathGen2Supported* is false, this array will be populated with reasons for the lack of support (chosen from *HostCapabilityVmDirectPathGen2UnsupportedReason_enum*).  If there is a reason for the lack of support that cannot be described by the available constants, *HostCapability.vmDirectPathGen2UnsupportedReasonExtended* will be populated with an additional explanation provided by the platform.  Note that this list of reasons is not guaranteed to be exhaustive.  If the reason \&quot;hostNptIncompatibleProduct\&quot; is provided, then that will be the only provided reason, as the host software is incapable of providing additional information.  ***Since:*** vSphere API 4.1  | [optional] 
**vm_direct_path_gen2_unsupported_reason_extended** | **str** | Deprecated as of vSphere API 8.0. VMDirectPath Gen 2 is no longer supported and there is no replacement.  If *HostCapability.vmDirectPathGen2Supported* is false, this property may contain an explanation provided by the platform, beyond the reasons (if any) enumerated in *HostCapability.vmDirectPathGen2UnsupportedReason*.  ***Since:*** vSphere API 4.1  | [optional] 
**supported_vmfs_major_version** | **List[int]** | List of VMFS major versions supported by the host.  ***Since:*** vSphere API 5.0  | [optional] 
**v_storage_capable** | **bool** | Indicates whether the host supports vStorage Hardware acceleration.  ***Since:*** vSphere API 4.1  | 
**snapshot_relayout_supported** | **bool** | Indicates whether this host supports unrestricted relocation of virtual machines with snapshots.  Only needs to be true on the destination host for the unrestricted relocation to work. The full snapshot relocation does not restrict the layout of snapshot files or disks of the virtual machine, nor its power state. If the virtual machine is powered on, a storage vmotion will be performed to relocate its snapshots and disks.  ***Since:*** vSphere API 5.0  | 
**firewall_ip_rules_supported** | **bool** | Indicates whether this host supports ip address based restrictions in the firewall configuration.  ***Since:*** vSphere API 5.0  | [optional] 
**service_package_info_supported** | **bool** | Indicates whether this host supports package information in service configuration.  ***Since:*** vSphere API 5.0  | [optional] 
**max_host_running_vms** | **int** | The maximum number of virtual machines that can be run on the host.  An unset value indicates that the value could not be obtained. In contrast to *HostCapability.maxRunningVMs*, this value is the minimum of (i) the maximum number supported by the hardware and (ii) the maximum number permitted by the host license.  ***Since:*** vSphere API 5.0  | [optional] 
**max_host_supported_vcpus** | **int** | The maximum number of virtual CPUs that can be run on the host.  An unset value indicates that the value could not be obtained. In contrast to *HostCapability.maxSupportedVcpus*, this value is the minimum of (i) the maximum number supported by the hardware and (ii) the maximum number permitted by the host license.  ***Since:*** vSphere API 5.0  | [optional] 
**vmfs_datastore_mount_capable** | **bool** | Indicates whether the host is capable of mounting/unmounting VMFS datastores.  ***Since:*** vSphere API 5.0  | 
**eight_plus_host_vmfs_shared_access_supported** | **bool** | Indicates whether the host is capable of accessing a VMFS disk when there are eight or more hosts accessing the disk already.  ***Since:*** vSphere API 5.1  | 
**nested_hv_supported** | **bool** | Indicates whether the host supports nested hardware-assisted virtualization.  ***Since:*** vSphere API 5.1  | 
**v_pmc_supported** | **bool** | Indicates whether the host supports virtual CPU performance counters.  ***Since:*** vSphere API 5.1  | 
**inter_vm_communication_through_vmci_supported** | **bool** | Indicates whether the host supports VMCI for communication between virtual machines.  ***Since:*** vSphere API 5.1  | 
**scheduled_hardware_upgrade_supported** | **bool** | Indicates whether the host supports scheduled hardware upgrades.  See also *VirtualMachineConfigInfo.scheduledHardwareUpgradeInfo*.  ***Since:*** vSphere API 5.1  | [optional] 
**feature_capabilities_supported** | **bool** | Indicated whether the host supports feature capabilities for EVC mode.  ***Since:*** vSphere API 5.1  | 
**latency_sensitivity_supported** | **bool** | Indicates whether the host supports latency sensitivity for the virtual machines.  ***Since:*** vSphere API 5.1  | 
**storage_policy_supported** | **bool** | Indicates that host supports Object-based Storage System and Storage-Profile based disk provisioning.  ***Since:*** vSphere API 5.5  | [optional] 
**accel3d_supported** | **bool** | Indicates if 3D hardware acceleration for virtual machines is supported.  ***Since:*** vSphere API 5.1  | 
**reliable_memory_aware** | **bool** | Indicates that this host uses a reliable memory aware allocation policy.  ***Since:*** vSphere API 5.5  | [optional] 
**multiple_network_stack_instance_supported** | **bool** | Indicates whether the host supports Multiple Instance TCP/IP stack  ***Since:*** vSphere API 5.5  | [optional] 
**message_bus_proxy_supported** | **bool** | Indicates whether the message bus proxy is supported  ***Since:*** vSphere API 6.0  | [optional] 
**vsan_supported** | **bool** | Indicates whether the host supports VSAN functionality.  See also *HostVsanSystem*.  ***Since:*** vSphere API 5.5  | [optional] 
**v_flash_supported** | **bool** | Indicates whether the host supports vFlash.  ***Since:*** vSphere API 5.5  | [optional] 
**host_access_manager_supported** | **bool** | Whether this host supports HostAccessManager for controlling direct access to the host and for better lockdown mode management.  ***Since:*** vSphere API 6.0  | [optional] 
**provisioning_nic_selection_supported** | **bool** | Indicates whether a dedicated nic can be selected for vSphere Provisioning NFC traffic.  ***Since:*** vSphere API 6.0  | 
**nfs41_supported** | **bool** | Whether this host supports NFS41 file systems.  ***Since:*** vSphere API 6.0  | [optional] 
**nfs41_krb5i_supported** | **bool** | Whether this host support NFS41 Kerberos 5\\* security type.  ***Since:*** vSphere API 6.5  | [optional] 
**turn_disk_locator_led_supported** | **bool** | Indicates whether turning on/off local disk LED is supported on the host.  See also *HostStorageSystem.TurnDiskLocatorLedOn_Task*, *HostStorageSystem.TurnDiskLocatorLedOff_Task*.  ***Since:*** vSphere API 6.0  | [optional] 
**virtual_volume_datastore_supported** | **bool** | Indicates whether this host supports VirtualVolume based Datastore.  ***Since:*** vSphere API 6.0  | [optional] 
**mark_as_ssd_supported** | **bool** | Indicates whether mark disk as SSD or Non-SSD is supported on the host.  See also *HostStorageSystem.MarkAsSsd_Task*, *HostStorageSystem.MarkAsNonSsd_Task*.  ***Since:*** vSphere API 6.0  | [optional] 
**mark_as_local_supported** | **bool** | Indicates whether mark disk as local or remote is supported on the host.  See also *HostStorageSystem.MarkAsLocal_Task*, *HostStorageSystem.MarkAsNonLocal_Task*.  ***Since:*** vSphere API 6.0  | [optional] 
**smart_card_authentication_supported** | **bool** | Indicates whether this host supports local two-factor user authentication using smart cards.  See also *HostActiveDirectoryAuthentication.EnableSmartCardAuthentication*.  ***Since:*** vSphere API 6.0  | [optional] 
**p_mem_supported** | **bool** | Indicates whether this host supports persistent memory.  If value is not specified, it should be considered as not supported.  ***Since:*** vSphere API 6.7  | [optional] 
**p_mem_snapshot_supported** | **bool** | Indicates whether this host supports snapshots for VMs with virtual devices backed by persistent memory.  If value is not specified, it should be considered as not supported.  ***Since:*** vSphere API 6.7  | [optional] 
**crypto_supported** | **bool** | Flag indicating whether Cryptographer feature is supported.  ***Since:*** vSphere API 6.5  | [optional] 
**one_k_volume_apis_supported** | **bool** | Indicates whether this host supports granular datastore cache update.  If value is not specified, it should be considered as not supported.  ***Since:*** vSphere API 6.5  | [optional] 
**gateway_on_nic_supported** | **bool** | Flag indicating whether default gateway can be configured on a vmkernel nic.  ***Since:*** vSphere API 6.5  | [optional] 
**upit_supported** | **bool** | Deprecated as of vSphere API 8.0, and there is no replacement for it.  Indicate whether this host supports UPIT  ***Since:*** vSphere API 6.5  | [optional] 
**cpu_hw_mmu_supported** | **bool** | Indicates whether this host supports hardware-based MMU virtualization.  ***Since:*** vSphere API 6.5  | [optional] 
**encrypted_v_motion_supported** | **bool** | Indicates whether this host supports encrypted vMotion.  ***Since:*** vSphere API 6.5  | [optional] 
**encryption_change_on_add_remove_supported** | **bool** | Indicates whether this host supports changing the encryption state of a virtual disk when the disk is being added or removed from a virtual machine configuration.  ***Since:*** vSphere API 6.5  | [optional] 
**encryption_hot_operation_supported** | **bool** | Indicates whether this host supports changing the encryption state of a virtual machine, or virtual disk, while the virtual machine is powered on.  ***Since:*** vSphere API 6.5  | [optional] 
**encryption_with_snapshots_supported** | **bool** | Indicates whether this host supports changing the encryption state state of a virtual machine, or virtual disk, while the virtual machine has snapshots present.  ***Since:*** vSphere API 6.5  | [optional] 
**encryption_fault_tolerance_supported** | **bool** | Indicates whether this host supports enabling Fault Tolerance on encrypted virtual machines.  ***Since:*** vSphere API 6.5  | [optional] 
**encryption_memory_save_supported** | **bool** | Indicates whether this host supports suspending, or creating with-memory snapshots, encrypted virtual machines.  ***Since:*** vSphere API 6.5  | [optional] 
**encryption_rdm_supported** | **bool** | Indicates whether this host supports encrypting RDM backed virtual disks.  ***Since:*** vSphere API 6.5  | [optional] 
**encryption_v_flash_supported** | **bool** | Indicates whether this host supports encrypting virtual disks with vFlash cache enabled.  ***Since:*** vSphere API 6.5  | [optional] 
**encryption_cbrc_supported** | **bool** | Indicates whether this host supports encrypting virtual disks with Content Based Read Cache (digest disks) enabled.  ***Since:*** vSphere API 6.5  | [optional] 
**encryption_hbr_supported** | **bool** | Indicates whether this host supports encrypting virtual disks with Host Based Replication enabled.  ***Since:*** vSphere API 6.5  | [optional] 
**ft_efi_supported** | **bool** | Indicates whether this host supports Fault Tolerance VMs that have specified UEFI firmware.  ***Since:*** vSphere API 6.7  | [optional] 
**unmap_method_supported** | **str** | Indicates which kind of VMFS unmap method is supported.  See *HostCapabilityUnmapMethodSupported_enum*  ***Since:*** vSphere API 6.7  | [optional] 
**max_mem_mb_per_ft_vm** | **int** | Indicates maximum memory allowed for Fault Tolerance virtual machine.  ***Since:*** vSphere API 6.7  | [optional] 
**virtual_mmu_usage_ignored** | **bool** | Indicates that *VirtualMachineFlagInfo.virtualMmuUsage* is ignored by the host, always operating as if \&quot;on\&quot; was selected.  ***Since:*** vSphere API 6.7  | [optional] 
**virtual_exec_usage_ignored** | **bool** | Indicates that *VirtualMachineFlagInfo.virtualExecUsage* is ignored by the host, always operating as if \&quot;hvOn\&quot; was selected.  ***Since:*** vSphere API 6.7  | [optional] 
**vm_create_date_supported** | **bool** | Indicates that createDate feature is supported by the host.  ***Since:*** vSphere API 6.7  | [optional] 
**vmfs3_eol_supported** | **bool** | Indicates whether this host supports VMFS-3 EOL.  If value is not specified, it should be considered as not supported.  ***Since:*** vSphere API 6.7  | [optional] 
**ft_vmcp_supported** | **bool** | Indicates whether this host supports VMCP for Fault Tolerance VMs.  ***Since:*** vSphere API 6.7  | [optional] 
**quick_boot_supported** | **bool** | Indicates whether this host supports the LoadESX feature which allows faster reboots.  See also *HostLoadEsxManager.QueryLoadEsxSupported*.  ***Since:*** vSphere API 6.7.1  | [optional] 
**encrypted_ft_supported** | **bool** | Indicates whether this host supports encrypted Fault Tolerance.  ***Since:*** vSphere API 7.0.2.0  | [optional] 
**assignable_hardware_supported** | **bool** | Indicates whether this host supports Assignable Hardware.  ***Since:*** vSphere API 7.0  | [optional] 
**suspend_to_memory_supported** | **bool** | Indicates whether this host supports suspending virtual machines to memory.  ***Since:*** vSphere API 7.0.2.0  | [optional] 
**use_feature_reqs_for_old_hwv** | **bool** | Indicates whether this host uses vmFeatures for compatibility checking of old (&amp;leq;8) virtual hardware version VMs.  ***Since:*** vSphere API 6.8.7  | [optional] 
**mark_perennially_reserved_supported** | **bool** | Indicates whether this host supports marking specified LUN as perennially reserved.  ***Since:*** vSphere API 6.7.2  | [optional] 
**hpp_psp_supported** | **bool** | Indicates whether this host supports HPP path selection policy settings.  ***Since:*** vSphere API 7.0  | [optional] 
**device_rebind_without_reboot_supported** | **bool** | Indicates whether device rebind without reboot is supported.  This is the capability which enables PCI passthrough and SR-IOV configuration without reboot.  ***Since:*** vSphere API 7.0  | [optional] 
**storage_policy_change_supported** | **bool** | Indicates whether this host supports storage policy change.  ***Since:*** vSphere API 7.0  | [optional] 
**precision_time_protocol_supported** | **bool** | Indicates whether this host supports date time synchronization over Precision Time Protocol (PTP).  ***Since:*** vSphere API 7.0  | [optional] 
**remote_device_v_motion_supported** | **bool** | Indicates whether vMotion of a VM with remote devices attached is supported.  This applies to CD-ROM and floppy devices backed by a remote client.  ***Since:*** vSphere API 7.0  | [optional] 
**max_supported_vm_memory** | **int** | The maximum amount of virtual memory supported per virtual machine.  If this capability is not set, the size is limited by hardware version of the virtual machine only.  ***Since:*** vSphere API 7.0  | [optional] 
**ah_device_hints_supported** | **bool** | Indicates if the host supports Assignable Hardware device hints.  ***Since:*** vSphere API 7.0.2.0  | [optional] 
**nvme_over_tcp_supported** | **bool** | Indicates if access to NVMe over TCP devices is supported.  ***Since:*** vSphere API 7.0.3.0  | [optional] 
**nvme_storage_fabric_services_supported** | **bool** | Indicates whether NVMe Storage Fabrics Services (StFS) are supported.  ***Since:*** vSphere API 7.0.3.0  | [optional] 
**assign_hw_pci_config_supported** | **bool** | Indicates if setting hardwareLabel using PciPassThrough is supported.  ***Since:*** vSphere API 7.0.2.0  | [optional] 
**time_config_supported** | **bool** | Indicates whether advanced timekeeping apis are supported  ***Since:*** vSphere API 7.0.3.0  | [optional] 
**nvme_batch_operations_supported** | **bool** | Indicates whether batch NVMe controller connection/disconnection is supported.  See *HostStorageSystem.ConnectNvmeControllerEx_Task* and *HostStorageSystem.DisconnectNvmeControllerEx_Task*.  ***Since:*** vSphere API 7.0.3.0  | [optional] 
**p_mem_failover_supported** | **bool** | Indicates whether this host supports failover for VMs with virtual devices backed by persistent memory.  If value is not specified, it should be considered as not supported.  ***Since:*** vSphere API 7.0.2.0  | [optional] 
**host_config_encryption_supported** | **bool** | Indicates whether this host supports host configuration encryption.  ***Since:*** vSphere API 7.0.2.0  | [optional] 
**max_supported_simultaneous_threads** | **int** | Max supported number of SMT (Simultaneous multithreading) threads.  If value is not specified, it should be considered as not supported.  | [optional] 
**ptp_config_supported** | **bool** | Indicates whether this host supports PTP (Precision Time Protocol) service configuration.  See *HostPtpConfig*. If value is not specified, it should be considered as not supported.  ***Since:*** vSphere API 7.0.3.0  | [optional] 
**max_supported_ptp_ports** | **int** | Number of PTP (Precision Time Protocol) ports supported by this host (See *HostPtpConfig*).  If this capability is not set, number of PTP ports in the host is 0.  ***Since:*** vSphere API 7.0.3.0  | [optional] 
**sgx_registration_supported** | **bool** | Indicates whether this host supports SGX registration.  | [optional] 
**p_mem_independent_snapshot_supported** | **bool** | Indicates whether this host supports snapshots of VMs configured with independent vNVDIMMs.  If value is not specified, it should be considered as not supported. This support does not depend on *HostCapability.pMemSnapshotSupported*.  ***Since:*** vSphere API 7.0.3.0  | [optional] 
**iommu_sl_dirty_capable** | **bool** | Indicates whether this host&#39;s IOMMUs are capable of tracking pages written by device DMAs using dirty bits in the second-level page tables.  If this value is not specified, it should be considered as not capable.  | [optional] 
**vmknic_binding_supported** | **bool** | Indicates whether vmknic binding is supported over this host.  | [optional] 
**ultralow_fixed_unmap_supported** | **bool** | Indicates whether ultralow fixed unmap bandwidth is supported on this host.  | [optional] 
**nvme_vvol_supported** | **bool** | Indicates whether mounting of NVMe vvol is supported on this host.  | [optional] 
**fpt_hotplug_supported** | **bool** | Indicates whether FPT Hotplug is supported on this host.  | [optional] 
**mconnect_supported** | **bool** | Indicates whether MCONNECT is supported on this host.  | [optional] 

## Example

```python
from vmware_vi.models.host_capability import HostCapability

# TODO update the JSON string below
json = "{}"
# create an instance of HostCapability from a JSON string
host_capability_instance = HostCapability.from_json(json)
# print the JSON string representation of the object
print HostCapability.to_json()

# convert the object into a dict
host_capability_dict = host_capability_instance.to_dict()
# create an instance of HostCapability from a dict
host_capability_form_dict = host_capability.from_dict(host_capability_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


