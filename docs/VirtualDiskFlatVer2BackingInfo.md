# VirtualDiskFlatVer2BackingInfo

This data object type contains information about backing a virtual disk using a virtual disk file on the host, in the flat file format used by VMware Server, ESX Server 2.x, and ESX Server 3.x.  Flat disks are allocated when created, unlike sparse disks, which grow as needed. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**disk_mode** | **str** | The disk persistence mode.  Valid modes are: - *persistent* - *independent_persistent* - *independent_nonpersistent* - *nonpersistent* - *undoable* - *append*    See also *VirtualDiskMode_enum*.  | 
**split** | **bool** | Flag to indicate the type of virtual disk file: split or monolithic.  If true, the virtual disk is stored in multiple files, each 2GB. On ESX this property is ignored when creating new disks or editing existing disks. This property is always false for disks created on ESX. When an existing split disk such as those created by VMware Server is added to a virtual machine on ESX, the property will be set to true when retrieved from *VirtualMachineConfigInfo*.  | [optional] 
**write_through** | **bool** | Flag to indicate whether writes should go directly to the file system or should be buffered.  | [optional] 
**thin_provisioned** | **bool** | Flag to indicate to the underlying filesystem, whether the virtual disk backing file should be allocated lazily (using thin provisioning). This flag is only used for file systems that support configuring the provisioning policy on a per file basis, such as VMFS3.  When specified as part of a *VirtualMachineConfigSpec*, this property applies only when creating a new virtual disk; it is ignored when editing an existing virtual disk.  see *DatastoreCapability.perFileThinProvisioningSupported*  | [optional] 
**eagerly_scrub** | **bool** | Flag to indicate to the underlying filesystem whether the virtual disk backing file should be scrubbed completely at this time.  Virtual disks on some filesystems like VMFS3 are zeroed-out lazily so that disk creation time doesn&#39;t take too long. However, clustering applications and features like Fault Tolerance require that the virtual disk be completely scrubbed. This setting allows controlling the scrubbing policy on a per-disk basis.  If this flag is unset or set to false when creating a new disk, the disk scrubbing policy will be decided by the filesystem. If this flag is unset or set to false when editing an existing disk, it is ignored. When returned as part of a *VirtualMachineConfigInfo*, this property may be unset if its value is unknown.  ***Since:*** vSphere API 4.0  | [optional] 
**uuid** | **str** | Disk UUID for the virtual disk, if available.  ***Since:*** VI API 2.5  | [optional] 
**content_id** | **str** | Content ID of the virtual disk file, if available.  A content ID indicates the logical contents of the disk backing and its parents.  This property is only guaranteed to be up to date if this disk backing is not currently being written to by any virtual machine.  The only supported operation is comparing if two content IDs are equal or not. The guarantee provided by the content ID is that if two disk backings have the same content ID and are not currently being written to, then reads issued from the guest operating system to those disk backings will return the same data.  ***Since:*** vSphere API 4.0  | [optional] 
**change_id** | **str** | The change ID of the virtual disk for the corresponding snapshot or virtual machine.  This can be used to track incremental changes to a virtual disk. See *VirtualMachine.QueryChangedDiskAreas*.  ***Since:*** vSphere API 4.0  | [optional] 
**parent** | [**VirtualDiskFlatVer2BackingInfo**](VirtualDiskFlatVer2BackingInfo.md) |  | [optional] 
**delta_disk_format** | **str** | The format of the delta disk.  This field is valid only for a delta disk.  See *DeltaDiskFormat* for the supported formats. If not specified, the default value used is *redoLogFormat*.  If *nativeFormat* is specified and the datastore does not support this format or the parent is on a different datastore, *DeltaDiskFormatNotSupported* is thrown.  vSphere server does not support relocation of virtual machines with *nativeFormat*. An exception is thrown for such requests.  ***Since:*** vSphere API 5.0  | [optional] 
**digest_enabled** | **bool** | Indicates whether the disk backing has digest file enabled.  ***Since:*** vSphere API 5.0  | [optional] 
**delta_grain_size** | **int** | Grain size in kB for a delta disk of format type seSparseFormat.  The default size is 4 kB. This setting is used to specify the grain size of *Flex-SE* delta disks when the base disk is of type FlatVer2BackingInfo. The *DeltaDiskFormat* must also be set to seSparseFormat.  ***Since:*** vSphere API 5.1  | [optional] 
**delta_disk_format_variant** | **str** | The delta disk format variant, if applicable.  This field is valid only for a delta disk and may specify more detailed information for the delta disk format specified in *deltaDiskFormat*.  If *redoLogFormat* is specified for the *deltaDiskFormat*, see *DeltaDiskFormatVariant* for the supported formats. If this is not specified for *redoLogFormat*, the default value used is *vmfsSparseVariant*.  For other delta disk formats, this currently remains unspecified.  ***Since:*** vSphere API 6.0  | [optional] 
**sharing** | **str** | The sharing mode of the virtual disk.  See *VirtualDiskSharing_enum*. The default value is no sharing.  ***Since:*** vSphere API 6.0  | [optional] 
**key_id** | [**CryptoKeyId**](CryptoKeyId.md) |  | [optional] 

## Example

```python
from vmware_vi.models.virtual_disk_flat_ver2_backing_info import VirtualDiskFlatVer2BackingInfo

# TODO update the JSON string below
json = "{}"
# create an instance of VirtualDiskFlatVer2BackingInfo from a JSON string
virtual_disk_flat_ver2_backing_info_instance = VirtualDiskFlatVer2BackingInfo.from_json(json)
# print the JSON string representation of the object
print VirtualDiskFlatVer2BackingInfo.to_json()

# convert the object into a dict
virtual_disk_flat_ver2_backing_info_dict = virtual_disk_flat_ver2_backing_info_instance.to_dict()
# create an instance of VirtualDiskFlatVer2BackingInfo from a dict
virtual_disk_flat_ver2_backing_info_form_dict = virtual_disk_flat_ver2_backing_info.from_dict(virtual_disk_flat_ver2_backing_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


