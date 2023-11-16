# ArrayOfDiskHasPartitions

A boxed array of *DiskHasPartitions*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[DiskHasPartitions]**](DiskHasPartitions.md) |  | 

## Example

```python
from vmware_vi.models.array_of_disk_has_partitions import ArrayOfDiskHasPartitions

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfDiskHasPartitions from a JSON string
array_of_disk_has_partitions_instance = ArrayOfDiskHasPartitions.from_json(json)
# print the JSON string representation of the object
print ArrayOfDiskHasPartitions.to_json()

# convert the object into a dict
array_of_disk_has_partitions_dict = array_of_disk_has_partitions_instance.to_dict()
# create an instance of ArrayOfDiskHasPartitions from a dict
array_of_disk_has_partitions_form_dict = array_of_disk_has_partitions.from_dict(array_of_disk_has_partitions_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


