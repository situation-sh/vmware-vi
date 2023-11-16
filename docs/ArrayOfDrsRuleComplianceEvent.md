# ArrayOfDrsRuleComplianceEvent

A boxed array of *DrsRuleComplianceEvent*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[DrsRuleComplianceEvent]**](DrsRuleComplianceEvent.md) |  | 

## Example

```python
from vmware_vi.models.array_of_drs_rule_compliance_event import ArrayOfDrsRuleComplianceEvent

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfDrsRuleComplianceEvent from a JSON string
array_of_drs_rule_compliance_event_instance = ArrayOfDrsRuleComplianceEvent.from_json(json)
# print the JSON string representation of the object
print ArrayOfDrsRuleComplianceEvent.to_json()

# convert the object into a dict
array_of_drs_rule_compliance_event_dict = array_of_drs_rule_compliance_event_instance.to_dict()
# create an instance of ArrayOfDrsRuleComplianceEvent from a dict
array_of_drs_rule_compliance_event_form_dict = array_of_drs_rule_compliance_event.from_dict(array_of_drs_rule_compliance_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


