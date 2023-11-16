# VirtualDisk

This data object type contains information about a disk in a virtual machine.  The virtual disk backing object types describe the different virtual disk backings available. The disk format version in each case describes the version of the format that is used.  Supported virtual disk backings: <dl> <dt>Sparse disk format, version 1 and 2</dt> <dd>The virtual disk backing grows when needed. Supported only for VMware Server.</dd> <dt>Flat disk format, version 1 and 2</dt> <dd>The virtual disk backing is preallocated. Version 1 is supported only for VMware Server.</dd> <dt>Space efficient sparse disk format</dt> <dd>The virtual disk backing grows on demand and incorporates additional space optimizations.</dd> <dt>Raw disk format, version 2</dt> <dd>The virtual disk backing uses a full physical disk drive to back the virtual disk. Supported only for VMware Server.</dd> <dt>Partitioned raw disk format, version 2</dt> <dd>The virtual disk backing uses one or more partitions on a physical disk drive to back a virtual disk. Supported only for VMware Server.</dd> <dt>Raw disk mapping, version 1</dt> <dd>The virtual disk backing uses a raw device mapping to back the virtual disk. Supported for ESX Server 2.5 and 3.x.</dd> </dl> 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**capacity_in_kb** | **int** | Deprecated as of vSphere API 5.5, use *VirtualDisk.capacityInBytes*.  Capacity of this virtual disk in kilobytes.  Information might be lost when actual disk size is rounded off to kilobytes. If the disk is on a Virtual Volume datastore the disk size must be a multiple of a megabyte.  | 
**capacity_in_bytes** | **int** | Capacity of this virtual disk in bytes.  Server will always populate this property. Clients must initialize it when creating a new non -RDM disk or in case they want to change the current capacity of an existing virtual disk, but can omit it otherwise. If the disk is on a Virtual Volume datastore the disk size must be a multiple of a megabyte.  ***Since:*** vSphere API 5.5  | [optional] 
**shares** | [**SharesInfo**](SharesInfo.md) |  | [optional] 
**storage_io_allocation** | [**StorageIOAllocationInfo**](StorageIOAllocationInfo.md) |  | [optional] 
**disk_object_id** | **str** | Deprecated as of vSphere API 6.5, use *VirtualDisk.vDiskId*.  Virtual disk durable and unmutable identifier.  Virtual disk has a UUID field but that can be set through VirtualDiskManager APIs. This identifier is a universally unique identifier which is not settable. VirtualDisk can remain in existence even if it is not associated with VM.  ***Since:*** vSphere API 5.5  | [optional] 
**v_flash_cache_config_info** | [**VirtualDiskVFlashCacheConfigInfo**](VirtualDiskVFlashCacheConfigInfo.md) |  | [optional] 
**iofilter** | **List[str]** | IDs of the IO Filters associated with the virtual disk.  See *IoFilterInfo.id*. This information is provided when retrieving configuration information for an existing virtual machine. The client cannot modify this information on a virtual machine.  ***Since:*** vSphere API 6.0  | [optional] 
**v_disk_id** | [**ID**](ID.md) |  | [optional] 
**v_disk_version** | **int** | Disk descriptor version of the virtual disk.  | [optional] 
**native_unmanaged_linked_clone** | **bool** | Indicates whether a disk with *VirtualDiskFlatVer2BackingInfo* backing is a linked clone from an unmanaged delta disk and hence the *VirtualDiskFlatVer2BackingInfo.parent* chain to this delta disk will not be available.  ***Since:*** vSphere API 6.7  | [optional] 
**independent_filters** | [**List[VirtualMachineBaseIndependentFilterSpec]**](VirtualMachineBaseIndependentFilterSpec.md) | The IDs of the independent filters associated with the virtual disk.  This information is provided when retrieving configuration information for an existing virtual machine. The client cannot modify this information on a virtual machine.  ***Since:*** vSphere API 7.0.2.1  | [optional] 

## Example

```python
from vmware_vi.models.virtual_disk import VirtualDisk

# TODO update the JSON string below
json = "{}"
# create an instance of VirtualDisk from a JSON string
virtual_disk_instance = VirtualDisk.from_json(json)
# print the JSON string representation of the object
print VirtualDisk.to_json()

# convert the object into a dict
virtual_disk_dict = virtual_disk_instance.to_dict()
# create an instance of VirtualDisk from a dict
virtual_disk_form_dict = virtual_disk.from_dict(virtual_disk_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


