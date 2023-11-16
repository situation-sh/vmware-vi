# ArrayOfClusterRuleSpec

A boxed array of *ClusterRuleSpec*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[ClusterRuleSpec]**](ClusterRuleSpec.md) |  | 

## Example

```python
from vmware_vi.models.array_of_cluster_rule_spec import ArrayOfClusterRuleSpec

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfClusterRuleSpec from a JSON string
array_of_cluster_rule_spec_instance = ArrayOfClusterRuleSpec.from_json(json)
# print the JSON string representation of the object
print ArrayOfClusterRuleSpec.to_json()

# convert the object into a dict
array_of_cluster_rule_spec_dict = array_of_cluster_rule_spec_instance.to_dict()
# create an instance of ArrayOfClusterRuleSpec from a dict
array_of_cluster_rule_spec_form_dict = array_of_cluster_rule_spec.from_dict(array_of_cluster_rule_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


