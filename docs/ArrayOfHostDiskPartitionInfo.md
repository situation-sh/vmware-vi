# ArrayOfHostDiskPartitionInfo

A boxed array of *HostDiskPartitionInfo*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[HostDiskPartitionInfo]**](HostDiskPartitionInfo.md) |  | 

## Example

```python
from vmware_vi.models.array_of_host_disk_partition_info import ArrayOfHostDiskPartitionInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfHostDiskPartitionInfo from a JSON string
array_of_host_disk_partition_info_instance = ArrayOfHostDiskPartitionInfo.from_json(json)
# print the JSON string representation of the object
print ArrayOfHostDiskPartitionInfo.to_json()

# convert the object into a dict
array_of_host_disk_partition_info_dict = array_of_host_disk_partition_info_instance.to_dict()
# create an instance of ArrayOfHostDiskPartitionInfo from a dict
array_of_host_disk_partition_info_form_dict = array_of_host_disk_partition_info.from_dict(array_of_host_disk_partition_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


