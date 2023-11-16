# TaskFilterSpecTimeOption

A boxed *TaskFilterSpecTimeOption_enum*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**TaskFilterSpecTimeOptionEnum**](TaskFilterSpecTimeOptionEnum.md) |  | 

## Example

```python
from vmware_vi.models.task_filter_spec_time_option import TaskFilterSpecTimeOption

# TODO update the JSON string below
json = "{}"
# create an instance of TaskFilterSpecTimeOption from a JSON string
task_filter_spec_time_option_instance = TaskFilterSpecTimeOption.from_json(json)
# print the JSON string representation of the object
print TaskFilterSpecTimeOption.to_json()

# convert the object into a dict
task_filter_spec_time_option_dict = task_filter_spec_time_option_instance.to_dict()
# create an instance of TaskFilterSpecTimeOption from a dict
task_filter_spec_time_option_form_dict = task_filter_spec_time_option.from_dict(task_filter_spec_time_option_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


