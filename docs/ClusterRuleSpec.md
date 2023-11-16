# ClusterRuleSpec

An incremental update to the cluster rules. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | [**ClusterRuleInfo**](ClusterRuleInfo.md) |  | [optional] 

## Example

```python
from vmware_vi.models.cluster_rule_spec import ClusterRuleSpec

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterRuleSpec from a JSON string
cluster_rule_spec_instance = ClusterRuleSpec.from_json(json)
# print the JSON string representation of the object
print ClusterRuleSpec.to_json()

# convert the object into a dict
cluster_rule_spec_dict = cluster_rule_spec_instance.to_dict()
# create an instance of ClusterRuleSpec from a dict
cluster_rule_spec_form_dict = cluster_rule_spec.from_dict(cluster_rule_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


