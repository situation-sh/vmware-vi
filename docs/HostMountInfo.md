# HostMountInfo

The *HostMountInfo* data object provides information related to a configured mount point.  This object does not include information about the mounted file system. (See *HostFileSystemMountInfo*.) 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**path** | **str** | Local file path where file system volume is mounted, if applicable.  This path identifies the file system volume from the point of view of the host.  | [optional] 
**access_mode** | **str** | Access mode to the underlying file system for this host.  | 
**mounted** | **bool** | The mount state of this mount point.  For a discovered volume, which is mounted, this is true. When this value is unset, the default value is true.  ***Since:*** vSphere API 5.0  | [optional] 
**accessible** | **bool** | Flag that indicates if the datastore is currently accessible from the host.  For the case of a standalone host, this property has the same value as *DatastoreSummary*.*DatastoreSummary.accessible*. You can use the *DatastoreSummary* property if the *HostMountInfo* property is not set. The VirtualCenter Server will always make sure the *DatastoreSummary* property is set correctly.  ***Since:*** VI API 2.5  | [optional] 
**inaccessible_reason** | **str** | This optional property for inaccessible reason is reported only if a datastore becomes inaccessible as reported by *HostMountInfo.accessible* and *DatastoreSummary*.*DatastoreSummary.accessible*.  The values for inaccessible reason are defined in the enum *HostMountInfoInaccessibleReason_enum* This helps to determine host specific reason for datastore inaccessibility. If the datastore becomes accessible following an inaccessible condition, the property *HostMountInfo.inaccessibleReason* will be unset.  ***Since:*** vSphere API 5.1  | [optional] 
**vmknic_name** | **str** | The name of the vmknic used during mount.  Populated by the vmk control layer if the NAS volume is mounted successfully with a vmknic binding.  | [optional] 
**vmknic_active** | **bool** | Indicates whether vmknic is active or inactive.  This field will be populated by vmk control layer during NAS volume mount, and will be set to true if the vmknic binding is active.  | [optional] 
**mount_failed_reason** | **str** | The optional property which gives the reason for mount operation failure of NFS datastore.  This field is applicable for only those mounts for which retry mount operation is configured. The values for the mount failed reason are defined in the enum *HostMountInfoMountFailedReason_enum*. If mount operation on NFS volume succeeds in the retry, then the property *HostMountInfo.mountFailedReason* will be unset.  | [optional] 
**num_tcp_connections** | **int** | Maintained for each Host, it indicates the total number of TCP connections for the NAS datastore  | [optional] 

## Example

```python
from vmware_vi.models.host_mount_info import HostMountInfo

# TODO update the JSON string below
json = "{}"
# create an instance of HostMountInfo from a JSON string
host_mount_info_instance = HostMountInfo.from_json(json)
# print the JSON string representation of the object
print HostMountInfo.to_json()

# convert the object into a dict
host_mount_info_dict = host_mount_info_instance.to_dict()
# create an instance of HostMountInfo from a dict
host_mount_info_form_dict = host_mount_info.from_dict(host_mount_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


