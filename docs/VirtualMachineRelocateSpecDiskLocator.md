# VirtualMachineRelocateSpecDiskLocator

The DiskLocator data object type specifies a virtual disk device (by ID) and a datastore locator for the disk's storage. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**disk_id** | **int** | Device ID of the virtual disk.  | 
**datastore** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | 
**disk_move_type** | **str** | Manner in which to move the virtual disk to the *target datastore*.  The set of possible values is described in *VirtualMachineRelocateDiskMoveOptions_enum*.  This property can only be set if *HostCapability.deltaDiskBackingsSupported* is true.  If left unset then *moveAllDiskBackingsAndDisallowSharing* is assumed.  ***Since:*** vSphere API 4.0  | [optional] 
**disk_backing_info** | [**VirtualDeviceBackingInfo**](VirtualDeviceBackingInfo.md) |  | [optional] 
**profile** | [**List[VirtualMachineProfileSpec]**](VirtualMachineProfileSpec.md) | Virtual Disk Profile requirement.  Profiles are solution specific. Profile Based Storage Management is a vSphere server extension. The API users who want to provision VMs using Storage Profiles, need to interact with it. This is an optional parameter and if user doesn&#39;t specify profile, the default behavior will apply.  ***Since:*** vSphere API 5.5  | [optional] 
**backing** | [**VirtualMachineRelocateSpecDiskLocatorBackingSpec**](VirtualMachineRelocateSpecDiskLocatorBackingSpec.md) |  | [optional] 
**filter_spec** | [**List[VirtualMachineBaseIndependentFilterSpec]**](VirtualMachineBaseIndependentFilterSpec.md) | List of independent filters *VirtualMachineIndependentFilterSpec* to be configured on the virtual disk after the relocate.  ***Since:*** vSphere API 7.0.2.1  | [optional] 

## Example

```python
from vmware_vi.models.virtual_machine_relocate_spec_disk_locator import VirtualMachineRelocateSpecDiskLocator

# TODO update the JSON string below
json = "{}"
# create an instance of VirtualMachineRelocateSpecDiskLocator from a JSON string
virtual_machine_relocate_spec_disk_locator_instance = VirtualMachineRelocateSpecDiskLocator.from_json(json)
# print the JSON string representation of the object
print VirtualMachineRelocateSpecDiskLocator.to_json()

# convert the object into a dict
virtual_machine_relocate_spec_disk_locator_dict = virtual_machine_relocate_spec_disk_locator_instance.to_dict()
# create an instance of VirtualMachineRelocateSpecDiskLocator from a dict
virtual_machine_relocate_spec_disk_locator_form_dict = virtual_machine_relocate_spec_disk_locator.from_dict(virtual_machine_relocate_spec_disk_locator_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


