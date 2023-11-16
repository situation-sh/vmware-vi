# ArrayOfHostDiskMappingPartitionOption

A boxed array of *HostDiskMappingPartitionOption*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[HostDiskMappingPartitionOption]**](HostDiskMappingPartitionOption.md) |  | 

## Example

```python
from vmware_vi.models.array_of_host_disk_mapping_partition_option import ArrayOfHostDiskMappingPartitionOption

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfHostDiskMappingPartitionOption from a JSON string
array_of_host_disk_mapping_partition_option_instance = ArrayOfHostDiskMappingPartitionOption.from_json(json)
# print the JSON string representation of the object
print ArrayOfHostDiskMappingPartitionOption.to_json()

# convert the object into a dict
array_of_host_disk_mapping_partition_option_dict = array_of_host_disk_mapping_partition_option_instance.to_dict()
# create an instance of ArrayOfHostDiskMappingPartitionOption from a dict
array_of_host_disk_mapping_partition_option_form_dict = array_of_host_disk_mapping_partition_option.from_dict(array_of_host_disk_mapping_partition_option_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


