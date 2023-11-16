# ArrayOfTaskFilterSpec

A boxed array of *TaskFilterSpec*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[TaskFilterSpec]**](TaskFilterSpec.md) |  | 

## Example

```python
from vmware_vi.models.array_of_task_filter_spec import ArrayOfTaskFilterSpec

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfTaskFilterSpec from a JSON string
array_of_task_filter_spec_instance = ArrayOfTaskFilterSpec.from_json(json)
# print the JSON string representation of the object
print ArrayOfTaskFilterSpec.to_json()

# convert the object into a dict
array_of_task_filter_spec_dict = array_of_task_filter_spec_instance.to_dict()
# create an instance of ArrayOfTaskFilterSpec from a dict
array_of_task_filter_spec_form_dict = array_of_task_filter_spec.from_dict(array_of_task_filter_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


