# ArrayOfMethodActionArgument

A boxed array of *MethodActionArgument*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[MethodActionArgument]**](MethodActionArgument.md) |  | 

## Example

```python
from vmware_vi.models.array_of_method_action_argument import ArrayOfMethodActionArgument

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfMethodActionArgument from a JSON string
array_of_method_action_argument_instance = ArrayOfMethodActionArgument.from_json(json)
# print the JSON string representation of the object
print ArrayOfMethodActionArgument.to_json()

# convert the object into a dict
array_of_method_action_argument_dict = array_of_method_action_argument_instance.to_dict()
# create an instance of ArrayOfMethodActionArgument from a dict
array_of_method_action_argument_form_dict = array_of_method_action_argument.from_dict(array_of_method_action_argument_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


