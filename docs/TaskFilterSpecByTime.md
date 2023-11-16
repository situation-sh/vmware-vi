# TaskFilterSpecByTime

This data object type specifies a time range used to filter task history. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**time_type** | [**TaskFilterSpecTimeOptionEnum**](TaskFilterSpecTimeOptionEnum.md) |  | 
**begin_time** | **datetime** | The beginning of the time range.  If this property is not specified, then tasks are collected from the earliest time in the database.  When this property is specified, the time type field must also be specified.  | [optional] 
**end_time** | **datetime** | The end of the time range.  If this property is not specified, then tasks are collected up to the latest time in the database.  When this property is specified, the time type field must also be specified.  | [optional] 

## Example

```python
from vmware_vi.models.task_filter_spec_by_time import TaskFilterSpecByTime

# TODO update the JSON string below
json = "{}"
# create an instance of TaskFilterSpecByTime from a JSON string
task_filter_spec_by_time_instance = TaskFilterSpecByTime.from_json(json)
# print the JSON string representation of the object
print TaskFilterSpecByTime.to_json()

# convert the object into a dict
task_filter_spec_by_time_dict = task_filter_spec_by_time_instance.to_dict()
# create an instance of TaskFilterSpecByTime from a dict
task_filter_spec_by_time_form_dict = task_filter_spec_by_time.from_dict(task_filter_spec_by_time_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


