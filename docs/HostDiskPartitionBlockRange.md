# HostDiskPartitionBlockRange

A BlockRange data object type describes a contiguous set of blocks on a disk.  A BlockRange may describe either a partition or unpartitioned (primordial) blocks on the disk. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**partition** | **int** | Partition number.  This number is a hint from the server indicating what the partition number for this block range is if the range corresponds to a partition. The partition number should correlate to the one in the partition specification. If sent back to the server, this property is ignored.  | [optional] 
**type** | **str** | The type of data in the partition.  See also *HostDiskPartitionAttributes.type*.  | 
**start** | [**HostDiskDimensionsLba**](HostDiskDimensionsLba.md) |  | 
**end** | [**HostDiskDimensionsLba**](HostDiskDimensionsLba.md) |  | 

## Example

```python
from vmware_vi.models.host_disk_partition_block_range import HostDiskPartitionBlockRange

# TODO update the JSON string below
json = "{}"
# create an instance of HostDiskPartitionBlockRange from a JSON string
host_disk_partition_block_range_instance = HostDiskPartitionBlockRange.from_json(json)
# print the JSON string representation of the object
print HostDiskPartitionBlockRange.to_json()

# convert the object into a dict
host_disk_partition_block_range_dict = host_disk_partition_block_range_instance.to_dict()
# create an instance of HostDiskPartitionBlockRange from a dict
host_disk_partition_block_range_form_dict = host_disk_partition_block_range.from_dict(host_disk_partition_block_range_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


