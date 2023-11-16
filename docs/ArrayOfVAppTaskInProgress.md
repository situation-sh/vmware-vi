# ArrayOfVAppTaskInProgress

A boxed array of *VAppTaskInProgress*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[VAppTaskInProgress]**](VAppTaskInProgress.md) |  | 

## Example

```python
from vmware_vi.models.array_of_v_app_task_in_progress import ArrayOfVAppTaskInProgress

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfVAppTaskInProgress from a JSON string
array_of_v_app_task_in_progress_instance = ArrayOfVAppTaskInProgress.from_json(json)
# print the JSON string representation of the object
print ArrayOfVAppTaskInProgress.to_json()

# convert the object into a dict
array_of_v_app_task_in_progress_dict = array_of_v_app_task_in_progress_instance.to_dict()
# create an instance of ArrayOfVAppTaskInProgress from a dict
array_of_v_app_task_in_progress_form_dict = array_of_v_app_task_in_progress.from_dict(array_of_v_app_task_in_progress_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


