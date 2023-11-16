# VsanHostRuntimeInfo

This data object contains VSAN cluster runtime information from the perspective of the host in question.  This data object is used to represent read-only state whose values may change during operation.  ***Since:*** vSphere API 5.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**membership_list** | [**List[VsanHostMembershipInfo]**](VsanHostMembershipInfo.md) | This property reports host membership information.  ***Since:*** vSphere API 5.5  | [optional] 
**disk_issues** | [**List[VsanHostRuntimeInfoDiskIssue]**](VsanHostRuntimeInfoDiskIssue.md) | List of disk issues detected on this host.  To retrieve more information on the issues, use *HostVsanSystem.QueryDisksForVsan*.  ***Since:*** vSphere API 5.5  | [optional] 
**access_gen_no** | **int** | Generation number tracking object accessibility.  ***Since:*** vSphere API 5.5  | [optional] 

## Example

```python
from vmware_vi.models.vsan_host_runtime_info import VsanHostRuntimeInfo

# TODO update the JSON string below
json = "{}"
# create an instance of VsanHostRuntimeInfo from a JSON string
vsan_host_runtime_info_instance = VsanHostRuntimeInfo.from_json(json)
# print the JSON string representation of the object
print VsanHostRuntimeInfo.to_json()

# convert the object into a dict
vsan_host_runtime_info_dict = vsan_host_runtime_info_instance.to_dict()
# create an instance of VsanHostRuntimeInfo from a dict
vsan_host_runtime_info_form_dict = vsan_host_runtime_info.from_dict(vsan_host_runtime_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


