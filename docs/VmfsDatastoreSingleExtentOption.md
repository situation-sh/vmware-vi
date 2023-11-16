# VmfsDatastoreSingleExtentOption

Datastore addition policy to use a single extent on the disk for a VMFS datastore.  A single extent implies that one disk partition will be created on the disk for creating or increasing the capacity of a VMFS datastore. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vmfs_extent** | [**HostDiskPartitionBlockRange**](HostDiskPartitionBlockRange.md) |  | 

## Example

```python
from vmware_vi.models.vmfs_datastore_single_extent_option import VmfsDatastoreSingleExtentOption

# TODO update the JSON string below
json = "{}"
# create an instance of VmfsDatastoreSingleExtentOption from a JSON string
vmfs_datastore_single_extent_option_instance = VmfsDatastoreSingleExtentOption.from_json(json)
# print the JSON string representation of the object
print VmfsDatastoreSingleExtentOption.to_json()

# convert the object into a dict
vmfs_datastore_single_extent_option_dict = vmfs_datastore_single_extent_option_instance.to_dict()
# create an instance of VmfsDatastoreSingleExtentOption from a dict
vmfs_datastore_single_extent_option_form_dict = vmfs_datastore_single_extent_option.from_dict(vmfs_datastore_single_extent_option_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


