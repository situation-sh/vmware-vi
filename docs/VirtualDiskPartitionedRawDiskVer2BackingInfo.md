# VirtualDiskPartitionedRawDiskVer2BackingInfo

This data object type contains information about backing a virtual disk using one or more partitions on a physical disk device.  This type of backing is supported for VMware Server. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**partition** | **List[int]** | Array of partition indexes.  This array identifies the partitions that are used on the physical disk drive.  | 

## Example

```python
from vmware_vi.models.virtual_disk_partitioned_raw_disk_ver2_backing_info import VirtualDiskPartitionedRawDiskVer2BackingInfo

# TODO update the JSON string below
json = "{}"
# create an instance of VirtualDiskPartitionedRawDiskVer2BackingInfo from a JSON string
virtual_disk_partitioned_raw_disk_ver2_backing_info_instance = VirtualDiskPartitionedRawDiskVer2BackingInfo.from_json(json)
# print the JSON string representation of the object
print VirtualDiskPartitionedRawDiskVer2BackingInfo.to_json()

# convert the object into a dict
virtual_disk_partitioned_raw_disk_ver2_backing_info_dict = virtual_disk_partitioned_raw_disk_ver2_backing_info_instance.to_dict()
# create an instance of VirtualDiskPartitionedRawDiskVer2BackingInfo from a dict
virtual_disk_partitioned_raw_disk_ver2_backing_info_form_dict = virtual_disk_partitioned_raw_disk_ver2_backing_info.from_dict(virtual_disk_partitioned_raw_disk_ver2_backing_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


