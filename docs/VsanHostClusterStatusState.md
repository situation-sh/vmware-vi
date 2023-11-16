# VsanHostClusterStatusState

Data object representing the VSAN node state for a host.  ***Since:*** vSphere API 5.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**state** | **str** | VSAN node state for this host.  See also *VsanHostNodeState_enum*.  ***Since:*** vSphere API 5.5  | 
**completion** | [**VsanHostClusterStatusStateCompletionEstimate**](VsanHostClusterStatusStateCompletionEstimate.md) |  | [optional] 

## Example

```python
from vmware_vi.models.vsan_host_cluster_status_state import VsanHostClusterStatusState

# TODO update the JSON string below
json = "{}"
# create an instance of VsanHostClusterStatusState from a JSON string
vsan_host_cluster_status_state_instance = VsanHostClusterStatusState.from_json(json)
# print the JSON string representation of the object
print VsanHostClusterStatusState.to_json()

# convert the object into a dict
vsan_host_cluster_status_state_dict = vsan_host_cluster_status_state_instance.to_dict()
# create an instance of VsanHostClusterStatusState from a dict
vsan_host_cluster_status_state_form_dict = vsan_host_cluster_status_state.from_dict(vsan_host_cluster_status_state_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


