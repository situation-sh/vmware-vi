# ArrayOfAction

A boxed array of *Action*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[Action]**](Action.md) |  | 

## Example

```python
from vmware_vi.models.array_of_action import ArrayOfAction

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfAction from a JSON string
array_of_action_instance = ArrayOfAction.from_json(json)
# print the JSON string representation of the object
print ArrayOfAction.to_json()

# convert the object into a dict
array_of_action_dict = array_of_action_instance.to_dict()
# create an instance of ArrayOfAction from a dict
array_of_action_form_dict = array_of_action.from_dict(array_of_action_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


