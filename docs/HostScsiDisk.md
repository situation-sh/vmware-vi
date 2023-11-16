# HostScsiDisk

This data object type describes a SCSI disk.  A SCSI disk contains a partition table which can be changed. To change a SCSI disk, use the device name and the partition specification.  See also *HostStorageSystem.RetrieveDiskPartitionInfo*, *HostStorageSystem.UpdateDiskPartitions*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**capacity** | [**HostDiskDimensionsLba**](HostDiskDimensionsLba.md) |  | 
**device_path** | **str** | The device path of the ScsiDisk.  This device path is a file path that can be opened to create partitions on the disk.  See also *HostStorageSystem.RetrieveDiskPartitionInfo*, *HostStorageSystem.UpdateDiskPartitions*.  | 
**ssd** | **bool** | Indicates whether the ScsiDisk is SSD backed.  If unset, the information whether the ScsiDisk is SSD backed is unknown.  ***Since:*** vSphere API 5.0  | [optional] 
**local_disk** | **bool** | Indicates whether the ScsiDisk is local.  If unset, the information whether the ScsiDisk is local is unknown.  ***Since:*** vSphere API 6.0  | [optional] 
**physical_location** | **List[str]** | The physical location of the ScsiDisk if can be determined, otherwise unset.  If the ScsiDisk is a logical drive, it should be the location of all constituent physical drives of the logical drive. If the ScsiDisk is a physical drive, it&#39;s an array of one element.  ***Since:*** vSphere API 6.0  | [optional] 
**emulated_dixdif_enabled** | **bool** | Indicates whether the ScsiDisk has emulated Data Integrity Extension (DIX) / Data Integrity Field (DIF) enabled.  If unset, the default value is false.  ***Since:*** vSphere API 6.0  | [optional] 
**vsan_disk_info** | [**VsanHostVsanDiskInfo**](VsanHostVsanDiskInfo.md) |  | [optional] 
**scsi_disk_type** | **str** | The type of disk drives.  See *ScsiDiskType_enum* for definitions of supported types.  ***Since:*** vSphere API 6.5  | [optional] 

## Example

```python
from vmware_vi.models.host_scsi_disk import HostScsiDisk

# TODO update the JSON string below
json = "{}"
# create an instance of HostScsiDisk from a JSON string
host_scsi_disk_instance = HostScsiDisk.from_json(json)
# print the JSON string representation of the object
print HostScsiDisk.to_json()

# convert the object into a dict
host_scsi_disk_dict = host_scsi_disk_instance.to_dict()
# create an instance of HostScsiDisk from a dict
host_scsi_disk_form_dict = host_scsi_disk.from_dict(host_scsi_disk_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


