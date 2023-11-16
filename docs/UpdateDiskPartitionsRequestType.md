# UpdateDiskPartitionsRequestType

The parameters of *HostStorageSystem.UpdateDiskPartitions*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**device_path** | **str** | The name of the device path for the specific disk.  | 
**spec** | [**HostDiskPartitionSpec**](HostDiskPartitionSpec.md) |  | 

## Example

```python
from vmware_vi.models.update_disk_partitions_request_type import UpdateDiskPartitionsRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateDiskPartitionsRequestType from a JSON string
update_disk_partitions_request_type_instance = UpdateDiskPartitionsRequestType.from_json(json)
# print the JSON string representation of the object
print UpdateDiskPartitionsRequestType.to_json()

# convert the object into a dict
update_disk_partitions_request_type_dict = update_disk_partitions_request_type_instance.to_dict()
# create an instance of UpdateDiskPartitionsRequestType from a dict
update_disk_partitions_request_type_form_dict = update_disk_partitions_request_type.from_dict(update_disk_partitions_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


