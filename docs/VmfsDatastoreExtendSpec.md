# VmfsDatastoreExtendSpec

Specification to increase the capacity of a VMFS datastore by adding one or more new extents to the datastore.  All the extents to be added must be on the same disk. Extension is different from creation in that the VMFS creation specification need not be specified. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**partition** | [**HostDiskPartitionSpec**](HostDiskPartitionSpec.md) |  | 
**extent** | [**List[HostScsiDiskPartition]**](HostScsiDiskPartition.md) | Extents to append to VMFS.  | 

## Example

```python
from vmware_vi.models.vmfs_datastore_extend_spec import VmfsDatastoreExtendSpec

# TODO update the JSON string below
json = "{}"
# create an instance of VmfsDatastoreExtendSpec from a JSON string
vmfs_datastore_extend_spec_instance = VmfsDatastoreExtendSpec.from_json(json)
# print the JSON string representation of the object
print VmfsDatastoreExtendSpec.to_json()

# convert the object into a dict
vmfs_datastore_extend_spec_dict = vmfs_datastore_extend_spec_instance.to_dict()
# create an instance of VmfsDatastoreExtendSpec from a dict
vmfs_datastore_extend_spec_form_dict = vmfs_datastore_extend_spec.from_dict(vmfs_datastore_extend_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


