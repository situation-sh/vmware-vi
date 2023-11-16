# AttachVmfsExtentRequestType

The parameters of *HostStorageSystem.AttachVmfsExtent*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vmfs_path** | **str** | The path of the VMFS to extend. See *FileSystemMountInfo*.  | 
**extent** | [**HostScsiDiskPartition**](HostScsiDiskPartition.md) |  | 

## Example

```python
from vmware_vi.models.attach_vmfs_extent_request_type import AttachVmfsExtentRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of AttachVmfsExtentRequestType from a JSON string
attach_vmfs_extent_request_type_instance = AttachVmfsExtentRequestType.from_json(json)
# print the JSON string representation of the object
print AttachVmfsExtentRequestType.to_json()

# convert the object into a dict
attach_vmfs_extent_request_type_dict = attach_vmfs_extent_request_type_instance.to_dict()
# create an instance of AttachVmfsExtentRequestType from a dict
attach_vmfs_extent_request_type_form_dict = attach_vmfs_extent_request_type.from_dict(attach_vmfs_extent_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


