# TaskFilterSpecByEntity

This data object type specifies a managed entity used to filter task history. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entity** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | 
**recursion** | [**TaskFilterSpecRecursionOptionEnum**](TaskFilterSpecRecursionOptionEnum.md) |  | 

## Example

```python
from vmware_vi.models.task_filter_spec_by_entity import TaskFilterSpecByEntity

# TODO update the JSON string below
json = "{}"
# create an instance of TaskFilterSpecByEntity from a JSON string
task_filter_spec_by_entity_instance = TaskFilterSpecByEntity.from_json(json)
# print the JSON string representation of the object
print TaskFilterSpecByEntity.to_json()

# convert the object into a dict
task_filter_spec_by_entity_dict = task_filter_spec_by_entity_instance.to_dict()
# create an instance of TaskFilterSpecByEntity from a dict
task_filter_spec_by_entity_form_dict = task_filter_spec_by_entity.from_dict(task_filter_spec_by_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


