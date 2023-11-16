# HostDiskMappingPartitionOption

The PhysicalPartitionOption data class contains the options for a partition on a physical disk. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Partition name.  | 
**file_system** | **str** | File system, if the partition is formatted.  | 
**capacity_in_kb** | **int** | Partition capacity, in KB.  | 

## Example

```python
from vmware_vi.models.host_disk_mapping_partition_option import HostDiskMappingPartitionOption

# TODO update the JSON string below
json = "{}"
# create an instance of HostDiskMappingPartitionOption from a JSON string
host_disk_mapping_partition_option_instance = HostDiskMappingPartitionOption.from_json(json)
# print the JSON string representation of the object
print HostDiskMappingPartitionOption.to_json()

# convert the object into a dict
host_disk_mapping_partition_option_dict = host_disk_mapping_partition_option_instance.to_dict()
# create an instance of HostDiskMappingPartitionOption from a dict
host_disk_mapping_partition_option_form_dict = host_disk_mapping_partition_option.from_dict(host_disk_mapping_partition_option_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


