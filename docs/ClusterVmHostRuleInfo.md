# ClusterVmHostRuleInfo

A *ClusterVmHostRuleInfo* object identifies virtual machines and host groups that determine virtual machine placement. The virtual machines and hosts referenced by a VM-Host rule must be in the same cluster.  A VM-Host rule identifies the following groups. - A virtual machine group (*ClusterVmGroup*). - Two host groups - an affine host group and an anti-affine host group   (*ClusterHostGroup*).   At least one of the groups must contain one or more hosts.    *ClusterVmHostRuleInfo* stores only the names of the relevant virtual machine and host groups. The group contents are stored in the virtual machine and host group objects.  When you modify a VM-Host rule, only the fields that are specified are set.  ***Since:*** vSphere API 4.1 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vm_group_name** | **str** | Virtual group name (*ClusterVmGroup*.*ClusterGroupInfo.name*).  The virtual group may contain one or more virtual machines.  ***Since:*** vSphere API 4.1  | [optional] 
**affine_host_group_name** | **str** | Name of the affine host group (*ClusterHostGroup*.*ClusterGroupInfo.name*).  The affine host group identifies hosts on which *ClusterVmHostRuleInfo.vmGroupName* virtual machines can be powered-on. The value of the *ClusterRuleInfo.mandatory* property determines how the Server interprets the rule.  ***Since:*** vSphere API 4.1  | [optional] 
**anti_affine_host_group_name** | **str** | Name of the anti-affine host group (*ClusterHostGroup*.*ClusterGroupInfo.name*).  The anti-affine host group identifies hosts on which *ClusterVmHostRuleInfo.vmGroupName* virtual machines should not be powered-on. The value of the *ClusterRuleInfo.mandatory* property determines how the Server interprets the rule.  ***Since:*** vSphere API 4.1  | [optional] 

## Example

```python
from vmware_vi.models.cluster_vm_host_rule_info import ClusterVmHostRuleInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterVmHostRuleInfo from a JSON string
cluster_vm_host_rule_info_instance = ClusterVmHostRuleInfo.from_json(json)
# print the JSON string representation of the object
print ClusterVmHostRuleInfo.to_json()

# convert the object into a dict
cluster_vm_host_rule_info_dict = cluster_vm_host_rule_info_instance.to_dict()
# create an instance of ClusterVmHostRuleInfo from a dict
cluster_vm_host_rule_info_form_dict = cluster_vm_host_rule_info.from_dict(cluster_vm_host_rule_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


