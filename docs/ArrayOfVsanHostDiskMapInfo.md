# ArrayOfVsanHostDiskMapInfo

A boxed array of *VsanHostDiskMapInfo*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[VsanHostDiskMapInfo]**](VsanHostDiskMapInfo.md) |  | 

## Example

```python
from vmware_vi.models.array_of_vsan_host_disk_map_info import ArrayOfVsanHostDiskMapInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfVsanHostDiskMapInfo from a JSON string
array_of_vsan_host_disk_map_info_instance = ArrayOfVsanHostDiskMapInfo.from_json(json)
# print the JSON string representation of the object
print ArrayOfVsanHostDiskMapInfo.to_json()

# convert the object into a dict
array_of_vsan_host_disk_map_info_dict = array_of_vsan_host_disk_map_info_instance.to_dict()
# create an instance of ArrayOfVsanHostDiskMapInfo from a dict
array_of_vsan_host_disk_map_info_form_dict = array_of_vsan_host_disk_map_info.from_dict(array_of_vsan_host_disk_map_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


