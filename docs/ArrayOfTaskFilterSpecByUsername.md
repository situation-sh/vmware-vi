# ArrayOfTaskFilterSpecByUsername

A boxed array of *TaskFilterSpecByUsername*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[TaskFilterSpecByUsername]**](TaskFilterSpecByUsername.md) |  | 

## Example

```python
from vmware_vi.models.array_of_task_filter_spec_by_username import ArrayOfTaskFilterSpecByUsername

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfTaskFilterSpecByUsername from a JSON string
array_of_task_filter_spec_by_username_instance = ArrayOfTaskFilterSpecByUsername.from_json(json)
# print the JSON string representation of the object
print ArrayOfTaskFilterSpecByUsername.to_json()

# convert the object into a dict
array_of_task_filter_spec_by_username_dict = array_of_task_filter_spec_by_username_instance.to_dict()
# create an instance of ArrayOfTaskFilterSpecByUsername from a dict
array_of_task_filter_spec_by_username_form_dict = array_of_task_filter_spec_by_username.from_dict(array_of_task_filter_spec_by_username_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


