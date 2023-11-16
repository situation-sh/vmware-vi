# RetrieveDiskPartitionInfoRequestType

The parameters of *HostStorageSystem.RetrieveDiskPartitionInfo*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**device_path** | **List[str]** | An array of device path names that identify disks. See *ScsiDisk*.  | 

## Example

```python
from vmware_vi.models.retrieve_disk_partition_info_request_type import RetrieveDiskPartitionInfoRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of RetrieveDiskPartitionInfoRequestType from a JSON string
retrieve_disk_partition_info_request_type_instance = RetrieveDiskPartitionInfoRequestType.from_json(json)
# print the JSON string representation of the object
print RetrieveDiskPartitionInfoRequestType.to_json()

# convert the object into a dict
retrieve_disk_partition_info_request_type_dict = retrieve_disk_partition_info_request_type_instance.to_dict()
# create an instance of RetrieveDiskPartitionInfoRequestType from a dict
retrieve_disk_partition_info_request_type_form_dict = retrieve_disk_partition_info_request_type.from_dict(retrieve_disk_partition_info_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


