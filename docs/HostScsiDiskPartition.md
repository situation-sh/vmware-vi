# HostScsiDiskPartition

This data object type describes the specification of a Disk partition. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**disk_name** | **str** | The SCSI disk device on which a VMware File System (VMFS) extent resides.  See also *HostScsiDisk*, *ScsiLun.canonicalName*.  | 
**partition** | **int** | The partition number of the partition on the ScsiDisk.  | 

## Example

```python
from vmware_vi.models.host_scsi_disk_partition import HostScsiDiskPartition

# TODO update the JSON string below
json = "{}"
# create an instance of HostScsiDiskPartition from a JSON string
host_scsi_disk_partition_instance = HostScsiDiskPartition.from_json(json)
# print the JSON string representation of the object
print HostScsiDiskPartition.to_json()

# convert the object into a dict
host_scsi_disk_partition_dict = host_scsi_disk_partition_instance.to_dict()
# create an instance of HostScsiDiskPartition from a dict
host_scsi_disk_partition_form_dict = host_scsi_disk_partition.from_dict(host_scsi_disk_partition_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


