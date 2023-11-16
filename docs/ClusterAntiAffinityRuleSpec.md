# ClusterAntiAffinityRuleSpec

The *ClusterAntiAffinityRuleSpec* data object defines a set of virtual machines.  DRS will attempt to schedule the virtual machines to run on different hosts. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vm** | [**List[ManagedObjectReference]**](ManagedObjectReference.md) | List of virtual machine references.  Refers instances of *VirtualMachine*.  | 

## Example

```python
from vmware_vi.models.cluster_anti_affinity_rule_spec import ClusterAntiAffinityRuleSpec

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterAntiAffinityRuleSpec from a JSON string
cluster_anti_affinity_rule_spec_instance = ClusterAntiAffinityRuleSpec.from_json(json)
# print the JSON string representation of the object
print ClusterAntiAffinityRuleSpec.to_json()

# convert the object into a dict
cluster_anti_affinity_rule_spec_dict = cluster_anti_affinity_rule_spec_instance.to_dict()
# create an instance of ClusterAntiAffinityRuleSpec from a dict
cluster_anti_affinity_rule_spec_form_dict = cluster_anti_affinity_rule_spec.from_dict(cluster_anti_affinity_rule_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


