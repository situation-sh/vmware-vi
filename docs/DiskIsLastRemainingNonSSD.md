# DiskIsLastRemainingNonSSD

Fault thrown for the case that an attempt is made to delete the last *VsanHostDiskMapping.nonSsd* from a *VsanHostDiskMapping*.  See also *HostVsanSystem.RemoveDisk_Task*, *HostVsanSystem.RemoveDiskMapping_Task*.  ***Since:*** vSphere API 5.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.disk_is_last_remaining_non_ssd import DiskIsLastRemainingNonSSD

# TODO update the JSON string below
json = "{}"
# create an instance of DiskIsLastRemainingNonSSD from a JSON string
disk_is_last_remaining_non_ssd_instance = DiskIsLastRemainingNonSSD.from_json(json)
# print the JSON string representation of the object
print DiskIsLastRemainingNonSSD.to_json()

# convert the object into a dict
disk_is_last_remaining_non_ssd_dict = disk_is_last_remaining_non_ssd_instance.to_dict()
# create an instance of DiskIsLastRemainingNonSSD from a dict
disk_is_last_remaining_non_ssd_form_dict = disk_is_last_remaining_non_ssd.from_dict(disk_is_last_remaining_non_ssd_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


