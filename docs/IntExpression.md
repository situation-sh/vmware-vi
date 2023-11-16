# IntExpression

The integer type of setting or configuration that may get a negated value.  ***Since:*** vSphere API 5.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **int** | The integer value that is either negated or used as it is  ***Since:*** vSphere API 5.5  | [optional] 

## Example

```python
from vmware_vi.models.int_expression import IntExpression

# TODO update the JSON string below
json = "{}"
# create an instance of IntExpression from a JSON string
int_expression_instance = IntExpression.from_json(json)
# print the JSON string representation of the object
print IntExpression.to_json()

# convert the object into a dict
int_expression_dict = int_expression_instance.to_dict()
# create an instance of IntExpression from a dict
int_expression_form_dict = int_expression.from_dict(int_expression_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


