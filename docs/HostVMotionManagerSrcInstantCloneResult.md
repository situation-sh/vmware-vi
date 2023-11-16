# HostVMotionManagerSrcInstantCloneResult

The result of an InstantClone InitiateSource task.  Contains the timestamp value at the time of different operations.  ***Since:*** vSphere API 7.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start_time** | **int** | Time stamp at the start of the InstantClone operation at the source VM.  ***Since:*** vSphere API 7.0  | [optional] 
**quiesce_time** | **int** | Time stamp when the source VM enters quiesce state.  ***Since:*** vSphere API 7.0  | [optional] 
**quiesce_done_time** | **int** | Time stamp when the source VM successfully quiesces.  ***Since:*** vSphere API 7.0  | [optional] 
**resume_done_time** | **int** | Time stamp when the source VM completes resuming.  ***Since:*** vSphere API 7.0  | [optional] 
**end_time** | **int** | Time stamp when the migration completes on the source VM.  ***Since:*** vSphere API 7.0  | [optional] 

## Example

```python
from vmware_vi.models.host_v_motion_manager_src_instant_clone_result import HostVMotionManagerSrcInstantCloneResult

# TODO update the JSON string below
json = "{}"
# create an instance of HostVMotionManagerSrcInstantCloneResult from a JSON string
host_v_motion_manager_src_instant_clone_result_instance = HostVMotionManagerSrcInstantCloneResult.from_json(json)
# print the JSON string representation of the object
print HostVMotionManagerSrcInstantCloneResult.to_json()

# convert the object into a dict
host_v_motion_manager_src_instant_clone_result_dict = host_v_motion_manager_src_instant_clone_result_instance.to_dict()
# create an instance of HostVMotionManagerSrcInstantCloneResult from a dict
host_v_motion_manager_src_instant_clone_result_form_dict = host_v_motion_manager_src_instant_clone_result.from_dict(host_v_motion_manager_src_instant_clone_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


