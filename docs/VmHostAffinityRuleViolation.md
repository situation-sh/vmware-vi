# VmHostAffinityRuleViolation

The virtual machine if powered on or VMotioned, would violate a VM-Host affinity rule.  ***Since:*** vSphere API 4.1 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vm_name** | **str** | The vm that can not be powered on or VMotioned without violating a rule.  ***Since:*** vSphere API 4.1  | 
**host_name** | **str** | The host that the virtual machine can not be powered on without violating a rule.  ***Since:*** vSphere API 4.1  | 

## Example

```python
from vmware_vi.models.vm_host_affinity_rule_violation import VmHostAffinityRuleViolation

# TODO update the JSON string below
json = "{}"
# create an instance of VmHostAffinityRuleViolation from a JSON string
vm_host_affinity_rule_violation_instance = VmHostAffinityRuleViolation.from_json(json)
# print the JSON string representation of the object
print VmHostAffinityRuleViolation.to_json()

# convert the object into a dict
vm_host_affinity_rule_violation_dict = vm_host_affinity_rule_violation_instance.to_dict()
# create an instance of VmHostAffinityRuleViolation from a dict
vm_host_affinity_rule_violation_form_dict = vm_host_affinity_rule_violation.from_dict(vm_host_affinity_rule_violation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


