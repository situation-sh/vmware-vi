# ArrayOfRuleViolation

A boxed array of *RuleViolation*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[RuleViolation]**](RuleViolation.md) |  | 

## Example

```python
from vmware_vi.models.array_of_rule_violation import ArrayOfRuleViolation

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfRuleViolation from a JSON string
array_of_rule_violation_instance = ArrayOfRuleViolation.from_json(json)
# print the JSON string representation of the object
print ArrayOfRuleViolation.to_json()

# convert the object into a dict
array_of_rule_violation_dict = array_of_rule_violation_instance.to_dict()
# create an instance of ArrayOfRuleViolation from a dict
array_of_rule_violation_form_dict = array_of_rule_violation.from_dict(array_of_rule_violation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


