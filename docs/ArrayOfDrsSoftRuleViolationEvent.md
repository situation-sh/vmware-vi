# ArrayOfDrsSoftRuleViolationEvent

A boxed array of *DrsSoftRuleViolationEvent*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[DrsSoftRuleViolationEvent]**](DrsSoftRuleViolationEvent.md) |  | 

## Example

```python
from vmware_vi.models.array_of_drs_soft_rule_violation_event import ArrayOfDrsSoftRuleViolationEvent

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfDrsSoftRuleViolationEvent from a JSON string
array_of_drs_soft_rule_violation_event_instance = ArrayOfDrsSoftRuleViolationEvent.from_json(json)
# print the JSON string representation of the object
print ArrayOfDrsSoftRuleViolationEvent.to_json()

# convert the object into a dict
array_of_drs_soft_rule_violation_event_dict = array_of_drs_soft_rule_violation_event_instance.to_dict()
# create an instance of ArrayOfDrsSoftRuleViolationEvent from a dict
array_of_drs_soft_rule_violation_event_form_dict = array_of_drs_soft_rule_violation_event.from_dict(array_of_drs_soft_rule_violation_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


