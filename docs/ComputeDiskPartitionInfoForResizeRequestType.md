# ComputeDiskPartitionInfoForResizeRequestType

The parameters of *HostStorageSystem.ComputeDiskPartitionInfoForResize*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**partition** | [**HostScsiDiskPartition**](HostScsiDiskPartition.md) |  | 
**block_range** | [**HostDiskPartitionBlockRange**](HostDiskPartitionBlockRange.md) |  | 
**partition_format** | **str** | Specifies the desired partition format to be computed from the block range. If partitionFormat is not specified, the existing partitionFormat on disk is used, if the disk is not blank and mbr otherwise.  | [optional] 

## Example

```python
from vmware_vi.models.compute_disk_partition_info_for_resize_request_type import ComputeDiskPartitionInfoForResizeRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of ComputeDiskPartitionInfoForResizeRequestType from a JSON string
compute_disk_partition_info_for_resize_request_type_instance = ComputeDiskPartitionInfoForResizeRequestType.from_json(json)
# print the JSON string representation of the object
print ComputeDiskPartitionInfoForResizeRequestType.to_json()

# convert the object into a dict
compute_disk_partition_info_for_resize_request_type_dict = compute_disk_partition_info_for_resize_request_type_instance.to_dict()
# create an instance of ComputeDiskPartitionInfoForResizeRequestType from a dict
compute_disk_partition_info_for_resize_request_type_form_dict = compute_disk_partition_info_for_resize_request_type.from_dict(compute_disk_partition_info_for_resize_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


