# ExpandVmfsExtentRequestType

The parameters of *HostStorageSystem.ExpandVmfsExtent*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vmfs_path** | **str** | The path of the VMFS to expand. See *FileSystemMountInfo*.  | 
**extent** | [**HostScsiDiskPartition**](HostScsiDiskPartition.md) |  | 

## Example

```python
from vmware_vi.models.expand_vmfs_extent_request_type import ExpandVmfsExtentRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of ExpandVmfsExtentRequestType from a JSON string
expand_vmfs_extent_request_type_instance = ExpandVmfsExtentRequestType.from_json(json)
# print the JSON string representation of the object
print ExpandVmfsExtentRequestType.to_json()

# convert the object into a dict
expand_vmfs_extent_request_type_dict = expand_vmfs_extent_request_type_instance.to_dict()
# create an instance of ExpandVmfsExtentRequestType from a dict
expand_vmfs_extent_request_type_form_dict = expand_vmfs_extent_request_type.from_dict(expand_vmfs_extent_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


