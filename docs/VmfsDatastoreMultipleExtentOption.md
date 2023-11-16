# VmfsDatastoreMultipleExtentOption

Datastore addition policy to use multiple extents on the disk for a VMFS datastore.  Multiple extents implies that more than one disk partition will be created on the disk for creating or increasing the capacity of a VMFS datastore. Multiple extents are needed when unpartitioned space is fragmented in the existing partition layout of the disk. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vmfs_extent** | [**List[HostDiskPartitionBlockRange]**](HostDiskPartitionBlockRange.md) | The block ranges to be used as extents in a VMFS datastore.  The first block range will be the head partition.  | 

## Example

```python
from vmware_vi.models.vmfs_datastore_multiple_extent_option import VmfsDatastoreMultipleExtentOption

# TODO update the JSON string below
json = "{}"
# create an instance of VmfsDatastoreMultipleExtentOption from a JSON string
vmfs_datastore_multiple_extent_option_instance = VmfsDatastoreMultipleExtentOption.from_json(json)
# print the JSON string representation of the object
print VmfsDatastoreMultipleExtentOption.to_json()

# convert the object into a dict
vmfs_datastore_multiple_extent_option_dict = vmfs_datastore_multiple_extent_option_instance.to_dict()
# create an instance of VmfsDatastoreMultipleExtentOption from a dict
vmfs_datastore_multiple_extent_option_form_dict = vmfs_datastore_multiple_extent_option.from_dict(vmfs_datastore_multiple_extent_option_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


