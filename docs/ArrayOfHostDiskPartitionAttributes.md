# ArrayOfHostDiskPartitionAttributes

A boxed array of *HostDiskPartitionAttributes*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[HostDiskPartitionAttributes]**](HostDiskPartitionAttributes.md) |  | 

## Example

```python
from vmware_vi.models.array_of_host_disk_partition_attributes import ArrayOfHostDiskPartitionAttributes

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfHostDiskPartitionAttributes from a JSON string
array_of_host_disk_partition_attributes_instance = ArrayOfHostDiskPartitionAttributes.from_json(json)
# print the JSON string representation of the object
print ArrayOfHostDiskPartitionAttributes.to_json()

# convert the object into a dict
array_of_host_disk_partition_attributes_dict = array_of_host_disk_partition_attributes_instance.to_dict()
# create an instance of ArrayOfHostDiskPartitionAttributes from a dict
array_of_host_disk_partition_attributes_form_dict = array_of_host_disk_partition_attributes.from_dict(array_of_host_disk_partition_attributes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


