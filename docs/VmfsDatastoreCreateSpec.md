# VmfsDatastoreCreateSpec

This data object type is used when creating a new VMFS datastore, to create a specification for the VMFS datastore. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**partition** | [**HostDiskPartitionSpec**](HostDiskPartitionSpec.md) |  | 
**vmfs** | [**HostVmfsSpec**](HostVmfsSpec.md) |  | 
**extent** | [**List[HostScsiDiskPartition]**](HostScsiDiskPartition.md) | Extents to append to VMFS.  | [optional] 

## Example

```python
from vmware_vi.models.vmfs_datastore_create_spec import VmfsDatastoreCreateSpec

# TODO update the JSON string below
json = "{}"
# create an instance of VmfsDatastoreCreateSpec from a JSON string
vmfs_datastore_create_spec_instance = VmfsDatastoreCreateSpec.from_json(json)
# print the JSON string representation of the object
print VmfsDatastoreCreateSpec.to_json()

# convert the object into a dict
vmfs_datastore_create_spec_dict = vmfs_datastore_create_spec_instance.to_dict()
# create an instance of VmfsDatastoreCreateSpec from a dict
vmfs_datastore_create_spec_form_dict = vmfs_datastore_create_spec.from_dict(vmfs_datastore_create_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


