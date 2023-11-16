# TaskFilterSpecByUsername

This data object type enables you to filter task history according to the users who performed the tasks. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**system_user** | **bool** | Whether or not to filter by system user.  If set to true, filters for system user event.  | 
**user_list** | **List[str]** | Specifies the username list to use in the filter.  If not set, then all regular user tasks are collected.  | [optional] 

## Example

```python
from vmware_vi.models.task_filter_spec_by_username import TaskFilterSpecByUsername

# TODO update the JSON string below
json = "{}"
# create an instance of TaskFilterSpecByUsername from a JSON string
task_filter_spec_by_username_instance = TaskFilterSpecByUsername.from_json(json)
# print the JSON string representation of the object
print TaskFilterSpecByUsername.to_json()

# convert the object into a dict
task_filter_spec_by_username_dict = task_filter_spec_by_username_instance.to_dict()
# create an instance of TaskFilterSpecByUsername from a dict
task_filter_spec_by_username_form_dict = task_filter_spec_by_username.from_dict(task_filter_spec_by_username_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


