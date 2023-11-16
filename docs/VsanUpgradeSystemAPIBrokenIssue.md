# VsanUpgradeSystemAPIBrokenIssue

Pre-flight check encountered a VC plumbing issue.  ***Since:*** vSphere API 6.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hosts** | [**List[ManagedObjectReference]**](ManagedObjectReference.md) | Hosts this issue applies to.  ***Since:*** vSphere API 6.0  Refers instances of *HostSystem*.  | 

## Example

```python
from vmware_vi.models.vsan_upgrade_system_api_broken_issue import VsanUpgradeSystemAPIBrokenIssue

# TODO update the JSON string below
json = "{}"
# create an instance of VsanUpgradeSystemAPIBrokenIssue from a JSON string
vsan_upgrade_system_api_broken_issue_instance = VsanUpgradeSystemAPIBrokenIssue.from_json(json)
# print the JSON string representation of the object
print VsanUpgradeSystemAPIBrokenIssue.to_json()

# convert the object into a dict
vsan_upgrade_system_api_broken_issue_dict = vsan_upgrade_system_api_broken_issue_instance.to_dict()
# create an instance of VsanUpgradeSystemAPIBrokenIssue from a dict
vsan_upgrade_system_api_broken_issue_form_dict = vsan_upgrade_system_api_broken_issue.from_dict(vsan_upgrade_system_api_broken_issue_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


