# MethodActionArgument

This data object type defines a named argument for an operation. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**Any**](Any.md) |  | [optional] 

## Example

```python
from vmware_vi.models.method_action_argument import MethodActionArgument

# TODO update the JSON string below
json = "{}"
# create an instance of MethodActionArgument from a JSON string
method_action_argument_instance = MethodActionArgument.from_json(json)
# print the JSON string representation of the object
print MethodActionArgument.to_json()

# convert the object into a dict
method_action_argument_dict = method_action_argument_instance.to_dict()
# create an instance of MethodActionArgument from a dict
method_action_argument_form_dict = method_action_argument.from_dict(method_action_argument_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


