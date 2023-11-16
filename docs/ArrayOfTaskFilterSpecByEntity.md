# ArrayOfTaskFilterSpecByEntity

A boxed array of *TaskFilterSpecByEntity*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[TaskFilterSpecByEntity]**](TaskFilterSpecByEntity.md) |  | 

## Example

```python
from vmware_vi.models.array_of_task_filter_spec_by_entity import ArrayOfTaskFilterSpecByEntity

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfTaskFilterSpecByEntity from a JSON string
array_of_task_filter_spec_by_entity_instance = ArrayOfTaskFilterSpecByEntity.from_json(json)
# print the JSON string representation of the object
print ArrayOfTaskFilterSpecByEntity.to_json()

# convert the object into a dict
array_of_task_filter_spec_by_entity_dict = array_of_task_filter_spec_by_entity_instance.to_dict()
# create an instance of ArrayOfTaskFilterSpecByEntity from a dict
array_of_task_filter_spec_by_entity_form_dict = array_of_task_filter_spec_by_entity.from_dict(array_of_task_filter_spec_by_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


