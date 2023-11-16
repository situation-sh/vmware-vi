# ArrayOfProfileSimpleExpression

A boxed array of *ProfileSimpleExpression*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[ProfileSimpleExpression]**](ProfileSimpleExpression.md) |  | 

## Example

```python
from vmware_vi.models.array_of_profile_simple_expression import ArrayOfProfileSimpleExpression

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfProfileSimpleExpression from a JSON string
array_of_profile_simple_expression_instance = ArrayOfProfileSimpleExpression.from_json(json)
# print the JSON string representation of the object
print ArrayOfProfileSimpleExpression.to_json()

# convert the object into a dict
array_of_profile_simple_expression_dict = array_of_profile_simple_expression_instance.to_dict()
# create an instance of ArrayOfProfileSimpleExpression from a dict
array_of_profile_simple_expression_form_dict = array_of_profile_simple_expression.from_dict(array_of_profile_simple_expression_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


