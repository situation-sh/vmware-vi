# VsanUpgradeSystemPreflightCheckIssue

Base class for a pre-flight check issue.  Can be used directly but usually a derived class with a specific issue type is used.  ***Since:*** vSphere API 6.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**msg** | **str** | Message describing the issue.  ***Since:*** vSphere API 6.0  | 

## Example

```python
from vmware_vi.models.vsan_upgrade_system_preflight_check_issue import VsanUpgradeSystemPreflightCheckIssue

# TODO update the JSON string below
json = "{}"
# create an instance of VsanUpgradeSystemPreflightCheckIssue from a JSON string
vsan_upgrade_system_preflight_check_issue_instance = VsanUpgradeSystemPreflightCheckIssue.from_json(json)
# print the JSON string representation of the object
print VsanUpgradeSystemPreflightCheckIssue.to_json()

# convert the object into a dict
vsan_upgrade_system_preflight_check_issue_dict = vsan_upgrade_system_preflight_check_issue_instance.to_dict()
# create an instance of VsanUpgradeSystemPreflightCheckIssue from a dict
vsan_upgrade_system_preflight_check_issue_form_dict = vsan_upgrade_system_preflight_check_issue.from_dict(vsan_upgrade_system_preflight_check_issue_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


