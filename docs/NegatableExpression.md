# NegatableExpression

The base class for any type of setting or configuration to which negation can be applied.  When used in a configuration information object: if *NegatableExpression.negate* is true, then ~(objectValue) will be used for the configuration. If false, then objectValue will be used as it is.  ***Since:*** vSphere API 5.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**negate** | **bool** | Whether the configuration needs to be negated or not.  ***Since:*** vSphere API 5.5  | [optional] 

## Example

```python
from vmware_vi.models.negatable_expression import NegatableExpression

# TODO update the JSON string below
json = "{}"
# create an instance of NegatableExpression from a JSON string
negatable_expression_instance = NegatableExpression.from_json(json)
# print the JSON string representation of the object
print NegatableExpression.to_json()

# convert the object into a dict
negatable_expression_dict = negatable_expression_instance.to_dict()
# create an instance of NegatableExpression from a dict
negatable_expression_form_dict = negatable_expression.from_dict(negatable_expression_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


