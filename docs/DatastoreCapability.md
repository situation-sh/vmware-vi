# DatastoreCapability

Information about the capabilities of this datastore. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**directory_hierarchy_supported** | **bool** | Indicates whether or not directories can be created on this datastore.  | 
**raw_disk_mappings_supported** | **bool** | Indicates whether or not raw disk mappings can be created on this datastore.  | 
**per_file_thin_provisioning_supported** | **bool** | Indicates whether or not the datastore supports thin provisioning on a per file basis.  When thin provisioning is used, backing storage is lazily allocated.  This is supported by VMFS3. VMFS2 always allocates storage eagerly. Thus, this value is false for VMFS2. Most NAS systems always use thin provisioning. They do not support configuring this on a per file basis, so for NAS systems this value is also false.  | 
**storage_iorm_supported** | **bool** | Indicates whether the datastore supports Storage I/O Resource Management.  ***Since:*** vSphere API 4.1  | 
**native_snapshot_supported** | **bool** | Indicates whether the datastore supports native snapshot feature which is based on Copy-On-Write.  ***Since:*** vSphere API 5.1  | 
**top_level_directory_create_supported** | **bool** | Indicates whether the datastore supports traditional top-level directory creation.  See also *DatastoreNamespaceManager*.  ***Since:*** vSphere API 5.5  | [optional] 
**se_sparse_supported** | **bool** | Indicates whether the datastore supports the Flex-SE(SeSparse) feature.  ***Since:*** vSphere API 5.5  | [optional] 
**vmfs_sparse_supported** | **bool** | Indicates whether the datastore supports the vmfsSparse feature.  True for VMFS3/VMFS5/NFS/NFS41, False for VMFS6. If value is undefined, then it should be read as supported.  ***Since:*** vSphere API 6.5  | [optional] 
**vsan_sparse_supported** | **bool** | Indicates whether the datastore supports the vsanSparse feature.  ***Since:*** vSphere API 6.5  | [optional] 
**upit_supported** | **bool** | Deprecated as of vSphere API 8.0, and there is no replacement for it.  Indicates whether the datastore supports the upit feature.  ***Since:*** vSphere API 6.5  | [optional] 
**vmdk_expand_supported** | **bool** | On certain datastores (e.g.  2016 PMEM datastore) VMDK expand is not supported. This field tells user if VMDK on this datastore can be expanded or not. If value is undefined, then it should be read as supported.  ***Since:*** vSphere API 6.7  | [optional] 
**clustered_vmdk_supported** | **bool** | Indicates whether the datastore supports clustered VMDK feature.  ***Since:*** vSphere API 7.0  | [optional] 

## Example

```python
from vmware_vi.models.datastore_capability import DatastoreCapability

# TODO update the JSON string below
json = "{}"
# create an instance of DatastoreCapability from a JSON string
datastore_capability_instance = DatastoreCapability.from_json(json)
# print the JSON string representation of the object
print DatastoreCapability.to_json()

# convert the object into a dict
datastore_capability_dict = datastore_capability_instance.to_dict()
# create an instance of DatastoreCapability from a dict
datastore_capability_form_dict = datastore_capability.from_dict(datastore_capability_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


