# HostDatastoreSystemCapabilities

Capability vector indicating the available product features.  ***Since:*** VI API 2.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**nfs_mount_creation_required** | **bool** | Indicates whether mounting the NFS volume is required to be done as part of NAS datastore creation.  If this is set to true, then NAS datastores cannot be created for currently mounted NFS volumes.  ***Since:*** VI API 2.5  | 
**nfs_mount_creation_supported** | **bool** | Indicates whether mounting an NFS volume is supported when a NAS datastore is created.  If this option is false, then NAS datastores corresponding to NFS volumes can be created only for already mounted NFS volumes.  ***Since:*** VI API 2.5  | 
**local_datastore_supported** | **bool** | Indicates whether local datastores are supported.  ***Since:*** VI API 2.5  | 
**vmfs_extent_expansion_supported** | **bool** | Indicates whether vmfs extent expansion is supported.  ***Since:*** vSphere API 4.0  | 

## Example

```python
from vmware_vi.models.host_datastore_system_capabilities import HostDatastoreSystemCapabilities

# TODO update the JSON string below
json = "{}"
# create an instance of HostDatastoreSystemCapabilities from a JSON string
host_datastore_system_capabilities_instance = HostDatastoreSystemCapabilities.from_json(json)
# print the JSON string representation of the object
print HostDatastoreSystemCapabilities.to_json()

# convert the object into a dict
host_datastore_system_capabilities_dict = host_datastore_system_capabilities_instance.to_dict()
# create an instance of HostDatastoreSystemCapabilities from a dict
host_datastore_system_capabilities_form_dict = host_datastore_system_capabilities.from_dict(host_datastore_system_capabilities_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


