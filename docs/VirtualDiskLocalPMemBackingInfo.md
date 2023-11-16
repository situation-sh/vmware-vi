# VirtualDiskLocalPMemBackingInfo

This data object type contains information about backing a virtual disk using non-volatile memory technologies (persistent memory).  Supported for ESX Server 6.5 and later.  ***Since:*** vSphere API 6.7 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**disk_mode** | **str** | The disk persistence mode.  See also *VirtualDiskMode_enum*.  ***Since:*** vSphere API 6.7  | 
**uuid** | **str** | Disk UUID for the virtual disk, if available.  ***Since:*** vSphere API 6.7  | [optional] 
**volume_uuid** | **str** | Persistent memory volume UUID - UUID which associates this virtual disk with a specific host.  This is read only property.  See also *HostPersistentMemoryInfo.volumeUUID*.  ***Since:*** vSphere API 6.7  | [optional] 
**content_id** | **str** | Content ID of the virtual disk file, if available.  A content ID indicates the logical contents of the disk backing and its parents.  This property is only guaranteed to be up to date if this disk backing is not currently being written to by any virtual machine.  The only supported operation is comparing if two content IDs are equal or not. The guarantee provided by the content ID is that if two disk backings have the same content ID and are not currently being written to, then reads issued from the guest operating system to those disk backings will return the same data.  ***Since:*** vSphere API 6.7  | [optional] 

## Example

```python
from vmware_vi.models.virtual_disk_local_p_mem_backing_info import VirtualDiskLocalPMemBackingInfo

# TODO update the JSON string below
json = "{}"
# create an instance of VirtualDiskLocalPMemBackingInfo from a JSON string
virtual_disk_local_p_mem_backing_info_instance = VirtualDiskLocalPMemBackingInfo.from_json(json)
# print the JSON string representation of the object
print VirtualDiskLocalPMemBackingInfo.to_json()

# convert the object into a dict
virtual_disk_local_p_mem_backing_info_dict = virtual_disk_local_p_mem_backing_info_instance.to_dict()
# create an instance of VirtualDiskLocalPMemBackingInfo from a dict
virtual_disk_local_p_mem_backing_info_form_dict = virtual_disk_local_p_mem_backing_info.from_dict(virtual_disk_local_p_mem_backing_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


