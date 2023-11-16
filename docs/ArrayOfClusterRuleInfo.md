# ArrayOfClusterRuleInfo

A boxed array of *ClusterRuleInfo*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[ClusterRuleInfo]**](ClusterRuleInfo.md) |  | 

## Example

```python
from vmware_vi.models.array_of_cluster_rule_info import ArrayOfClusterRuleInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfClusterRuleInfo from a JSON string
array_of_cluster_rule_info_instance = ArrayOfClusterRuleInfo.from_json(json)
# print the JSON string representation of the object
print ArrayOfClusterRuleInfo.to_json()

# convert the object into a dict
array_of_cluster_rule_info_dict = array_of_cluster_rule_info_instance.to_dict()
# create an instance of ArrayOfClusterRuleInfo from a dict
array_of_cluster_rule_info_form_dict = array_of_cluster_rule_info.from_dict(array_of_cluster_rule_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


