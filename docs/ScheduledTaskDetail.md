# ScheduledTaskDetail

Descriptive detail for each scheduler type. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**frequency** | **str** | Scheduler frequency description.  | 

## Example

```python
from vmware_vi.models.scheduled_task_detail import ScheduledTaskDetail

# TODO update the JSON string below
json = "{}"
# create an instance of ScheduledTaskDetail from a JSON string
scheduled_task_detail_instance = ScheduledTaskDetail.from_json(json)
# print the JSON string representation of the object
print ScheduledTaskDetail.to_json()

# convert the object into a dict
scheduled_task_detail_dict = scheduled_task_detail_instance.to_dict()
# create an instance of ScheduledTaskDetail from a dict
scheduled_task_detail_form_dict = scheduled_task_detail.from_dict(scheduled_task_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


