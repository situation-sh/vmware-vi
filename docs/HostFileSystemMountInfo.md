# HostFileSystemMountInfo

The *HostFileSystemMountInfo* data object describes a host mount point for a file system. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mount_info** | [**HostMountInfo**](HostMountInfo.md) |  | 
**volume** | [**HostFileSystemVolume**](HostFileSystemVolume.md) |  | 
**v_storage_support** | **str** | vStorage hardware acceleration support status.  This property represents the volume&#39;s capability for storage acceleration. See *FileSystemMountInfoVStorageSupportStatus_enum* for valid values.  If the ESX Server supports hardware acceleration, the Server can offload specific virtual machine management operations to a storage device with the hardware acceleration feature. With hardware assistance, the host performs storage operations faster and consumes less CPU, memory, and storage fabric bandwidth.  For vSphere 4.0 or earlier hosts, this value will be unset.  ***Since:*** vSphere API 4.1  | [optional] 

## Example

```python
from vmware_vi.models.host_file_system_mount_info import HostFileSystemMountInfo

# TODO update the JSON string below
json = "{}"
# create an instance of HostFileSystemMountInfo from a JSON string
host_file_system_mount_info_instance = HostFileSystemMountInfo.from_json(json)
# print the JSON string representation of the object
print HostFileSystemMountInfo.to_json()

# convert the object into a dict
host_file_system_mount_info_dict = host_file_system_mount_info_instance.to_dict()
# create an instance of HostFileSystemMountInfo from a dict
host_file_system_mount_info_form_dict = host_file_system_mount_info.from_dict(host_file_system_mount_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


