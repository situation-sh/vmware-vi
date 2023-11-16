# ArrayOfMethodAction

A boxed array of *MethodAction*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[MethodAction]**](MethodAction.md) |  | 

## Example

```python
from vmware_vi.models.array_of_method_action import ArrayOfMethodAction

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfMethodAction from a JSON string
array_of_method_action_instance = ArrayOfMethodAction.from_json(json)
# print the JSON string representation of the object
print ArrayOfMethodAction.to_json()

# convert the object into a dict
array_of_method_action_dict = array_of_method_action_instance.to_dict()
# create an instance of ArrayOfMethodAction from a dict
array_of_method_action_form_dict = array_of_method_action.from_dict(array_of_method_action_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


