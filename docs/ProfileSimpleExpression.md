# ProfileSimpleExpression

DataObject represents a pre-defined expression  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**expression_type** | **str** | Type of the simple expression to instantiate.  The expressionType should be derived from the available expressions as listed in the metadata.  ***Since:*** vSphere API 4.0  | 
**parameter** | [**List[KeyAnyValue]**](KeyAnyValue.md) | The parameters for the expressionType.  The list of parameters needed for a simple expression can be obtained from the metadata.  ***Since:*** vSphere API 4.0  | [optional] 

## Example

```python
from vmware_vi.models.profile_simple_expression import ProfileSimpleExpression

# TODO update the JSON string below
json = "{}"
# create an instance of ProfileSimpleExpression from a JSON string
profile_simple_expression_instance = ProfileSimpleExpression.from_json(json)
# print the JSON string representation of the object
print ProfileSimpleExpression.to_json()

# convert the object into a dict
profile_simple_expression_dict = profile_simple_expression_instance.to_dict()
# create an instance of ProfileSimpleExpression from a dict
profile_simple_expression_form_dict = profile_simple_expression.from_dict(profile_simple_expression_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


