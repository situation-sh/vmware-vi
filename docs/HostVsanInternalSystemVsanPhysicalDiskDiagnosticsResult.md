# HostVsanInternalSystemVsanPhysicalDiskDiagnosticsResult

Result structure for a VSAN Physical Disk Diagnostics run.  Specifies the result of a single disk.  ***Since:*** vSphere API 5.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**disk_uuid** | **str** | VSAN Disk UUID of the checked disk.  ***Since:*** vSphere API 5.5  | 
**success** | **bool** | Indicates success or failure of object creation on the disk.  ***Since:*** vSphere API 5.5  | 
**failure_reason** | **str** | A failure reason type, in case of failure.  ***Since:*** vSphere API 5.5  | [optional] 

## Example

```python
from vmware_vi.models.host_vsan_internal_system_vsan_physical_disk_diagnostics_result import HostVsanInternalSystemVsanPhysicalDiskDiagnosticsResult

# TODO update the JSON string below
json = "{}"
# create an instance of HostVsanInternalSystemVsanPhysicalDiskDiagnosticsResult from a JSON string
host_vsan_internal_system_vsan_physical_disk_diagnostics_result_instance = HostVsanInternalSystemVsanPhysicalDiskDiagnosticsResult.from_json(json)
# print the JSON string representation of the object
print HostVsanInternalSystemVsanPhysicalDiskDiagnosticsResult.to_json()

# convert the object into a dict
host_vsan_internal_system_vsan_physical_disk_diagnostics_result_dict = host_vsan_internal_system_vsan_physical_disk_diagnostics_result_instance.to_dict()
# create an instance of HostVsanInternalSystemVsanPhysicalDiskDiagnosticsResult from a dict
host_vsan_internal_system_vsan_physical_disk_diagnostics_result_form_dict = host_vsan_internal_system_vsan_physical_disk_diagnostics_result.from_dict(host_vsan_internal_system_vsan_physical_disk_diagnostics_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


