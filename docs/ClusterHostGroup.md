# ClusterHostGroup

The *ClusterHostGroup* data object identifies hosts for VM-Host rules.  VM-Host rules determine placement of virtual machines on hosts in a cluster. The logic specified in a *ClusterVmHostRuleInfo* object determines where virtual machines can be powered-on.  ***Since:*** vSphere API 4.1 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**host** | [**List[ManagedObjectReference]**](ManagedObjectReference.md) | List of hosts that are part of this group.  A host group can contain zero or more hosts.  ***Since:*** vSphere API 4.1  Refers instances of *HostSystem*.  | [optional] 

## Example

```python
from vmware_vi.models.cluster_host_group import ClusterHostGroup

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterHostGroup from a JSON string
cluster_host_group_instance = ClusterHostGroup.from_json(json)
# print the JSON string representation of the object
print ClusterHostGroup.to_json()

# convert the object into a dict
cluster_host_group_dict = cluster_host_group_instance.to_dict()
# create an instance of ClusterHostGroup from a dict
cluster_host_group_form_dict = cluster_host_group.from_dict(cluster_host_group_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


