# StringExpression

The string type of setting or configuration that may get a negated value.  ***Since:*** vSphere API 5.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **str** | The String value that is either used as it is or negated.  ***Since:*** vSphere API 5.5  | [optional] 

## Example

```python
from vmware_vi.models.string_expression import StringExpression

# TODO update the JSON string below
json = "{}"
# create an instance of StringExpression from a JSON string
string_expression_instance = StringExpression.from_json(json)
# print the JSON string representation of the object
print StringExpression.to_json()

# convert the object into a dict
string_expression_dict = string_expression_instance.to_dict()
# create an instance of StringExpression from a dict
string_expression_form_dict = string_expression.from_dict(string_expression_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


