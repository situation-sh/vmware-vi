# VsanHostRuntimeInfoDiskIssue

Data structure of reporting a disk issue.  ***Since:*** vSphere API 5.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**disk_id** | **str** | Disk uuid, @see vim.host.ScsiLun#uuid  ***Since:*** vSphere API 5.5  | 
**issue** | **str** | Type of issue  See also *VsanDiskIssueType_enum*.  ***Since:*** vSphere API 5.5  | 

## Example

```python
from vmware_vi.models.vsan_host_runtime_info_disk_issue import VsanHostRuntimeInfoDiskIssue

# TODO update the JSON string below
json = "{}"
# create an instance of VsanHostRuntimeInfoDiskIssue from a JSON string
vsan_host_runtime_info_disk_issue_instance = VsanHostRuntimeInfoDiskIssue.from_json(json)
# print the JSON string representation of the object
print VsanHostRuntimeInfoDiskIssue.to_json()

# convert the object into a dict
vsan_host_runtime_info_disk_issue_dict = vsan_host_runtime_info_disk_issue_instance.to_dict()
# create an instance of VsanHostRuntimeInfoDiskIssue from a dict
vsan_host_runtime_info_disk_issue_form_dict = vsan_host_runtime_info_disk_issue.from_dict(vsan_host_runtime_info_disk_issue_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


