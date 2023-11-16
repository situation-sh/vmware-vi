# ClusterVmGroup

The *ClusterVmGroup* data object identifies virtual machines for VM-Host rules.  VM-Host rules determine placement of virtual machines on hosts in a cluster. The logic specified in a *ClusterVmHostRuleInfo* object determines where virtual machines can be powered-on.  If a virtual machine is removed from the cluster, it loses its DRS group affiliation. The Server does not restore any group affiliations if the virtual machine is returned to the cluster.  ***Since:*** vSphere API 4.1 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vm** | [**List[ManagedObjectReference]**](ManagedObjectReference.md) | List of virtual machines that are part of this group.  A virtual machine group can contain zero or more virtual machines.  ***Since:*** vSphere API 4.1  Refers instances of *VirtualMachine*.  | [optional] 

## Example

```python
from vmware_vi.models.cluster_vm_group import ClusterVmGroup

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterVmGroup from a JSON string
cluster_vm_group_instance = ClusterVmGroup.from_json(json)
# print the JSON string representation of the object
print ClusterVmGroup.to_json()

# convert the object into a dict
cluster_vm_group_dict = cluster_vm_group_instance.to_dict()
# create an instance of ClusterVmGroup from a dict
cluster_vm_group_form_dict = cluster_vm_group.from_dict(cluster_vm_group_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


