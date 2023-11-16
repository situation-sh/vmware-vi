# ClusterDependencyRuleInfo

The *ClusterDependencyRuleInfo* data object indentifies VM-to-VM dependencies.  A VM-VM Dependency rule identifies the following groups. - A virtual machine group - *ClusterDependencyRuleInfo.vmGroup* - A \"depends on\" virtual machine group - *ClusterDependencyRuleInfo.dependsOnVmGroup*.    The VMs in *ClusterDependencyRuleInfo.vmGroup* depends on the list of VMs specified in *ClusterDependencyRuleInfo.dependsOnVmGroup*.  For example, this rule is used during vSphere HA VM recovery orchestration. vSphere HA will not restart the VMs in *ClusterDependencyRuleInfo.vmGroup* until all the VMs in *ClusterDependencyRuleInfo.dependsOnVmGroup* are deemded \"ready\" (See *ClusterVmReadiness*).  All the virtual machines referenced by this rule must be in the same cluster.  ***Since:*** vSphere API 6.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vm_group** | **str** | Virtual group name.  The virtual group may contain one or more virtual machines. *ClusterVmGroup*.*ClusterGroupInfo.name*  ***Since:*** vSphere API 6.5  | 
**depends_on_vm_group** | **str** | Depdendency virtual group name (*ClusterVmGroup*.*ClusterGroupInfo.name*).  The virtual group may contain one or more virtual machines.  ***Since:*** vSphere API 6.5  | 

## Example

```python
from vmware_vi.models.cluster_dependency_rule_info import ClusterDependencyRuleInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterDependencyRuleInfo from a JSON string
cluster_dependency_rule_info_instance = ClusterDependencyRuleInfo.from_json(json)
# print the JSON string representation of the object
print ClusterDependencyRuleInfo.to_json()

# convert the object into a dict
cluster_dependency_rule_info_dict = cluster_dependency_rule_info_instance.to_dict()
# create an instance of ClusterDependencyRuleInfo from a dict
cluster_dependency_rule_info_form_dict = cluster_dependency_rule_info.from_dict(cluster_dependency_rule_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


