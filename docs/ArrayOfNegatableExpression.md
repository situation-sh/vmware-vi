# ArrayOfNegatableExpression

A boxed array of *NegatableExpression*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[NegatableExpression]**](NegatableExpression.md) |  | 

## Example

```python
from vmware_vi.models.array_of_negatable_expression import ArrayOfNegatableExpression

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfNegatableExpression from a JSON string
array_of_negatable_expression_instance = ArrayOfNegatableExpression.from_json(json)
# print the JSON string representation of the object
print ArrayOfNegatableExpression.to_json()

# convert the object into a dict
array_of_negatable_expression_dict = array_of_negatable_expression_instance.to_dict()
# create an instance of ArrayOfNegatableExpression from a dict
array_of_negatable_expression_form_dict = array_of_negatable_expression.from_dict(array_of_negatable_expression_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


