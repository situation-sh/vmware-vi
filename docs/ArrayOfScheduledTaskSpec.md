# ArrayOfScheduledTaskSpec

A boxed array of *ScheduledTaskSpec*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[ScheduledTaskSpec]**](ScheduledTaskSpec.md) |  | 

## Example

```python
from vmware_vi.models.array_of_scheduled_task_spec import ArrayOfScheduledTaskSpec

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfScheduledTaskSpec from a JSON string
array_of_scheduled_task_spec_instance = ArrayOfScheduledTaskSpec.from_json(json)
# print the JSON string representation of the object
print ArrayOfScheduledTaskSpec.to_json()

# convert the object into a dict
array_of_scheduled_task_spec_dict = array_of_scheduled_task_spec_instance.to_dict()
# create an instance of ArrayOfScheduledTaskSpec from a dict
array_of_scheduled_task_spec_form_dict = array_of_scheduled_task_spec.from_dict(array_of_scheduled_task_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


