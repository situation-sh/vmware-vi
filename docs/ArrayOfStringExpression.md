# ArrayOfStringExpression

A boxed array of *StringExpression*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[StringExpression]**](StringExpression.md) |  | 

## Example

```python
from vmware_vi.models.array_of_string_expression import ArrayOfStringExpression

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfStringExpression from a JSON string
array_of_string_expression_instance = ArrayOfStringExpression.from_json(json)
# print the JSON string representation of the object
print ArrayOfStringExpression.to_json()

# convert the object into a dict
array_of_string_expression_dict = array_of_string_expression_instance.to_dict()
# create an instance of ArrayOfStringExpression from a dict
array_of_string_expression_form_dict = array_of_string_expression.from_dict(array_of_string_expression_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


