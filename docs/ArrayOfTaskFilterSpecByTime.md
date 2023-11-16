# ArrayOfTaskFilterSpecByTime

A boxed array of *TaskFilterSpecByTime*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[TaskFilterSpecByTime]**](TaskFilterSpecByTime.md) |  | 

## Example

```python
from vmware_vi.models.array_of_task_filter_spec_by_time import ArrayOfTaskFilterSpecByTime

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfTaskFilterSpecByTime from a JSON string
array_of_task_filter_spec_by_time_instance = ArrayOfTaskFilterSpecByTime.from_json(json)
# print the JSON string representation of the object
print ArrayOfTaskFilterSpecByTime.to_json()

# convert the object into a dict
array_of_task_filter_spec_by_time_dict = array_of_task_filter_spec_by_time_instance.to_dict()
# create an instance of ArrayOfTaskFilterSpecByTime from a dict
array_of_task_filter_spec_by_time_form_dict = array_of_task_filter_spec_by_time.from_dict(array_of_task_filter_spec_by_time_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


