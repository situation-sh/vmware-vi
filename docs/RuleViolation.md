# RuleViolation

The virtual machine if powered on, would violate an affinity/anti-affinity rule.  In this case, the VM can still be powered on manually by a user who knows what they are doing, but VirtualCenter will never automatically move or power on a VM such that it triggers the violation. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**host** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | [optional] 
**rule** | [**ClusterRuleInfo**](ClusterRuleInfo.md) |  | 

## Example

```python
from vmware_vi.models.rule_violation import RuleViolation

# TODO update the JSON string below
json = "{}"
# create an instance of RuleViolation from a JSON string
rule_violation_instance = RuleViolation.from_json(json)
# print the JSON string representation of the object
print RuleViolation.to_json()

# convert the object into a dict
rule_violation_dict = rule_violation_instance.to_dict()
# create an instance of RuleViolation from a dict
rule_violation_form_dict = rule_violation.from_dict(rule_violation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


