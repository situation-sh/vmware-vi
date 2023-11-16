# VirtualMachineRelocateSpec

Specification for moving or copying a virtual machine to a different datastore or host. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**service** | [**ServiceLocator**](ServiceLocator.md) |  | [optional] 
**folder** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | [optional] 
**datastore** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | [optional] 
**disk_move_type** | **str** | Manner in which to move the virtual disk to the *target datastore*.  The set of possible values is described in *VirtualMachineRelocateDiskMoveOptions_enum*.  This property applies to all the disks which the virtual machine has, but can be overridden on a per-disk basis using *VirtualMachineRelocateSpecDiskLocator.diskMoveType* prior to vSphere API 6.0 or using *VirtualDiskConfigSpec.diskMoveType* in vSphere API 6.0 and later.  This property can only be set if *HostCapability.deltaDiskBackingsSupported* is true.  If left unset then *moveAllDiskBackingsAndDisallowSharing* is assumed.  ***Since:*** vSphere API 4.0  | [optional] 
**pool** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | [optional] 
**host** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | [optional] 
**disk** | [**List[VirtualMachineRelocateSpecDiskLocator]**](VirtualMachineRelocateSpecDiskLocator.md) | An optional list that allows specifying the datastore location for each virtual disk.  | [optional] 
**transform** | [**VirtualMachineRelocateTransformationEnum**](VirtualMachineRelocateTransformationEnum.md) |  | [optional] 
**device_change** | [**List[VirtualDeviceConfigSpec]**](VirtualDeviceConfigSpec.md) | An optional list of virtual device specs that allow specifying the new device locations for the relocate operation.  The supported device changes are: - For *VirtualEthernetCard*, it has to be used   in *VirtualDeviceConfigSpec.device* to specify the   target network backing. - For *VirtualDisk*, it can be used to specify   vFlash cache configuration, or the storage profile for destination   disks. The storage profiles are used to either upgrade the virtual   disk&#39;s storage to a persistent memory, or keep the virtual disk   in persistent memory when moving the virtual machine&#39;s overall   storage. - All other specification are ignored.    ***Since:*** vSphere API 5.5  | [optional] 
**profile** | [**List[VirtualMachineProfileSpec]**](VirtualMachineProfileSpec.md) | Storage profile requirement for Virtual Machine&#39;s home directory.  Profiles are solution specific. Storage Profile Based Management(SPBM) is a vSphere server extension. The API users who want to provision VMs using Storage Profiles, need to interact with SPBM. This is an optional parameter and if user doesn&#39;t specify profile, the default behavior will apply.  ***Since:*** vSphere API 5.5  | [optional] 
**crypto_spec** | [**CryptoSpec**](CryptoSpec.md) |  | [optional] 

## Example

```python
from vmware_vi.models.virtual_machine_relocate_spec import VirtualMachineRelocateSpec

# TODO update the JSON string below
json = "{}"
# create an instance of VirtualMachineRelocateSpec from a JSON string
virtual_machine_relocate_spec_instance = VirtualMachineRelocateSpec.from_json(json)
# print the JSON string representation of the object
print VirtualMachineRelocateSpec.to_json()

# convert the object into a dict
virtual_machine_relocate_spec_dict = virtual_machine_relocate_spec_instance.to_dict()
# create an instance of VirtualMachineRelocateSpec from a dict
virtual_machine_relocate_spec_form_dict = virtual_machine_relocate_spec.from_dict(virtual_machine_relocate_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


