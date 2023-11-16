# ArrayOfClusterVmHostRuleInfo

A boxed array of *ClusterVmHostRuleInfo*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[ClusterVmHostRuleInfo]**](ClusterVmHostRuleInfo.md) |  | 

## Example

```python
from vmware_vi.models.array_of_cluster_vm_host_rule_info import ArrayOfClusterVmHostRuleInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfClusterVmHostRuleInfo from a JSON string
array_of_cluster_vm_host_rule_info_instance = ArrayOfClusterVmHostRuleInfo.from_json(json)
# print the JSON string representation of the object
print ArrayOfClusterVmHostRuleInfo.to_json()

# convert the object into a dict
array_of_cluster_vm_host_rule_info_dict = array_of_cluster_vm_host_rule_info_instance.to_dict()
# create an instance of ArrayOfClusterVmHostRuleInfo from a dict
array_of_cluster_vm_host_rule_info_form_dict = array_of_cluster_vm_host_rule_info.from_dict(array_of_cluster_vm_host_rule_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


