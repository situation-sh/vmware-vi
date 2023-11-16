# ArrayOfRunScriptAction

A boxed array of *RunScriptAction*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[RunScriptAction]**](RunScriptAction.md) |  | 

## Example

```python
from vmware_vi.models.array_of_run_script_action import ArrayOfRunScriptAction

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfRunScriptAction from a JSON string
array_of_run_script_action_instance = ArrayOfRunScriptAction.from_json(json)
# print the JSON string representation of the object
print ArrayOfRunScriptAction.to_json()

# convert the object into a dict
array_of_run_script_action_dict = array_of_run_script_action_instance.to_dict()
# create an instance of ArrayOfRunScriptAction from a dict
array_of_run_script_action_form_dict = array_of_run_script_action.from_dict(array_of_run_script_action_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


