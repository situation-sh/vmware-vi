# HostDiskMappingPartitionInfo

The PhysicalPartitionInfo data class. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Partition name.  | 
**file_system** | **str** | Filesystem, if the partition is formatted.  | 
**capacity_in_kb** | **int** | Partition capacity, in KB.  | 

## Example

```python
from vmware_vi.models.host_disk_mapping_partition_info import HostDiskMappingPartitionInfo

# TODO update the JSON string below
json = "{}"
# create an instance of HostDiskMappingPartitionInfo from a JSON string
host_disk_mapping_partition_info_instance = HostDiskMappingPartitionInfo.from_json(json)
# print the JSON string representation of the object
print HostDiskMappingPartitionInfo.to_json()

# convert the object into a dict
host_disk_mapping_partition_info_dict = host_disk_mapping_partition_info_instance.to_dict()
# create an instance of HostDiskMappingPartitionInfo from a dict
host_disk_mapping_partition_info_form_dict = host_disk_mapping_partition_info.from_dict(host_disk_mapping_partition_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


