# PlacementAffinityRule

The *PlacementAffinityRule* data object specifies affinity rules for placement  ***Since:*** vSphere API 6.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rule_type** | **str** | Type of affinity rule.  The set of possible values are described in *PlacementAffinityRuleRuleType_enum*  ***Since:*** vSphere API 6.0  | 
**rule_scope** | **str** | Scope of the affinity rule.  The set of possible values are described in *PlacementAffinityRuleRuleScope_enum*  ***Since:*** vSphere API 6.0  | 
**vms** | [**List[ManagedObjectReference]**](ManagedObjectReference.md) | List of virtual machines that are part of this rule.  ***Since:*** vSphere API 6.0  Refers instances of *VirtualMachine*.  | [optional] 
**keys** | **List[str]** | List of PlacementSpec keys that are part of this rule representing virtual machines yet to be placed.  ***Since:*** vSphere API 6.0  | [optional] 

## Example

```python
from vmware_vi.models.placement_affinity_rule import PlacementAffinityRule

# TODO update the JSON string below
json = "{}"
# create an instance of PlacementAffinityRule from a JSON string
placement_affinity_rule_instance = PlacementAffinityRule.from_json(json)
# print the JSON string representation of the object
print PlacementAffinityRule.to_json()

# convert the object into a dict
placement_affinity_rule_dict = placement_affinity_rule_instance.to_dict()
# create an instance of PlacementAffinityRule from a dict
placement_affinity_rule_form_dict = placement_affinity_rule.from_dict(placement_affinity_rule_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


