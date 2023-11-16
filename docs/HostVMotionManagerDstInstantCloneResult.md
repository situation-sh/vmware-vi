# HostVMotionManagerDstInstantCloneResult

The result of an InstantClone task.  Contains the dest VM id and timestamp values at the time of different operations.  ***Since:*** vSphere API 7.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dst_vm_id** | **int** | The destination VM ID of the InstantCloned VM.  ***Since:*** vSphere API 7.0  | [optional] 
**start_time** | **int** | Time stamp at the start of the InstantClone operation at the dest VM.  ***Since:*** vSphere API 7.0  | [optional] 
**cpt_load_time** | **int** | Time stamp when the destination VM starts cpt load.  ***Since:*** vSphere API 7.0  | [optional] 
**cpt_load_done_time** | **int** | Time stamp when the destination VM completes cpt load.  ***Since:*** vSphere API 7.0  | [optional] 
**replicate_mem_done_time** | **int** | Time stamp when the destination VM completes replicating memory.  ***Since:*** vSphere API 7.0  | [optional] 
**end_time** | **int** | Time stamp when the migration completes on the destination VM.  ***Since:*** vSphere API 7.0  | [optional] 
**cpt_xfer_time** | **int** | Device checkpoint stream time.  ***Since:*** vSphere API 7.0  | [optional] 
**cpt_cache_used** | **int** | Checkpoint cache size used.  ***Since:*** vSphere API 7.0  | [optional] 
**dev_cpt_stream_size** | **int** | Device checkpoint stream size.  ***Since:*** vSphere API 7.0  | [optional] 
**dev_cpt_stream_time** | **int** | Device checkpoint stream time.  ***Since:*** vSphere API 7.0  | [optional] 

## Example

```python
from vmware_vi.models.host_v_motion_manager_dst_instant_clone_result import HostVMotionManagerDstInstantCloneResult

# TODO update the JSON string below
json = "{}"
# create an instance of HostVMotionManagerDstInstantCloneResult from a JSON string
host_v_motion_manager_dst_instant_clone_result_instance = HostVMotionManagerDstInstantCloneResult.from_json(json)
# print the JSON string representation of the object
print HostVMotionManagerDstInstantCloneResult.to_json()

# convert the object into a dict
host_v_motion_manager_dst_instant_clone_result_dict = host_v_motion_manager_dst_instant_clone_result_instance.to_dict()
# create an instance of HostVMotionManagerDstInstantCloneResult from a dict
host_v_motion_manager_dst_instant_clone_result_form_dict = host_v_motion_manager_dst_instant_clone_result.from_dict(host_v_motion_manager_dst_instant_clone_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


