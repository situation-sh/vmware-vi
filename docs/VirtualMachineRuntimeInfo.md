# VirtualMachineRuntimeInfo

The RuntimeInfo data object type provides information about the execution state and history of a virtual machine. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**device** | [**List[VirtualMachineDeviceRuntimeInfo]**](VirtualMachineDeviceRuntimeInfo.md) | Per-device runtime info.  This array will be empty if the host software does not provide runtime info for any of the device types currently in use by the virtual machine. In releases after vSphere API 5.0, vSphere Servers might not generate property collector update notifications for this property. To obtain the latest value of the property, you can use PropertyCollector methods RetrievePropertiesEx or WaitForUpdatesEx. If you use the PropertyCollector.WaitForUpdatesEx method, specify an empty string for the version parameter. Since this property is on a DataObject, an update returned by WaitForUpdatesEx may contain values for this property when some other property on the DataObject changes. If this update is a result of a call to WaitForUpdatesEx with a non-empty version parameter, the value for this property may not be current.  ***Since:*** vSphere API 4.1  | [optional] 
**host** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | [optional] 
**connection_state** | [**VirtualMachineConnectionStateEnum**](VirtualMachineConnectionStateEnum.md) |  | 
**power_state** | [**VirtualMachinePowerStateEnum**](VirtualMachinePowerStateEnum.md) |  | 
**vm_failover_in_progress** | **bool** | Represents if the vm is currently being failed over by FDM  ***Since:*** vSphere API 7.0.2.0  | [optional] 
**fault_tolerance_state** | [**VirtualMachineFaultToleranceStateEnum**](VirtualMachineFaultToleranceStateEnum.md) |  | 
**das_vm_protection** | [**VirtualMachineRuntimeInfoDasProtectionState**](VirtualMachineRuntimeInfoDasProtectionState.md) |  | [optional] 
**tools_installer_mounted** | **bool** | Flag to indicate whether or not the VMware Tools installer is mounted as a CD-ROM.  | 
**suspend_time** | **datetime** | The timestamp when the virtual machine was most recently suspended.  This property is updated every time the virtual machine is suspended.  | [optional] 
**boot_time** | **datetime** | The timestamp when the virtual machine was most recently powered on.  This property is updated when the virtual machine is powered on from the poweredOff state, and is cleared when the virtual machine is powered off. This property is not updated when a virtual machine is resumed from a suspended state.  | [optional] 
**suspend_interval** | **int** | The total time the virtual machine has been suspended since it was initially powered on.  This time excludes the current period, if the virtual machine is currently suspended. This property is updated when the virtual machine resumes, and is reset to zero when the virtual machine is powered off.  | [optional] 
**question** | [**VirtualMachineQuestionInfo**](VirtualMachineQuestionInfo.md) |  | [optional] 
**memory_overhead** | **int** | Deprecated as of vSphere API 4.1, use the *PerformanceManager* memory overhead counter to get this value.  The amount of memory resource (in bytes) that will be used by the virtual machine above its guest memory requirements.  This value is set if and only if the virtual machine is registered on a host that supports memory resource allocation features.  For powered off VMs, this is the minimum overhead required to power on the VM on the registered host.  For powered on VMs, this is the current overhead reservation, a value which is almost always larger than the minimum overhead, and which grows with time.  See also *HostSystem.QueryMemoryOverheadEx*.  | [optional] 
**max_cpu_usage** | **int** | Current upper-bound on CPU usage.  The upper-bound is based on the host the virtual machine is current running on, as well as limits configured on the virtual machine itself or any parent resource pool. Valid while the virtual machine is running. In releases after vSphere API 5.0, vSphere Servers might not generate property collector update notifications for this property. To obtain the latest value of the property, you can use PropertyCollector methods RetrievePropertiesEx or WaitForUpdatesEx. If you use the PropertyCollector.WaitForUpdatesEx method, specify an empty string for the version parameter. Since this property is on a DataObject, an update returned by WaitForUpdatesEx may contain values for this property when some other property on the DataObject changes. If this update is a result of a call to WaitForUpdatesEx with a non-empty version parameter, the value for this property may not be current.  | [optional] 
**max_memory_usage** | **int** | Current upper-bound on memory usage.  The upper-bound is based on memory configuration of the virtual machine, as well as limits configured on the virtual machine itself or any parent resource pool. Valid while the virtual machine is running. In releases after vSphere API 5.0, vSphere Servers might not generate property collector update notifications for this property. To obtain the latest value of the property, you can use PropertyCollector methods RetrievePropertiesEx or WaitForUpdatesEx. If you use the PropertyCollector.WaitForUpdatesEx method, specify an empty string for the version parameter. Since this property is on a DataObject, an update returned by WaitForUpdatesEx may contain values for this property when some other property on the DataObject changes. If this update is a result of a call to WaitForUpdatesEx with a non-empty version parameter, the value for this property may not be current.  | [optional] 
**num_mks_connections** | **int** | Number of active MKS connections to this virtual machine.  | 
**record_replay_state** | [**VirtualMachineRecordReplayStateEnum**](VirtualMachineRecordReplayStateEnum.md) |  | 
**clean_power_off** | **bool** | For a powered off virtual machine, indicates whether the virtual machine&#39;s last shutdown was an orderly power off or not.  Unset if the virtual machine is running or suspended.  ***Since:*** vSphere API 4.0  | [optional] 
**need_secondary_reason** | **str** | If set, indicates the reason the virtual machine needs a secondary.  ***Since:*** vSphere API 4.0  | [optional] 
**online_standby** | **bool** | This property indicates whether the guest has gone into one of the s1, s2 or s3 standby modes, false indicates the guest is awake.  ***Since:*** vSphere API 5.1  | 
**min_required_evc_mode_key** | **str** | For a powered-on or suspended virtual machine in a cluster with Enhanced VMotion Compatibility (EVC) enabled, this identifies the least-featured EVC mode (among those for the appropriate CPU vendor) that could admit the virtual machine.  See *EVCMode*. Until vSphere 6.5, this property will be unset if the virtual machine is powered off or is not in an EVC cluster.  This property may be used as a general indicator of the CPU feature baseline currently in use by the virtual machine. However, the virtual machine may be suppressing some of the features present in the CPU feature baseline of the indicated mode, either explicitly (in the virtual machine&#39;s configured *cpuFeatureMask*) or implicitly (in the default masks for the *GuestOsDescriptor* appropriate for the virtual machine&#39;s configured guest OS).  ***Since:*** vSphere API 4.1  | [optional] 
**consolidation_needed** | **bool** | Whether any disk of the virtual machine requires consolidation.  This can happen for example when a snapshot is deleted but its associated disk is not committed back to the base disk. Use *VirtualMachine.ConsolidateVMDisks_Task* to consolidate if needed.  ***Since:*** vSphere API 5.0  | 
**offline_feature_requirement** | [**List[VirtualMachineFeatureRequirement]**](VirtualMachineFeatureRequirement.md) | These requirements must have equivalent host capabilities *HostConfigInfo.featureCapability* in order to power on.  ***Since:*** vSphere API 5.1  | [optional] 
**feature_requirement** | [**List[VirtualMachineFeatureRequirement]**](VirtualMachineFeatureRequirement.md) | These requirements must have equivalent host capabilities *HostConfigInfo.featureCapability* in order to power on, resume, or migrate to the host.  ***Since:*** vSphere API 5.1  | [optional] 
**feature_mask** | [**List[HostFeatureMask]**](HostFeatureMask.md) | The masks applied to an individual virtual machine as a result of its configuration.  ***Since:*** vSphere API 5.1  | [optional] 
**v_flash_cache_allocation** | **int** | Deprecated since vSphere 7.0 because vFlash Read Cache end of availability.  Specifies the total allocated vFlash resource for the vFlash caches associated with VM&#39;s VMDKs when VM is powered on, in bytes.  ***Since:*** vSphere API 5.5  | [optional] 
**paused** | **bool** | Whether the virtual machine is paused, or not.  ***Since:*** vSphere API 6.0  | [optional] 
**snapshot_in_background** | **bool** | Whether a snapshot operation is in progress in the background, or not.  ***Since:*** vSphere API 6.0  | [optional] 
**quiesced_fork_parent** | **bool** | This flag indicates whether a parent virtual machine is in a fork ready state.  A persistent instant clone child can be created only when this flag is true. While a non-persistent instant clone child can be created independent of this flag, it can only be powered on if this flag is true.  ***Since:*** vSphere API 6.0  | [optional] 
**instant_clone_frozen** | **bool** | Whether the virtual machine is frozen for instant clone, or not.  ***Since:*** vSphere API 6.7  | [optional] 
**crypto_state** | **str** | Encryption state of the virtual machine.  Valid values are enumerated by the *CryptoState* type.  ***Since:*** vSphere API 6.7  | [optional] 
**suspended_to_memory** | **bool** | Whether the virtual machine is suspended to memory, or not.  ***Since:*** vSphere API 7.0.2.0  | [optional] 
**op_notification_timeout** | **int** | Operation notification timeout in seconds.  Specifies the maximum time duration the application may take to prepare for the operation after it has been notified. This property is set only for powered on VMs.  | [optional] 
**iommu_active** | **bool** | Indicates whether there is active IOMMU domain in the current VM.  | [optional] 

## Example

```python
from vmware_vi.models.virtual_machine_runtime_info import VirtualMachineRuntimeInfo

# TODO update the JSON string below
json = "{}"
# create an instance of VirtualMachineRuntimeInfo from a JSON string
virtual_machine_runtime_info_instance = VirtualMachineRuntimeInfo.from_json(json)
# print the JSON string representation of the object
print VirtualMachineRuntimeInfo.to_json()

# convert the object into a dict
virtual_machine_runtime_info_dict = virtual_machine_runtime_info_instance.to_dict()
# create an instance of VirtualMachineRuntimeInfo from a dict
virtual_machine_runtime_info_form_dict = virtual_machine_runtime_info.from_dict(virtual_machine_runtime_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


