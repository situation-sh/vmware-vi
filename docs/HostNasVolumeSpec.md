# HostNasVolumeSpec

Specification for creating NAS volume.  When mounting a NAS volume on multiple hosts, the same remoteHost and remotePath values should be used on every host, otherwise it will be treated as different datastores. For example, if one host references the remotePath of a NAS volume as \"/mnt/mount1\" and another references it as \"/mnt/mount1/\", it will not be recognized as the same datastore. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**remote_host** | **str** | The host that runs the NFS v3 or CIFS server.  For NFS v4.1 and beyond use remoteHostNames defined later. The field remotehost may be deprecated in future for NFS, so clients should plan to use the property remoteHostNames to send in the host name(s) for both NFS v3 and v4.1  | 
**remote_path** | **str** | The remote path of the NFS mount point.  | 
**local_path** | **str** | The localPath refers to the name of the NAS datastore to be created using this specification.  In the case of ESX Server, the datastore name is a component in the file system path at which the NAS volume can be found. For example, if localPath is set to \&quot;nas\\_volume\&quot; the created NAS datastore will be named \&quot;nas\\_volume\&quot; and it can be accessed via the file system path \&quot;/vmfs/volumes/nas\\_volume\&quot;.  In the case of VMware Server, the localPath will also be used as the datastore name, but the datastore name may not necessarily be reflected in the file system path where the NAS volume may be accessed.  | 
**access_mode** | **str** | Access mode for the mount point.  Mounting in read-write mode would be successful irregardless on how the mount point is exported or access permissions. For example, mounting a volume that is exported as read-only as readWrite will succeed. Hence, that a readWrite mount succeeds should not be taken as an indication that all files on a mount is writable.  If a file system is mounted readOnly, the system cannot create or modify any files on the file system. This is mostly useful for storing ISO images and templates, since a virtual machine cannot be powered on from a readOnly volume.  The access mode of a mounted NFS volume can be obtained at *HostMountInfo.accessMode*.  See also *HostMountMode_enum*.  | 
**type** | **str** | Specifies the type of the the NAS volume.  Supported types are *CIFS*, *NFS*, *NFS41* If not specified, defaults to *NFS*  ***Since:*** VI API 2.5  | [optional] 
**user_name** | **str** | If type is CIFS, the user name to use when connecting to the CIFS server.  If type is NFS, this field will be ignored.  ***Since:*** VI API 2.5  | [optional] 
**password** | **str** | If type is CIFS, the password to use when connecting to the CIFS server.  If type is NFS, this field will be ignored.  ***Since:*** VI API 2.5  | [optional] 
**remote_host_names** | **List[str]** | Hostnames or IP addresses of remote NFS server.  In case of NFS v4.1 this may have multiple entries. For NFS v3 the input should be same in both remoteHost and remoteHostNames. In case of NFS v4.1, if vmknic binding is enabled, then input can be in format {hostip1:vmknic1, hostip2:vmknic2}.  ***Since:*** vSphere API 6.0  | [optional] 
**security_type** | **str** | Provided during mount indicating what security type, if any, to use See *HostNasVolumeSecurityType_enum*  ***Since:*** vSphere API 6.0  | [optional] 
**vmknic_to_bind** | **str** | Name of the vmknic to be used by this mount.  This field will be updated by a client with vmknic that will be used for NAS volume mount operation for vmknic binding for NFSv3  | [optional] 
**vmknic_bound** | **bool** | Indicates whether a client wants to bind this mount to vmknic.  This field will be set to true by a client if vmknic should bind during NAS volume mount operation for NFSv3 else it will be set to false  | [optional] 
**connections** | **int** | Indicates the number of TCP connections for the particular NFSv3 Server during NAS volume mount operation.  If unset or set to 0, it defaults to one connection  | [optional] 

## Example

```python
from vmware_vi.models.host_nas_volume_spec import HostNasVolumeSpec

# TODO update the JSON string below
json = "{}"
# create an instance of HostNasVolumeSpec from a JSON string
host_nas_volume_spec_instance = HostNasVolumeSpec.from_json(json)
# print the JSON string representation of the object
print HostNasVolumeSpec.to_json()

# convert the object into a dict
host_nas_volume_spec_dict = host_nas_volume_spec_instance.to_dict()
# create an instance of HostNasVolumeSpec from a dict
host_nas_volume_spec_form_dict = host_nas_volume_spec.from_dict(host_nas_volume_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


