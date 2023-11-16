# VsanHostDiskMapResult

A DiskMapResult represents the result of an operation performed on the set of disks in a *VsanHostDiskMapping*.  See also *HostVsanSystem.InitializeDisks_Task*, *HostVsanSystem.UpdateVsan_Task*.  ***Since:*** vSphere API 5.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mapping** | [**VsanHostDiskMapping**](VsanHostDiskMapping.md) |  | 
**disk_result** | [**List[VsanHostDiskResult]**](VsanHostDiskResult.md) | List of results for each disk in the mapping.  ***Since:*** vSphere API 5.5  | [optional] 
**error** | [**MethodFault**](MethodFault.md) |  | [optional] 

## Example

```python
from vmware_vi.models.vsan_host_disk_map_result import VsanHostDiskMapResult

# TODO update the JSON string below
json = "{}"
# create an instance of VsanHostDiskMapResult from a JSON string
vsan_host_disk_map_result_instance = VsanHostDiskMapResult.from_json(json)
# print the JSON string representation of the object
print VsanHostDiskMapResult.to_json()

# convert the object into a dict
vsan_host_disk_map_result_dict = vsan_host_disk_map_result_instance.to_dict()
# create an instance of VsanHostDiskMapResult from a dict
vsan_host_disk_map_result_form_dict = vsan_host_disk_map_result.from_dict(vsan_host_disk_map_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


