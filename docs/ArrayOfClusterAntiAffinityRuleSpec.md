# ArrayOfClusterAntiAffinityRuleSpec

A boxed array of *ClusterAntiAffinityRuleSpec*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[ClusterAntiAffinityRuleSpec]**](ClusterAntiAffinityRuleSpec.md) |  | 

## Example

```python
from vmware_vi.models.array_of_cluster_anti_affinity_rule_spec import ArrayOfClusterAntiAffinityRuleSpec

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfClusterAntiAffinityRuleSpec from a JSON string
array_of_cluster_anti_affinity_rule_spec_instance = ArrayOfClusterAntiAffinityRuleSpec.from_json(json)
# print the JSON string representation of the object
print ArrayOfClusterAntiAffinityRuleSpec.to_json()

# convert the object into a dict
array_of_cluster_anti_affinity_rule_spec_dict = array_of_cluster_anti_affinity_rule_spec_instance.to_dict()
# create an instance of ArrayOfClusterAntiAffinityRuleSpec from a dict
array_of_cluster_anti_affinity_rule_spec_form_dict = array_of_cluster_anti_affinity_rule_spec.from_dict(array_of_cluster_anti_affinity_rule_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


