# VsanHostVsanDiskInfo

A VsanDiskInfo represents the additional detailed information of a ScsiDisk used by VSAN, to map physical disk to VSAN disk.  See also *HostScsiDisk*.  ***Since:*** vSphere API 6.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vsan_uuid** | **str** | Disk UUID in VSAN  ***Since:*** vSphere API 6.0  | 
**format_version** | **int** | VSAN file system version number  ***Since:*** vSphere API 6.0  | 

## Example

```python
from vmware_vi.models.vsan_host_vsan_disk_info import VsanHostVsanDiskInfo

# TODO update the JSON string below
json = "{}"
# create an instance of VsanHostVsanDiskInfo from a JSON string
vsan_host_vsan_disk_info_instance = VsanHostVsanDiskInfo.from_json(json)
# print the JSON string representation of the object
print VsanHostVsanDiskInfo.to_json()

# convert the object into a dict
vsan_host_vsan_disk_info_dict = vsan_host_vsan_disk_info_instance.to_dict()
# create an instance of VsanHostVsanDiskInfo from a dict
vsan_host_vsan_disk_info_form_dict = vsan_host_vsan_disk_info.from_dict(vsan_host_vsan_disk_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


