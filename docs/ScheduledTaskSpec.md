# ScheduledTaskSpec

Parameters for scheduled task creation. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the scheduled task.  | 
**description** | **str** | Description of the scheduled task.  | 
**enabled** | **bool** | Flag to indicate whether the scheduled task is enabled or disabled.  | 
**scheduler** | [**TaskScheduler**](TaskScheduler.md) |  | 
**action** | [**Action**](Action.md) |  | 
**notification** | **str** | The email notification.  If not set, this property is set to empty string, indicating no notification.  | [optional] 

## Example

```python
from vmware_vi.models.scheduled_task_spec import ScheduledTaskSpec

# TODO update the JSON string below
json = "{}"
# create an instance of ScheduledTaskSpec from a JSON string
scheduled_task_spec_instance = ScheduledTaskSpec.from_json(json)
# print the JSON string representation of the object
print ScheduledTaskSpec.to_json()

# convert the object into a dict
scheduled_task_spec_dict = scheduled_task_spec_instance.to_dict()
# create an instance of ScheduledTaskSpec from a dict
scheduled_task_spec_form_dict = scheduled_task_spec.from_dict(scheduled_task_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


