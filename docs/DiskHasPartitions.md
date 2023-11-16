# DiskHasPartitions

Fault used for disks which have existing, non-VSAN partitions.  See also *HostStorageSystem.UpdateDiskPartitions*, *HostVsanSystem.QueryDisksForVsan*.  ***Since:*** vSphere API 5.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.disk_has_partitions import DiskHasPartitions

# TODO update the JSON string below
json = "{}"
# create an instance of DiskHasPartitions from a JSON string
disk_has_partitions_instance = DiskHasPartitions.from_json(json)
# print the JSON string representation of the object
print DiskHasPartitions.to_json()

# convert the object into a dict
disk_has_partitions_dict = disk_has_partitions_instance.to_dict()
# create an instance of DiskHasPartitions from a dict
disk_has_partitions_form_dict = disk_has_partitions.from_dict(disk_has_partitions_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


