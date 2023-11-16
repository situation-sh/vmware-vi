# VsanHostDiskMapInfo

A DiskMapInfo represents a *VsanHostDiskMapping* and its corresponding runtime information.  See also *VsanHostConfigInfoStorageInfo*, *HostVsanSystem.InitializeDisks_Task*.  ***Since:*** vSphere API 6.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mapping** | [**VsanHostDiskMapping**](VsanHostDiskMapping.md) |  | 
**mounted** | **bool** | Indicates whether the *VsanHostDiskMapping* is mounted.  ***Since:*** vSphere API 6.0  | 

## Example

```python
from vmware_vi.models.vsan_host_disk_map_info import VsanHostDiskMapInfo

# TODO update the JSON string below
json = "{}"
# create an instance of VsanHostDiskMapInfo from a JSON string
vsan_host_disk_map_info_instance = VsanHostDiskMapInfo.from_json(json)
# print the JSON string representation of the object
print VsanHostDiskMapInfo.to_json()

# convert the object into a dict
vsan_host_disk_map_info_dict = vsan_host_disk_map_info_instance.to_dict()
# create an instance of VsanHostDiskMapInfo from a dict
vsan_host_disk_map_info_form_dict = vsan_host_disk_map_info.from_dict(vsan_host_disk_map_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


