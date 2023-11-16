# DrsRuleViolationEvent

This event records when a virtual machine violates a DRS VM-Host rule.  ***Since:*** vSphere API 4.1 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.drs_rule_violation_event import DrsRuleViolationEvent

# TODO update the JSON string below
json = "{}"
# create an instance of DrsRuleViolationEvent from a JSON string
drs_rule_violation_event_instance = DrsRuleViolationEvent.from_json(json)
# print the JSON string representation of the object
print DrsRuleViolationEvent.to_json()

# convert the object into a dict
drs_rule_violation_event_dict = drs_rule_violation_event_instance.to_dict()
# create an instance of DrsRuleViolationEvent from a dict
drs_rule_violation_event_form_dict = drs_rule_violation_event.from_dict(drs_rule_violation_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


