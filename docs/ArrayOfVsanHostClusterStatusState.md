# ArrayOfVsanHostClusterStatusState

A boxed array of *VsanHostClusterStatusState*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[VsanHostClusterStatusState]**](VsanHostClusterStatusState.md) |  | 

## Example

```python
from vmware_vi.models.array_of_vsan_host_cluster_status_state import ArrayOfVsanHostClusterStatusState

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfVsanHostClusterStatusState from a JSON string
array_of_vsan_host_cluster_status_state_instance = ArrayOfVsanHostClusterStatusState.from_json(json)
# print the JSON string representation of the object
print ArrayOfVsanHostClusterStatusState.to_json()

# convert the object into a dict
array_of_vsan_host_cluster_status_state_dict = array_of_vsan_host_cluster_status_state_instance.to_dict()
# create an instance of ArrayOfVsanHostClusterStatusState from a dict
array_of_vsan_host_cluster_status_state_form_dict = array_of_vsan_host_cluster_status_state.from_dict(array_of_vsan_host_cluster_status_state_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


