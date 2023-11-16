# CreateCollectorForTasksRequestType

The parameters of *TaskManager.CreateCollectorForTasks*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filter** | [**TaskFilterSpec**](TaskFilterSpec.md) |  | 

## Example

```python
from vmware_vi.models.create_collector_for_tasks_request_type import CreateCollectorForTasksRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of CreateCollectorForTasksRequestType from a JSON string
create_collector_for_tasks_request_type_instance = CreateCollectorForTasksRequestType.from_json(json)
# print the JSON string representation of the object
print CreateCollectorForTasksRequestType.to_json()

# convert the object into a dict
create_collector_for_tasks_request_type_dict = create_collector_for_tasks_request_type_instance.to_dict()
# create an instance of CreateCollectorForTasksRequestType from a dict
create_collector_for_tasks_request_type_form_dict = create_collector_for_tasks_request_type.from_dict(create_collector_for_tasks_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


