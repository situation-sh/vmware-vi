# VsanUpgradeSystemHostsDisconnectedIssue

Pre-flight check encountered at least one host that is disconnected or not responding.  ***Since:*** vSphere API 6.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hosts** | [**List[ManagedObjectReference]**](ManagedObjectReference.md) | Hosts this issue applies to.  ***Since:*** vSphere API 6.0  Refers instances of *HostSystem*.  | 

## Example

```python
from vmware_vi.models.vsan_upgrade_system_hosts_disconnected_issue import VsanUpgradeSystemHostsDisconnectedIssue

# TODO update the JSON string below
json = "{}"
# create an instance of VsanUpgradeSystemHostsDisconnectedIssue from a JSON string
vsan_upgrade_system_hosts_disconnected_issue_instance = VsanUpgradeSystemHostsDisconnectedIssue.from_json(json)
# print the JSON string representation of the object
print VsanUpgradeSystemHostsDisconnectedIssue.to_json()

# convert the object into a dict
vsan_upgrade_system_hosts_disconnected_issue_dict = vsan_upgrade_system_hosts_disconnected_issue_instance.to_dict()
# create an instance of VsanUpgradeSystemHostsDisconnectedIssue from a dict
vsan_upgrade_system_hosts_disconnected_issue_form_dict = vsan_upgrade_system_hosts_disconnected_issue.from_dict(vsan_upgrade_system_hosts_disconnected_issue_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


