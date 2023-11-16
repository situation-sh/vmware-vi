# ArrayOfTaskFilterSpecTimeOption

A boxed array of *TaskFilterSpecTimeOption_enum*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[TaskFilterSpecTimeOptionEnum]**](TaskFilterSpecTimeOptionEnum.md) |  | 

## Example

```python
from vmware_vi.models.array_of_task_filter_spec_time_option import ArrayOfTaskFilterSpecTimeOption

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfTaskFilterSpecTimeOption from a JSON string
array_of_task_filter_spec_time_option_instance = ArrayOfTaskFilterSpecTimeOption.from_json(json)
# print the JSON string representation of the object
print ArrayOfTaskFilterSpecTimeOption.to_json()

# convert the object into a dict
array_of_task_filter_spec_time_option_dict = array_of_task_filter_spec_time_option_instance.to_dict()
# create an instance of ArrayOfTaskFilterSpecTimeOption from a dict
array_of_task_filter_spec_time_option_form_dict = array_of_task_filter_spec_time_option.from_dict(array_of_task_filter_spec_time_option_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


