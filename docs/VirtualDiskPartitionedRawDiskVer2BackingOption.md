# VirtualDiskPartitionedRawDiskVer2BackingOption

The VirtualDiskOption.PartitionedRawDiskVer2BackingOption object type contains the available options when backing a virtual disk using one or more partitions on a physical disk device.  This backing is supported in VMware Server. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.virtual_disk_partitioned_raw_disk_ver2_backing_option import VirtualDiskPartitionedRawDiskVer2BackingOption

# TODO update the JSON string below
json = "{}"
# create an instance of VirtualDiskPartitionedRawDiskVer2BackingOption from a JSON string
virtual_disk_partitioned_raw_disk_ver2_backing_option_instance = VirtualDiskPartitionedRawDiskVer2BackingOption.from_json(json)
# print the JSON string representation of the object
print VirtualDiskPartitionedRawDiskVer2BackingOption.to_json()

# convert the object into a dict
virtual_disk_partitioned_raw_disk_ver2_backing_option_dict = virtual_disk_partitioned_raw_disk_ver2_backing_option_instance.to_dict()
# create an instance of VirtualDiskPartitionedRawDiskVer2BackingOption from a dict
virtual_disk_partitioned_raw_disk_ver2_backing_option_form_dict = virtual_disk_partitioned_raw_disk_ver2_backing_option.from_dict(virtual_disk_partitioned_raw_disk_ver2_backing_option_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


