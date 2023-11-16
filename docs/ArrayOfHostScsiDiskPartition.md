# ArrayOfHostScsiDiskPartition

A boxed array of *HostScsiDiskPartition*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[HostScsiDiskPartition]**](HostScsiDiskPartition.md) |  | 

## Example

```python
from vmware_vi.models.array_of_host_scsi_disk_partition import ArrayOfHostScsiDiskPartition

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfHostScsiDiskPartition from a JSON string
array_of_host_scsi_disk_partition_instance = ArrayOfHostScsiDiskPartition.from_json(json)
# print the JSON string representation of the object
print ArrayOfHostScsiDiskPartition.to_json()

# convert the object into a dict
array_of_host_scsi_disk_partition_dict = array_of_host_scsi_disk_partition_instance.to_dict()
# create an instance of ArrayOfHostScsiDiskPartition from a dict
array_of_host_scsi_disk_partition_form_dict = array_of_host_scsi_disk_partition.from_dict(array_of_host_scsi_disk_partition_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


