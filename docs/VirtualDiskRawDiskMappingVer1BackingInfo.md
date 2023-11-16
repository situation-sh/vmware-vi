# VirtualDiskRawDiskMappingVer1BackingInfo

This data object type contains information about backing a virtual disk using a raw device mapping.  Supported for ESX Server 2.5 and 3.x. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**lun_uuid** | **str** | Unique identifier of the LUN accessed by the raw disk mapping.  | [optional] 
**device_name** | **str** | The host-specific device the LUN is being accessed through.  If the target LUN is not available on the host then it is empty. For example, this could happen if it has accidentally been masked out.  | [optional] 
**compatibility_mode** | **str** | The compatibility mode of the raw disk mapping (RDM).  This must be specified when a new virtual disk with an RDM backing is created. On subsequent virtual machine reconfigurations, this property should be handled as follows, depending on the version of the host:  On ESX Server 2.5, the compatibility mode of an RDM backing is a characteristic of the virtual machine&#39;s configuration. When reconfiguring a virtual machine that currently uses a virtual disk backed by an RDM, the compatibility mode of that backing may be modified. When reconfiguring a virtual machine to add an existing virtual disk backed by an RDM, the compatibility mode of that backing may be specified. If left unspecified it defaults to \&quot;physicalMode\&quot;.  On ESX Server 3.x, the compatibility mode of an RDM backing is a characteristic of the RDM itself. Once the RDM is created, its compatibility mode cannot be changed by reconfiguring the virtual machine. When reconfiguring a virtual machine to add an existing virtual disk backed by an RDM, the compatibility mode of that backing must be left unspecified.  See also *VirtualDiskCompatibilityMode_enum*.  | [optional] 
**disk_mode** | **str** | The disk mode.  Valid values are: - *persistent* - *independent_persistent* - *independent_nonpersistent* - *nonpersistent* - *undoable* - *append*    Disk modes are only supported when the raw disk mapping is using virtual compatibility mode.  See also *VirtualDiskMode_enum*.  | [optional] 
**uuid** | **str** | Disk UUID for the virtual disk, if available.  Disk UUID is not available if the raw disk mapping is in physical compatibility mode.  ***Since:*** VI API 2.5  | [optional] 
**content_id** | **str** | Content ID of the virtual disk file, if available.  A content ID indicates the logical contents of the disk backing and its parents.  This property is only guaranteed to be up to date if this disk backing is not currently being written to by any virtual machine.  The only supported operation is comparing if two content IDs are equal or not. The guarantee provided by the content ID is that if two disk backings have the same content ID and are not currently being written to, then reads issued from the guest operating system to those disk backings will return the same data.  ***Since:*** vSphere API 4.0  | [optional] 
**change_id** | **str** | The change ID of the virtual disk for the corresponding snapshot or virtual machine.  This can be used to track incremental changes to a virtual disk. See *VirtualMachine.QueryChangedDiskAreas*.  ***Since:*** vSphere API 4.0  | [optional] 
**parent** | [**VirtualDiskRawDiskMappingVer1BackingInfo**](VirtualDiskRawDiskMappingVer1BackingInfo.md) |  | [optional] 
**delta_disk_format** | **str** | The format of the delta disk.  This field is valid only for a delta disk.  See *DeltaDiskFormat* for the supported formats. The default value used for VM with hardware version 8 and lower is *redoLogFormat*. The default value used for VM with hardware version 9 and higher is *seSparseFormat*.  *nativeFormat* is not supported for bask disk of type RawDiskMappingVer1BackingInfo.  ***Since:*** vSphere API 6.7  | [optional] 
**delta_grain_size** | **int** | Grain size in kB for a delta disk of format type seSparseFormat.  The default size is 4 kB. The grain size of *Flex-SE* delta disks when the base disk is of type RawDiskMappingVer1BackingInfo. The *DeltaDiskFormat* must also be set to seSparseFormat.  ***Since:*** vSphere API 6.7  | [optional] 
**sharing** | **str** | The sharing mode of the virtual disk.  See *VirtualDiskSharing_enum*. The default value is no sharing.  ***Since:*** vSphere API 6.0  | [optional] 

## Example

```python
from vmware_vi.models.virtual_disk_raw_disk_mapping_ver1_backing_info import VirtualDiskRawDiskMappingVer1BackingInfo

# TODO update the JSON string below
json = "{}"
# create an instance of VirtualDiskRawDiskMappingVer1BackingInfo from a JSON string
virtual_disk_raw_disk_mapping_ver1_backing_info_instance = VirtualDiskRawDiskMappingVer1BackingInfo.from_json(json)
# print the JSON string representation of the object
print VirtualDiskRawDiskMappingVer1BackingInfo.to_json()

# convert the object into a dict
virtual_disk_raw_disk_mapping_ver1_backing_info_dict = virtual_disk_raw_disk_mapping_ver1_backing_info_instance.to_dict()
# create an instance of VirtualDiskRawDiskMappingVer1BackingInfo from a dict
virtual_disk_raw_disk_mapping_ver1_backing_info_form_dict = virtual_disk_raw_disk_mapping_ver1_backing_info.from_dict(virtual_disk_raw_disk_mapping_ver1_backing_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


