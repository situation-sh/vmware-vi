# ConfigTarget

The ConfigTarget class contains information about \"physical\" devices that can be used to back virtual devices. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**num_cpus** | **int** | Number of logical CPUs that can be used to run virtual machines.  If invoked against a cluster, this is the total number of logical CPUs available in the cluster.  | 
**num_cpu_cores** | **int** | Number of physical CPU cores that are available to run virtual machines.  If invoked against a cluster, this is the total number of physical CPUs available in the cluster.  | 
**num_numa_nodes** | **int** | Number of NUMA nodes.  If invoked against a cluster, this is the total number of NUMA nodes available in the cluster.  | 
**max_cpus_per_host** | **int** | Maximum number of CPUs available on a single host.  For standalone hosts, this value will be the same as numCpus.  ***Since:*** vSphere API 7.0  | [optional] 
**smc_present** | **bool** | Presence of System Management Controller, indicates the host is Apple hardware, and thus capable of running Mac OS guest as VM.  ***Since:*** vSphere API 5.0  | 
**datastore** | [**List[VirtualMachineDatastoreInfo]**](VirtualMachineDatastoreInfo.md) | List of datastores available for virtual disks and associated storage.  | [optional] 
**network** | [**List[VirtualMachineNetworkInfo]**](VirtualMachineNetworkInfo.md) | List of networks available for virtual network adapters.  | [optional] 
**opaque_network** | [**List[OpaqueNetworkTargetInfo]**](OpaqueNetworkTargetInfo.md) | List of opaque networks available for virtual network adapters.  ***Since:*** vSphere API 5.5  | [optional] 
**distributed_virtual_portgroup** | [**List[DistributedVirtualPortgroupInfo]**](DistributedVirtualPortgroupInfo.md) | List of networks available from DistributedVirtualSwitch for virtual network adapters.  ***Since:*** vSphere API 4.0  | [optional] 
**distributed_virtual_switch** | [**List[DistributedVirtualSwitchInfo]**](DistributedVirtualSwitchInfo.md) | List of distributed virtual switch available for virtual network adapters.  ***Since:*** vSphere API 4.0  | [optional] 
**cd_rom** | [**List[VirtualMachineCdromInfo]**](VirtualMachineCdromInfo.md) | List of CD-ROM devices available for use by virtual CD-ROMs.  Used for *VirtualCdromAtapiBackingInfo*.  | [optional] 
**serial** | [**List[VirtualMachineSerialInfo]**](VirtualMachineSerialInfo.md) | List of serial devices available to support virtualization.  Used for *VirtualSerialPortDeviceBackingInfo*.  | [optional] 
**parallel** | [**List[VirtualMachineParallelInfo]**](VirtualMachineParallelInfo.md) | List of parallel devices available to support virtualization.  Used for *VirtualParallelPortDeviceBackingInfo*.  | [optional] 
**sound** | [**List[VirtualMachineSoundInfo]**](VirtualMachineSoundInfo.md) | List of sound devices available to support virtualization.  Used for *VirtualSoundCardDeviceBackingInfo*.  ***Since:*** VI API 2.5  | [optional] 
**usb** | [**List[VirtualMachineUsbInfo]**](VirtualMachineUsbInfo.md) | List of USB devices on the host that are available to support virtualization.  Used for *VirtualUSBUSBBackingInfo*.  ***Since:*** VI API 2.5  | [optional] 
**floppy** | [**List[VirtualMachineFloppyInfo]**](VirtualMachineFloppyInfo.md) | List of floppy devices available for use by virtual floppies.  Used for *VirtualFloppyDeviceBackingInfo*.  | [optional] 
**legacy_network_info** | [**List[VirtualMachineLegacyNetworkSwitchInfo]**](VirtualMachineLegacyNetworkSwitchInfo.md) | Legacy switch names when using the LegacyNetworkBacking types.  | [optional] 
**scsi_passthrough** | [**List[VirtualMachineScsiPassthroughInfo]**](VirtualMachineScsiPassthroughInfo.md) | List of generic SCSI devices.  | [optional] 
**scsi_disk** | [**List[VirtualMachineScsiDiskDeviceInfo]**](VirtualMachineScsiDiskDeviceInfo.md) | List of physical SCSI disks that can be used as targets for raw disk mapping backings.  | [optional] 
**ide_disk** | [**List[VirtualMachineIdeDiskDeviceInfo]**](VirtualMachineIdeDiskDeviceInfo.md) | List of physical IDE disks that can be used as targets for raw disk backings.  | [optional] 
**max_mem_mb_optimal_perf** | **int** | Maximum recommended memory size, in MB, for creating a new virtual machine.  | 
**supported_max_mem_mb** | **int** | Maximum supported memory size, in MB, for creating a new virtual machine.  Maximum allowed size is smaller of this and limit in *GuestOsDescriptor.supportedMaxMemMB*. When invoked on the cluster, maximum size that can be created on at least one host in the cluster is reported.  ***Since:*** vSphere API 7.0  | [optional] 
**resource_pool** | [**ResourcePoolRuntimeInfo**](ResourcePoolRuntimeInfo.md) |  | [optional] 
**auto_vmotion** | **bool** | Information whether a virtual machine with this ConfigTarget can auto vmotion.  This field is only populated from an Environment browser obtained from a virtual machine.  | [optional] 
**pci_passthrough** | [**List[VirtualMachinePciPassthroughInfo]**](VirtualMachinePciPassthroughInfo.md) | List of generic PCI devices.  ***Since:*** vSphere API 4.0  | [optional] 
**sriov** | [**List[VirtualMachineSriovInfo]**](VirtualMachineSriovInfo.md) | List of SRIOV devices.  ***Since:*** vSphere API 5.5  | [optional] 
**v_flash_module** | [**List[VirtualMachineVFlashModuleInfo]**](VirtualMachineVFlashModuleInfo.md) | List of vFlash modules.  ***Since:*** vSphere API 5.5  | [optional] 
**shared_gpu_passthrough_types** | [**List[VirtualMachinePciSharedGpuPassthroughInfo]**](VirtualMachinePciSharedGpuPassthroughInfo.md) | List of shared GPU passthrough types.  ***Since:*** vSphere API 6.0  | [optional] 
**available_persistent_memory_reservation_mb** | **int** | Maximum available persistent memory reservation on a compute resource in MB.  ***Since:*** vSphere API 6.7  | [optional] 
**dynamic_passthrough** | [**List[VirtualMachineDynamicPassthroughInfo]**](VirtualMachineDynamicPassthroughInfo.md) | List of Dynamic DirectPath PCI devices.  ***Since:*** vSphere API 7.0  | [optional] 
**sgx_target_info** | [**VirtualMachineSgxTargetInfo**](VirtualMachineSgxTargetInfo.md) |  | [optional] 
**precision_clock_info** | [**List[VirtualMachinePrecisionClockInfo]**](VirtualMachinePrecisionClockInfo.md) | List of host clock resources available to support virtual precision clock device.  Used for *VirtualPrecisionClockSystemClockBackingInfo*  ***Since:*** vSphere API 7.0  | [optional] 
**sev_supported** | **bool** | Indicates whether the compute resource is capable of running AMD Secure Encrypted Virtualization (SEV) enabled virtual machines.  The compute resource supports SEV when this value is set to true.  ***Since:*** vSphere API 7.0.1.0  | [optional] 
**vgpu_device_info** | [**List[VirtualMachineVgpuDeviceInfo]**](VirtualMachineVgpuDeviceInfo.md) | List of vGPU device capabilities.  ***Since:*** vSphere API 7.0.3.0  | [optional] 
**vgpu_profile_info** | [**List[VirtualMachineVgpuProfileInfo]**](VirtualMachineVgpuProfileInfo.md) | List of vGPU profile attributes.  ***Since:*** vSphere API 7.0.3.0  | [optional] 
**vendor_device_group_info** | [**List[VirtualMachineVendorDeviceGroupInfo]**](VirtualMachineVendorDeviceGroupInfo.md) | List of PCI Vendor Device Groups.  | [optional] 
**max_simultaneous_threads** | **int** | Max SMT (Simultaneous multithreading) threads.  | [optional] 
**dvx_class_info** | [**List[VirtualMachineDvxClassInfo]**](VirtualMachineDvxClassInfo.md) | List of Device Virtualization Extensions (DVX) classes.  | [optional] 

## Example

```python
from vmware_vi.models.config_target import ConfigTarget

# TODO update the JSON string below
json = "{}"
# create an instance of ConfigTarget from a JSON string
config_target_instance = ConfigTarget.from_json(json)
# print the JSON string representation of the object
print ConfigTarget.to_json()

# convert the object into a dict
config_target_dict = config_target_instance.to_dict()
# create an instance of ConfigTarget from a dict
config_target_form_dict = config_target.from_dict(config_target_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


