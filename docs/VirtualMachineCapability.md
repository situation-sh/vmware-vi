# VirtualMachineCapability

This data object type contains information about the operation/capabilities of a virtual machine 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**snapshot_operations_supported** | **bool** | Indicates whether or not a virtual machine supports snapshot operations.  | 
**multiple_snapshots_supported** | **bool** | Indicates whether or not a virtual machine supports multiple snapshots.  This value is not set when the virtual machine is unavailable, for instance, when it is being created or deleted.  | 
**snapshot_config_supported** | **bool** | Indicates whether or not a virtual machine supports snapshot config.  | 
**powered_off_snapshots_supported** | **bool** | Indicates whether or not a virtual machine supports snapshot operations in poweredOff state.  This flag doesn&#39;t affect vim.VirtualMachine.GetSnapshot, which is always supported.  | 
**memory_snapshots_supported** | **bool** | Indicates whether or not a virtual machine supports memory snapshots.  | 
**revert_to_snapshot_supported** | **bool** | Indicates whether or not a virtual machine supports reverting to a snapshot.  | 
**quiesced_snapshots_supported** | **bool** | Indicates whether or not a virtual machine supports quiesced snapshots.  | 
**disable_snapshots_supported** | **bool** | Deprecated as of vSphere API 4.0. The value returned from the server is always false.  Indicates whether or not snapshots can be disabled.  ***Since:*** VI API 2.5  | 
**lock_snapshots_supported** | **bool** | Indicates whether or not the snapshot tree can be locked.  ***Since:*** VI API 2.5  | 
**console_preferences_supported** | **bool** | Indicates whether console preferences can be set for this virtual machine.  | 
**cpu_feature_mask_supported** | **bool** | Indicates whether CPU feature requirements masks can be set for this virtual machine.  Masking for hardware version 9 and newer virtual machines is controlled by *VirtualMachineCapability.featureRequirementSupported*.  | 
**s1_acpi_management_supported** | **bool** | Indicates whether or not a virtual machine supports ACPI S1 settings management.  | 
**setting_screen_resolution_supported** | **bool** | Indicates whether of not this virtual machine supports setting the screen resolution of the console window.  This capability depends on the guest operating system configured for this virtual machine.  | 
**tools_auto_update_supported** | **bool** | Supports tools auto-update.  | 
**vm_npiv_wwn_supported** | **bool** | Supports virtual machine NPIV WWN.  ***Since:*** VI API 2.5  | 
**npiv_wwn_on_non_rdm_vm_supported** | **bool** | Supports assigning NPIV WWN to virtual machines that don&#39;t have RDM disks.  ***Since:*** VI API 2.5  | 
**vm_npiv_wwn_disable_supported** | **bool** | Indicates whether the NPIV disabling operation is supported the virtual machine.  ***Since:*** vSphere API 4.0  | 
**vm_npiv_wwn_update_supported** | **bool** | Indicates whether the update of NPIV WWNs are supported on the virtual machine.  ***Since:*** vSphere API 4.0  | 
**swap_placement_supported** | **bool** | Flag indicating whether the virtual machine has a configurable *swapfile placement policy*.  ***Since:*** VI API 2.5  | 
**tools_sync_time_supported** | **bool** | Indicates whether asking tools to sync time with the host is supported.  ***Since:*** VI API 2.5  | 
**virtual_mmu_usage_supported** | **bool** | Indicates whether or not the use of nested page table hardware support can be explicitly set.  ***Since:*** VI API 2.5  | 
**disk_shares_supported** | **bool** | Indicates whether resource settings for disks can be applied to this virtual machine.  ***Since:*** VI API 2.5  | 
**boot_options_supported** | **bool** | Indicates whether boot options can be configured for this virtual machine.  ***Since:*** VI API 2.5  | 
**boot_retry_options_supported** | **bool** | Indicates whether automatic boot retry can be configured for this virtual machine.  ***Since:*** vSphere API 4.1  | 
**setting_video_ram_size_supported** | **bool** | Flag indicating whether the video ram size of this virtual machine can be configured.  ***Since:*** VI API 2.5  | 
**setting_display_topology_supported** | **bool** | Indicates whether of not this virtual machine supports setting the display topology of the console window.  This capability depends on the guest operating system configured for this virtual machine.  ***Since:*** vSphere API 4.0  | 
**record_replay_supported** | **bool** | Deprecated as of vSphere API 6.0.  Indicates whether record and replay functionality is supported on this virtual machine.  ***Since:*** vSphere API 4.0  | 
**change_tracking_supported** | **bool** | Indicates that change tracking is supported for virtual disks of this virtual machine.  However, even if change tracking is supported, it might not be available for all disks of the virtual machine. For example, passthru raw disk mappings or disks backed by any Ver1BackingInfo cannot be tracked.  ***Since:*** vSphere API 4.0  | 
**multiple_cores_per_socket_supported** | **bool** | Indicates whether multiple virtual cores per socket is supported on this VM.  ***Since:*** vSphere API 5.0  | 
**host_based_replication_supported** | **bool** | Indicates that host based replication is supported on this virtual machine.  However, even if host based replication is supported, it might not be available for all disk types. For example, passthru raw disk mappings can not be replicated.  ***Since:*** vSphere API 5.0  | 
**guest_auto_lock_supported** | **bool** | Indicates whether features like guest OS auto-lock and MKS connection controls are supported for this virtual machine.  ***Since:*** vSphere API 5.0  | 
**memory_reservation_lock_supported** | **bool** | Indicates whether *memoryReservationLockedToMax* may be set to true for this virtual machine.  ***Since:*** vSphere API 5.0  | 
**feature_requirement_supported** | **bool** | Indicates whether featureRequirement feature is supported.  ***Since:*** vSphere API 5.1  | 
**powered_on_monitor_type_change_supported** | **bool** | Indicates whether a monitor type change is supported while this virtual machine is in the poweredOn state.  ***Since:*** vSphere API 5.1  | 
**se_sparse_disk_supported** | **bool** | Indicates whether this virtual machine supports the Flex-SE (space-efficient, sparse) format for virtual disks.  ***Since:*** vSphere API 5.1  | 
**nested_hv_supported** | **bool** | Indicates whether this virtual machine supports nested hardware-assisted virtualization.  ***Since:*** vSphere API 5.1  | 
**v_pmc_supported** | **bool** | Indicates whether this virtual machine supports virtualized CPU performance counters.  ***Since:*** vSphere API 5.1  | 
**secure_boot_supported** | **bool** | Indicates whether secureBoot is supported for this virtual machine.  ***Since:*** vSphere API 6.5  | [optional] 
**per_vm_evc_supported** | **bool** | Indicates whether this virtual machine supports Per-VM EVC mode.  ***Since:*** vSphere API 6.7  | [optional] 
**virtual_mmu_usage_ignored** | **bool** | Indicates that *VirtualMachineFlagInfo.virtualMmuUsage* is ignored by this virtual machine, always operating as if \&quot;on\&quot; was selected.  ***Since:*** vSphere API 6.7  | [optional] 
**virtual_exec_usage_ignored** | **bool** | Indicates that *VirtualMachineFlagInfo.virtualExecUsage* is ignored by this virtual machine, always operating as if \&quot;hvOn\&quot; was selected.  ***Since:*** vSphere API 6.7  | [optional] 
**disk_only_snapshot_on_suspended_vm_supported** | **bool** | Indicates whether this virtual machine supports creating disk-only snapshots in suspended state.  If this capability is not set, the snapshot of a virtual machine in suspended state will always include memory.  ***Since:*** vSphere API 6.7  | [optional] 
**suspend_to_memory_supported** | **bool** | Indicates whether this virtual machine supports suspending to memory.  ***Since:*** vSphere API 7.0.2.0  | [optional] 
**tools_sync_time_allow_supported** | **bool** | Indicates support for allowing or disallowing all tools time sync with host.  ***Since:*** vSphere API 7.0.1.0  | [optional] 
**sev_supported** | **bool** | Indicates support for AMD-SEV (Secure Encrypted Virtualization).  SEV is supported when set to true, and unsupported otherwise.  ***Since:*** vSphere API 7.0.1.0  | [optional] 
**pmem_failover_supported** | **bool** | Indicates support for failover to a dfferent host on VM&#39;s with pmem.  Failover is supported when set to true, and unsupported otherwise.  ***Since:*** vSphere API 7.0.2.0  | [optional] 
**require_sgx_attestation_supported** | **bool** | Whether the VM supports requiring SGX remote attestation.  | [optional] 
**change_mode_disks_supported** | **bool** | Indicates support for change mode on virtual disks  | [optional] 
**vendor_device_group_supported** | **bool** | Indicates support for Vendor Device Groups  | [optional] 

## Example

```python
from vmware_vi.models.virtual_machine_capability import VirtualMachineCapability

# TODO update the JSON string below
json = "{}"
# create an instance of VirtualMachineCapability from a JSON string
virtual_machine_capability_instance = VirtualMachineCapability.from_json(json)
# print the JSON string representation of the object
print VirtualMachineCapability.to_json()

# convert the object into a dict
virtual_machine_capability_dict = virtual_machine_capability_instance.to_dict()
# create an instance of VirtualMachineCapability from a dict
virtual_machine_capability_form_dict = virtual_machine_capability.from_dict(virtual_machine_capability_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


