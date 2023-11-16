# ComputeDiskPartitionInfoRequestType

The parameters of *HostStorageSystem.ComputeDiskPartitionInfo*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**device_path** | **str** | The name of the device path for the specific disk.  | 
**layout** | [**HostDiskPartitionLayout**](HostDiskPartitionLayout.md) |  | 
**partition_format** | **str** | Specifies the desired partition format to be computed from the block range. If partitionFormat is not specified, the existing partitionFormat on disk is used, if the disk is not blank and mbr otherwise.  | [optional] 

## Example

```python
from vmware_vi.models.compute_disk_partition_info_request_type import ComputeDiskPartitionInfoRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of ComputeDiskPartitionInfoRequestType from a JSON string
compute_disk_partition_info_request_type_instance = ComputeDiskPartitionInfoRequestType.from_json(json)
# print the JSON string representation of the object
print ComputeDiskPartitionInfoRequestType.to_json()

# convert the object into a dict
compute_disk_partition_info_request_type_dict = compute_disk_partition_info_request_type_instance.to_dict()
# create an instance of ComputeDiskPartitionInfoRequestType from a dict
compute_disk_partition_info_request_type_form_dict = compute_disk_partition_info_request_type.from_dict(compute_disk_partition_info_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


