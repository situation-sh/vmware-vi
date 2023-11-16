# RunVsanPhysicalDiskDiagnosticsRequestType

The parameters of *HostVsanInternalSystem.RunVsanPhysicalDiskDiagnostics*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**disks** | **List[str]** | List of VSAN disk UUIDs. If specified restricts the diagnostics run to VSAN disks present in the provided list.  | [optional] 

## Example

```python
from vmware_vi.models.run_vsan_physical_disk_diagnostics_request_type import RunVsanPhysicalDiskDiagnosticsRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of RunVsanPhysicalDiskDiagnosticsRequestType from a JSON string
run_vsan_physical_disk_diagnostics_request_type_instance = RunVsanPhysicalDiskDiagnosticsRequestType.from_json(json)
# print the JSON string representation of the object
print RunVsanPhysicalDiskDiagnosticsRequestType.to_json()

# convert the object into a dict
run_vsan_physical_disk_diagnostics_request_type_dict = run_vsan_physical_disk_diagnostics_request_type_instance.to_dict()
# create an instance of RunVsanPhysicalDiskDiagnosticsRequestType from a dict
run_vsan_physical_disk_diagnostics_request_type_form_dict = run_vsan_physical_disk_diagnostics_request_type.from_dict(run_vsan_physical_disk_diagnostics_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


