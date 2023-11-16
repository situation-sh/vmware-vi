# ArrayOfHostDiskPartitionBlockRange

A boxed array of *HostDiskPartitionBlockRange*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[HostDiskPartitionBlockRange]**](HostDiskPartitionBlockRange.md) |  | 

## Example

```python
from vmware_vi.models.array_of_host_disk_partition_block_range import ArrayOfHostDiskPartitionBlockRange

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfHostDiskPartitionBlockRange from a JSON string
array_of_host_disk_partition_block_range_instance = ArrayOfHostDiskPartitionBlockRange.from_json(json)
# print the JSON string representation of the object
print ArrayOfHostDiskPartitionBlockRange.to_json()

# convert the object into a dict
array_of_host_disk_partition_block_range_dict = array_of_host_disk_partition_block_range_instance.to_dict()
# create an instance of ArrayOfHostDiskPartitionBlockRange from a dict
array_of_host_disk_partition_block_range_form_dict = array_of_host_disk_partition_block_range.from_dict(array_of_host_disk_partition_block_range_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


