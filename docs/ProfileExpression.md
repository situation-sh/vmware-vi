# ProfileExpression


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Identifier of this expression.  The id has to be unique within a Profile. The id can be used as a key while building composite expressions.  ***Since:*** vSphere API 4.0  | 
**display_name** | **str** | User visible display name  ***Since:*** vSphere API 4.0  | 
**negated** | **bool** | Flag indicating if the condition of the expression should be negated.  e.g: conditions like VSwitch0 has vmnic0 connected to it can be turned into VSwitch0 doesn&#39;t have vmnic0 connected to it.  ***Since:*** vSphere API 4.0  | 

## Example

```python
from vmware_vi.models.profile_expression import ProfileExpression

# TODO update the JSON string below
json = "{}"
# create an instance of ProfileExpression from a JSON string
profile_expression_instance = ProfileExpression.from_json(json)
# print the JSON string representation of the object
print ProfileExpression.to_json()

# convert the object into a dict
profile_expression_dict = profile_expression_instance.to_dict()
# create an instance of ProfileExpression from a dict
profile_expression_form_dict = profile_expression.from_dict(profile_expression_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


