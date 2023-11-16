# ProfileCompositeExpression

DataObject to Compose expressions.  It is used to group expressions together. They are similar to a parentheses in an expression.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**operator** | **str** | Logical operator to be applied between the expressions in the composite expression.  e.g: or, and  ***Since:*** vSphere API 4.0  | 
**expression_name** | **List[str]** | List of expression names that will be used for this composition.  The individual expressions will return a boolean. The return values of the individual expressions will be used to compute the final return value of the CompositeExpression. The expressions specified in the list can themselves be CompositeExpressions.  ***Since:*** vSphere API 4.0  | 

## Example

```python
from vmware_vi.models.profile_composite_expression import ProfileCompositeExpression

# TODO update the JSON string below
json = "{}"
# create an instance of ProfileCompositeExpression from a JSON string
profile_composite_expression_instance = ProfileCompositeExpression.from_json(json)
# print the JSON string representation of the object
print ProfileCompositeExpression.to_json()

# convert the object into a dict
profile_composite_expression_dict = profile_composite_expression_instance.to_dict()
# create an instance of ProfileCompositeExpression from a dict
profile_composite_expression_form_dict = profile_composite_expression.from_dict(profile_composite_expression_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


