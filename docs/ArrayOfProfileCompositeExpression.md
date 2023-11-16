# ArrayOfProfileCompositeExpression

A boxed array of *ProfileCompositeExpression*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[ProfileCompositeExpression]**](ProfileCompositeExpression.md) |  | 

## Example

```python
from vmware_vi.models.array_of_profile_composite_expression import ArrayOfProfileCompositeExpression

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfProfileCompositeExpression from a JSON string
array_of_profile_composite_expression_instance = ArrayOfProfileCompositeExpression.from_json(json)
# print the JSON string representation of the object
print ArrayOfProfileCompositeExpression.to_json()

# convert the object into a dict
array_of_profile_composite_expression_dict = array_of_profile_composite_expression_instance.to_dict()
# create an instance of ArrayOfProfileCompositeExpression from a dict
array_of_profile_composite_expression_form_dict = array_of_profile_composite_expression.from_dict(array_of_profile_composite_expression_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


