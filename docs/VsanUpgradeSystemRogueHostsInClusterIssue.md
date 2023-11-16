# VsanUpgradeSystemRogueHostsInClusterIssue

Pre-flight check encountered at least one host that is part of the VSAN cluster but not the VC cluster.  ***Since:*** vSphere API 6.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuids** | **List[str]** | Host UUIDs of rogue hosts.  ***Since:*** vSphere API 6.0  | 

## Example

```python
from vmware_vi.models.vsan_upgrade_system_rogue_hosts_in_cluster_issue import VsanUpgradeSystemRogueHostsInClusterIssue

# TODO update the JSON string below
json = "{}"
# create an instance of VsanUpgradeSystemRogueHostsInClusterIssue from a JSON string
vsan_upgrade_system_rogue_hosts_in_cluster_issue_instance = VsanUpgradeSystemRogueHostsInClusterIssue.from_json(json)
# print the JSON string representation of the object
print VsanUpgradeSystemRogueHostsInClusterIssue.to_json()

# convert the object into a dict
vsan_upgrade_system_rogue_hosts_in_cluster_issue_dict = vsan_upgrade_system_rogue_hosts_in_cluster_issue_instance.to_dict()
# create an instance of VsanUpgradeSystemRogueHostsInClusterIssue from a dict
vsan_upgrade_system_rogue_hosts_in_cluster_issue_form_dict = vsan_upgrade_system_rogue_hosts_in_cluster_issue.from_dict(vsan_upgrade_system_rogue_hosts_in_cluster_issue_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


