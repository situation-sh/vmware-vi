# VsanHostClusterStatusStateCompletionEstimate

Estimated completion status for transitory node states.  See also *VsanHostNodeState_enum*.  ***Since:*** vSphere API 5.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**complete_time** | **datetime** | Estimated time of completion.  ***Since:*** vSphere API 5.5  | [optional] 
**percent_complete** | **int** | Estimated percent of completion as a value in the range \\[0, 100\\].  ***Since:*** vSphere API 5.5  | [optional] 

## Example

```python
from vmware_vi.models.vsan_host_cluster_status_state_completion_estimate import VsanHostClusterStatusStateCompletionEstimate

# TODO update the JSON string below
json = "{}"
# create an instance of VsanHostClusterStatusStateCompletionEstimate from a JSON string
vsan_host_cluster_status_state_completion_estimate_instance = VsanHostClusterStatusStateCompletionEstimate.from_json(json)
# print the JSON string representation of the object
print VsanHostClusterStatusStateCompletionEstimate.to_json()

# convert the object into a dict
vsan_host_cluster_status_state_completion_estimate_dict = vsan_host_cluster_status_state_completion_estimate_instance.to_dict()
# create an instance of VsanHostClusterStatusStateCompletionEstimate from a dict
vsan_host_cluster_status_state_completion_estimate_form_dict = vsan_host_cluster_status_state_completion_estimate.from_dict(vsan_host_cluster_status_state_completion_estimate_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


