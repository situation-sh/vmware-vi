# ArrayOfIntExpression

A boxed array of *IntExpression*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[IntExpression]**](IntExpression.md) |  | 

## Example

```python
from vmware_vi.models.array_of_int_expression import ArrayOfIntExpression

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfIntExpression from a JSON string
array_of_int_expression_instance = ArrayOfIntExpression.from_json(json)
# print the JSON string representation of the object
print ArrayOfIntExpression.to_json()

# convert the object into a dict
array_of_int_expression_dict = array_of_int_expression_instance.to_dict()
# create an instance of ArrayOfIntExpression from a dict
array_of_int_expression_form_dict = array_of_int_expression.from_dict(array_of_int_expression_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


