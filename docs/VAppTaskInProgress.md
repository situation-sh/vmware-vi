# VAppTaskInProgress

A specialized TaskInProgress when an operation is performed on a VM and it is failed due to a vApp-level operation is in progress.  For example, while the power-on sequence is executed on a vApp, individual power-on's of child VMs are failed.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.v_app_task_in_progress import VAppTaskInProgress

# TODO update the JSON string below
json = "{}"
# create an instance of VAppTaskInProgress from a JSON string
v_app_task_in_progress_instance = VAppTaskInProgress.from_json(json)
# print the JSON string representation of the object
print VAppTaskInProgress.to_json()

# convert the object into a dict
v_app_task_in_progress_dict = v_app_task_in_progress_instance.to_dict()
# create an instance of VAppTaskInProgress from a dict
v_app_task_in_progress_form_dict = v_app_task_in_progress.from_dict(v_app_task_in_progress_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


