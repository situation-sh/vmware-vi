# VsanUpgradeSystemV2ObjectsPresentDuringDowngradeIssue

Pre-flight check encountered v2 objects preventing a downgrade.  ***Since:*** vSphere API 6.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuids** | **List[str]** | Object UUIDs of v2 objects.  ***Since:*** vSphere API 6.0  | 

## Example

```python
from vmware_vi.models.vsan_upgrade_system_v2_objects_present_during_downgrade_issue import VsanUpgradeSystemV2ObjectsPresentDuringDowngradeIssue

# TODO update the JSON string below
json = "{}"
# create an instance of VsanUpgradeSystemV2ObjectsPresentDuringDowngradeIssue from a JSON string
vsan_upgrade_system_v2_objects_present_during_downgrade_issue_instance = VsanUpgradeSystemV2ObjectsPresentDuringDowngradeIssue.from_json(json)
# print the JSON string representation of the object
print VsanUpgradeSystemV2ObjectsPresentDuringDowngradeIssue.to_json()

# convert the object into a dict
vsan_upgrade_system_v2_objects_present_during_downgrade_issue_dict = vsan_upgrade_system_v2_objects_present_during_downgrade_issue_instance.to_dict()
# create an instance of VsanUpgradeSystemV2ObjectsPresentDuringDowngradeIssue from a dict
vsan_upgrade_system_v2_objects_present_during_downgrade_issue_form_dict = vsan_upgrade_system_v2_objects_present_during_downgrade_issue.from_dict(vsan_upgrade_system_v2_objects_present_during_downgrade_issue_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


