# ArrayOfHostDiskPartitionLayout

A boxed array of *HostDiskPartitionLayout*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[HostDiskPartitionLayout]**](HostDiskPartitionLayout.md) |  | 

## Example

```python
from vmware_vi.models.array_of_host_disk_partition_layout import ArrayOfHostDiskPartitionLayout

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfHostDiskPartitionLayout from a JSON string
array_of_host_disk_partition_layout_instance = ArrayOfHostDiskPartitionLayout.from_json(json)
# print the JSON string representation of the object
print ArrayOfHostDiskPartitionLayout.to_json()

# convert the object into a dict
array_of_host_disk_partition_layout_dict = array_of_host_disk_partition_layout_instance.to_dict()
# create an instance of ArrayOfHostDiskPartitionLayout from a dict
array_of_host_disk_partition_layout_form_dict = array_of_host_disk_partition_layout.from_dict(array_of_host_disk_partition_layout_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


