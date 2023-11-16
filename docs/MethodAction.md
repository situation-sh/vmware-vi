# MethodAction

This data object type defines an operation and its arguments, invoked on a particular entity. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the operation.  | 
**argument** | [**List[MethodActionArgument]**](MethodActionArgument.md) | An array consisting of the arguments for the operation.  | [optional] 

## Example

```python
from vmware_vi.models.method_action import MethodAction

# TODO update the JSON string below
json = "{}"
# create an instance of MethodAction from a JSON string
method_action_instance = MethodAction.from_json(json)
# print the JSON string representation of the object
print MethodAction.to_json()

# convert the object into a dict
method_action_dict = method_action_instance.to_dict()
# create an instance of MethodAction from a dict
method_action_form_dict = method_action.from_dict(method_action_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


