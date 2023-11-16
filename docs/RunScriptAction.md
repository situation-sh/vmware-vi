# RunScriptAction

This data object type specifies a script that is triggered by an alarm.  You can use any elements of the *ActionParameter* enumerated list as part of your script to provide information available at runtime. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**script** | **str** | The fully-qualified path to a shell script that runs on the VirtualCenter server as a result of an alarm.  | 

## Example

```python
from vmware_vi.models.run_script_action import RunScriptAction

# TODO update the JSON string below
json = "{}"
# create an instance of RunScriptAction from a JSON string
run_script_action_instance = RunScriptAction.from_json(json)
# print the JSON string representation of the object
print RunScriptAction.to_json()

# convert the object into a dict
run_script_action_dict = run_script_action_instance.to_dict()
# create an instance of RunScriptAction from a dict
run_script_action_form_dict = run_script_action.from_dict(run_script_action_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


