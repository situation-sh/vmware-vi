# HostDiskPartitionSpec

This data object type describes the disk partition table specification used to configure the partitions on a disk.  This data object represents the fundamental data needed to specify a partition table. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**partition_format** | **str** | Partition format type on the disk.  ***Since:*** vSphere API 5.0  | [optional] 
**chs** | [**HostDiskDimensionsChs**](HostDiskDimensionsChs.md) |  | [optional] 
**total_sectors** | **int** | Disk dimensions expressed in total number of 512-byte sectors.  | [optional] 
**partition** | [**List[HostDiskPartitionAttributes]**](HostDiskPartitionAttributes.md) | List of partitions on the disk.  | [optional] 

## Example

```python
from vmware_vi.models.host_disk_partition_spec import HostDiskPartitionSpec

# TODO update the JSON string below
json = "{}"
# create an instance of HostDiskPartitionSpec from a JSON string
host_disk_partition_spec_instance = HostDiskPartitionSpec.from_json(json)
# print the JSON string representation of the object
print HostDiskPartitionSpec.to_json()

# convert the object into a dict
host_disk_partition_spec_dict = host_disk_partition_spec_instance.to_dict()
# create an instance of HostDiskPartitionSpec from a dict
host_disk_partition_spec_form_dict = host_disk_partition_spec.from_dict(host_disk_partition_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


