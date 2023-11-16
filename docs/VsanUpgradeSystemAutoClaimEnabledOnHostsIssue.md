# VsanUpgradeSystemAutoClaimEnabledOnHostsIssue

Pre-flight check encountered at least one host with auto-claim enabled.  ***Since:*** vSphere API 6.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hosts** | [**List[ManagedObjectReference]**](ManagedObjectReference.md) | Hosts this issue applies to.  ***Since:*** vSphere API 6.0  Refers instances of *HostSystem*.  | 

## Example

```python
from vmware_vi.models.vsan_upgrade_system_auto_claim_enabled_on_hosts_issue import VsanUpgradeSystemAutoClaimEnabledOnHostsIssue

# TODO update the JSON string below
json = "{}"
# create an instance of VsanUpgradeSystemAutoClaimEnabledOnHostsIssue from a JSON string
vsan_upgrade_system_auto_claim_enabled_on_hosts_issue_instance = VsanUpgradeSystemAutoClaimEnabledOnHostsIssue.from_json(json)
# print the JSON string representation of the object
print VsanUpgradeSystemAutoClaimEnabledOnHostsIssue.to_json()

# convert the object into a dict
vsan_upgrade_system_auto_claim_enabled_on_hosts_issue_dict = vsan_upgrade_system_auto_claim_enabled_on_hosts_issue_instance.to_dict()
# create an instance of VsanUpgradeSystemAutoClaimEnabledOnHostsIssue from a dict
vsan_upgrade_system_auto_claim_enabled_on_hosts_issue_form_dict = vsan_upgrade_system_auto_claim_enabled_on_hosts_issue.from_dict(vsan_upgrade_system_auto_claim_enabled_on_hosts_issue_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


