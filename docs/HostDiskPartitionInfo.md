# HostDiskPartitionInfo

Information about the partitions on a disk.  A DiskPartitionInfo object provides two different views into the partitions on a disk: - A detailed specification that is used to create the partition   table. - A convenient view that shows the allocations   of blocks as a contiguous sequence of block ranges.    See also *HostStorageSystem.RetrieveDiskPartitionInfo*, *HostStorageSystem.ComputeDiskPartitionInfo*, *HostStorageSystem.UpdateDiskPartitions*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**device_name** | **str** | The device name of the disk to which this partition information corresponds.  | 
**spec** | [**HostDiskPartitionSpec**](HostDiskPartitionSpec.md) |  | 
**layout** | [**HostDiskPartitionLayout**](HostDiskPartitionLayout.md) |  | 

## Example

```python
from vmware_vi.models.host_disk_partition_info import HostDiskPartitionInfo

# TODO update the JSON string below
json = "{}"
# create an instance of HostDiskPartitionInfo from a JSON string
host_disk_partition_info_instance = HostDiskPartitionInfo.from_json(json)
# print the JSON string representation of the object
print HostDiskPartitionInfo.to_json()

# convert the object into a dict
host_disk_partition_info_dict = host_disk_partition_info_instance.to_dict()
# create an instance of HostDiskPartitionInfo from a dict
host_disk_partition_info_form_dict = host_disk_partition_info.from_dict(host_disk_partition_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


