# VsanUpgradeSystemMissingHostsInClusterIssue

Pre-flight check encountered at least one host that is part of the VC cluster but not the VSAN cluster.  ***Since:*** vSphere API 6.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hosts** | [**List[ManagedObjectReference]**](ManagedObjectReference.md) | Hosts this issue applies to.  ***Since:*** vSphere API 6.0  Refers instances of *HostSystem*.  | 

## Example

```python
from vmware_vi.models.vsan_upgrade_system_missing_hosts_in_cluster_issue import VsanUpgradeSystemMissingHostsInClusterIssue

# TODO update the JSON string below
json = "{}"
# create an instance of VsanUpgradeSystemMissingHostsInClusterIssue from a JSON string
vsan_upgrade_system_missing_hosts_in_cluster_issue_instance = VsanUpgradeSystemMissingHostsInClusterIssue.from_json(json)
# print the JSON string representation of the object
print VsanUpgradeSystemMissingHostsInClusterIssue.to_json()

# convert the object into a dict
vsan_upgrade_system_missing_hosts_in_cluster_issue_dict = vsan_upgrade_system_missing_hosts_in_cluster_issue_instance.to_dict()
# create an instance of VsanUpgradeSystemMissingHostsInClusterIssue from a dict
vsan_upgrade_system_missing_hosts_in_cluster_issue_form_dict = vsan_upgrade_system_missing_hosts_in_cluster_issue.from_dict(vsan_upgrade_system_missing_hosts_in_cluster_issue_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


