# VsanUpgradeSystemWrongEsxVersionIssue

Pre-flight check encountered at least one host with wrong ESX version.  Only 6.0 is allowed.  ***Since:*** vSphere API 6.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hosts** | [**List[ManagedObjectReference]**](ManagedObjectReference.md) | Hosts this issue applies to.  ***Since:*** vSphere API 6.0  Refers instances of *HostSystem*.  | 

## Example

```python
from vmware_vi.models.vsan_upgrade_system_wrong_esx_version_issue import VsanUpgradeSystemWrongEsxVersionIssue

# TODO update the JSON string below
json = "{}"
# create an instance of VsanUpgradeSystemWrongEsxVersionIssue from a JSON string
vsan_upgrade_system_wrong_esx_version_issue_instance = VsanUpgradeSystemWrongEsxVersionIssue.from_json(json)
# print the JSON string representation of the object
print VsanUpgradeSystemWrongEsxVersionIssue.to_json()

# convert the object into a dict
vsan_upgrade_system_wrong_esx_version_issue_dict = vsan_upgrade_system_wrong_esx_version_issue_instance.to_dict()
# create an instance of VsanUpgradeSystemWrongEsxVersionIssue from a dict
vsan_upgrade_system_wrong_esx_version_issue_form_dict = vsan_upgrade_system_wrong_esx_version_issue.from_dict(vsan_upgrade_system_wrong_esx_version_issue_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


