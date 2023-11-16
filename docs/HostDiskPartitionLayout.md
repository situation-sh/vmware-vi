# HostDiskPartitionLayout

This data object type describes the disk partition layout specified as a list of ordered BlockRanges.  This view of the disk partitions shows the data on the disk as a contiguous set of BlockRanges. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total** | [**HostDiskDimensionsLba**](HostDiskDimensionsLba.md) |  | [optional] 
**partition** | [**List[HostDiskPartitionBlockRange]**](HostDiskPartitionBlockRange.md) | List of block ranges on the disk.  | 

## Example

```python
from vmware_vi.models.host_disk_partition_layout import HostDiskPartitionLayout

# TODO update the JSON string below
json = "{}"
# create an instance of HostDiskPartitionLayout from a JSON string
host_disk_partition_layout_instance = HostDiskPartitionLayout.from_json(json)
# print the JSON string representation of the object
print HostDiskPartitionLayout.to_json()

# convert the object into a dict
host_disk_partition_layout_dict = host_disk_partition_layout_instance.to_dict()
# create an instance of HostDiskPartitionLayout from a dict
host_disk_partition_layout_form_dict = host_disk_partition_layout.from_dict(host_disk_partition_layout_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


