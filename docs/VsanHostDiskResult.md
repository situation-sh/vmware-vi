# VsanHostDiskResult

A DiskResult represents the result of VSAN configuration operation on a *HostScsiDisk*, and its current eligibility state for use by the VSAN service.  See also *HostVsanSystem.QueryDisksForVsan*, *HostVsanSystem.UpdateVsan_Task*, *VsanHostDiskResultState_enum*.  ***Since:*** vSphere API 5.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**disk** | [**HostScsiDisk**](HostScsiDisk.md) |  | 
**state** | **str** | State of the disk for this result.  See also *VsanHostDiskResultState_enum*.  ***Since:*** vSphere API 5.5  | 
**vsan_uuid** | **str** | VSAN disk UUID in case this disk is a VSAN disk.  ***Since:*** vSphere API 5.5  | [optional] 
**error** | [**MethodFault**](MethodFault.md) |  | [optional] 
**degraded** | **bool** | Indicates whether the disk is degraded in VSAN performance.  If set, indicates the disk performance is degraded in VSAN If unset, it is unknown whether the disk performance is degraded in VSAN.  ***Since:*** vSphere API 6.0  | [optional] 

## Example

```python
from vmware_vi.models.vsan_host_disk_result import VsanHostDiskResult

# TODO update the JSON string below
json = "{}"
# create an instance of VsanHostDiskResult from a JSON string
vsan_host_disk_result_instance = VsanHostDiskResult.from_json(json)
# print the JSON string representation of the object
print VsanHostDiskResult.to_json()

# convert the object into a dict
vsan_host_disk_result_dict = vsan_host_disk_result_instance.to_dict()
# create an instance of VsanHostDiskResult from a dict
vsan_host_disk_result_form_dict = vsan_host_disk_result.from_dict(vsan_host_disk_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


