# VmfsDatastoreExpandSpec

Specification to increase the capacity of a VMFS datastore by expanding (increasing the size of) an existing extent of the datastore.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**partition** | [**HostDiskPartitionSpec**](HostDiskPartitionSpec.md) |  | 
**extent** | [**HostScsiDiskPartition**](HostScsiDiskPartition.md) |  | 

## Example

```python
from vmware_vi.models.vmfs_datastore_expand_spec import VmfsDatastoreExpandSpec

# TODO update the JSON string below
json = "{}"
# create an instance of VmfsDatastoreExpandSpec from a JSON string
vmfs_datastore_expand_spec_instance = VmfsDatastoreExpandSpec.from_json(json)
# print the JSON string representation of the object
print VmfsDatastoreExpandSpec.to_json()

# convert the object into a dict
vmfs_datastore_expand_spec_dict = vmfs_datastore_expand_spec_instance.to_dict()
# create an instance of VmfsDatastoreExpandSpec from a dict
vmfs_datastore_expand_spec_form_dict = vmfs_datastore_expand_spec.from_dict(vmfs_datastore_expand_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


